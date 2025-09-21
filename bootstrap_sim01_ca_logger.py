#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
bootstrap_sim01_ca_logger.py

Cellular Automaton (CA) simulation for Coherence Theory — Sim 1

Key features:
 - Pure finite-protocol CL ∈ [0,1] (no leakage penalty inside CL)
 - Budgets: fuel/throughput, complexity, leakage (leakage only via budget)
 - Robust χ with warm-up & smoothed messenger clock
 - Common Random Numbers (CRN) poke panels reused across estimates
 - Risk-sensitive & closure-gap checks on CRN panels
 - Parallel evaluation (placeholder), per-restart snapshots, final summary.json
 - Calibration to set lambda multipliers from medians
 - Loader to aggregate summaries
 - CLI accepts dashed (--opt-restarts) and underscored (--opt_restarts) flags
 - **Risk gate uses β→∞ extrapolated value (fit r(β)=a+c/β); finite-β gap also reported**

Usage (examples):
  python bootstrap_sim01_ca_logger.py --outdir sims/sim01_ca_parallel --workers 10 \
      --opt-restarts 8 --opt-iters 120 --rs-panels 16 --panel-width 64 \
      --closure-draws 1600 --beta-grid 10 25 50 100 200 --calibration-evals 96

  # or with short aliases:
  python bootstrap_sim01_ca_logger.py -o sims/sim01_ca_parallel -j 10 -R 8 -I 120 -P 16 -W 64 -C 1600 -B 10 25 50 100 200 -E 96
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import random
import time
from dataclasses import dataclass, asdict
from typing import Any, Dict, List, Optional, Sequence, Tuple

import numpy as np

# ---------------------------
# Utilities / Logging
# ---------------------------

def now_hms() -> str:
    return time.strftime("%H:%M:%S", time.localtime())

def jlog(msg: str, **kv):
    rec = {"t": now_hms(), "msg": msg}
    rec.update(kv)
    print(json.dumps(rec), flush=True)

def ensure_dir(p: str):
    os.makedirs(p, exist_ok=True)

def save_json(p: str, obj: Any):
    with open(p, "w") as f:
        json.dump(obj, f, indent=2)

def load_json(p: str) -> Any:
    with open(p, "r") as f:
        return json.load(f)

# ---------------------------
# Config
# ---------------------------

@dataclass
class Config:
    # CA grid
    n: int = 15
    T: int = 50

    # Optimizer/search
    opt_restarts: int = 8
    opt_iters: int = 120
    seeds: Tuple[int, ...] = (42, 53)

    # Workers (parallel hint; core loops are still CPU-bound)
    workers: int = 10

    # Calibration
    calibration_evals: int = 96

    # Risk/closure panels
    rs_panels: int = 16     # number of poke “panels”
    panel_width: int = 64   # pokes per panel
    closure_draws: int = 1600
    beta_grid: Tuple[int, ...] = (10, 25, 50, 100, 200)

    # Budgets lambdas (calibrated)
    lambda_fuel: Optional[float] = None
    lambda_cpx: Optional[float] = None
    lambda_leak: Optional[float] = None

    # Thresholds (review gates)
    risk_gap_pct_threshold: float = 1.0
    closure_gap_pct_threshold: float = 1.0
    attainment_gap_threshold: float = 0.45  # vs p95 CL ceiling

    # Poke parameter ranges
    p_noise_range: Tuple[float, float] = (0.05, 0.20)
    q_adv_range: Tuple[float, float] = (0.01, 0.15)

    # Chi parameters
    chi_s_min: int = 5
    chi_core_frac: Tuple[float, float] = (0.25, 0.75)
    chi_theta: float = 0.05
    chi_smooth_w: int = 5
    chi_warmup: int = 3

    # Protocol defaults for CL
    s_mins: Tuple[int, ...] = (5,)
    tau_holds: Tuple[int, ...] = (5,)
    m_mins: Tuple[int, ...] = (5,)
    theta_msgs: Tuple[float, ...] = (0.5,)
    schedule_stride: int = 10
    w_S: float = 0.5
    w_M: float = 0.5

    # Leakage normalization (caps)
    L_cap_frac: float = 0.05  # 5% of cells per frame summed over T

# ---------------------------
# CA Simulation
# ---------------------------

def generate_random_pattern(n: int) -> Tuple[np.ndarray, int, List[int], List[int]]:
    radius = random.choice([1, 2, 3])
    birth = sorted(random.sample(range(1, 9), random.randint(1, 4)))
    survival = sorted(random.sample(range(1, 9), random.randint(1, 4)))
    seed_density = random.uniform(0.1, 0.3)
    seed = np.random.choice([0, 1, 2], size=(n, n),
                            p=[1 - seed_density, seed_density * 0.7, seed_density * 0.3])
    return seed, radius, birth, survival

def mutate_pattern(seed: np.ndarray, radius: int, birth: List[int], survival: List[int], n: int) -> Tuple[np.ndarray, int, List[int], List[int]]:
    new_radius = max(1, min(3, radius + random.choice([-1, 0, 1])))

    new_seed = seed.copy()
    flips = random.randint(1, max(1, n // 2))
    for _ in range(flips):
        i, j = random.randrange(n), random.randrange(n)
        if new_seed[i, j] == 0:
            new_seed[i, j] = random.choice([1, 2])
        else:
            new_seed[i, j] = random.choice([0, 1, 2])

    def tweak_rule(rule: List[int]) -> List[int]:
        r = set(rule)
        if random.random() < 0.5 and len(r) < 8:
            r.add(random.randint(1, 8))
        else:
            if len(r) > 1:
                r.discard(random.choice(list(r)))
        return sorted(r)

    new_birth = tweak_rule(birth)
    new_survival = tweak_rule(survival)
    return new_seed, new_radius, new_birth, new_survival

def update_grid(grid: np.ndarray, n: int, radius: int, birth: List[int], survival: List[int]) -> np.ndarray:
    new_grid = np.zeros_like(grid)
    for i in range(n):
        for j in range(n):
            min_i, max_i = max(0, i - radius), min(n, i + radius + 1)
            min_j, max_j = max(0, j - radius), min(n, j + radius + 1)
            neigh = grid[min_i:max_i, min_j:max_j]
            count_1 = np.sum(neigh == 1) - (1 if grid[i, j] == 1 else 0)
            count_2 = np.sum(neigh == 2) - (1 if grid[i, j] == 2 else 0)

            if grid[i, j] == 0:
                if (count_1 + count_2) in birth:
                    new_grid[i, j] = 1 if count_1 >= count_2 else 2
            elif grid[i, j] == 1:
                if count_1 in survival:
                    new_grid[i, j] = 1
                elif count_2 > 0:
                    new_grid[i, j] = 2
            elif grid[i, j] == 2:
                if count_2 in survival:
                    new_grid[i, j] = 2
    return new_grid

def apply_poke(grid: np.ndarray, n: int, p_noise: float, q_adv: float) -> np.ndarray:
    new_grid = grid.copy()
    rand_mat = np.random.rand(n, n)
    mask_noise = rand_mat < p_noise
    if mask_noise.any():
        new_grid[mask_noise] = np.random.choice([0, 1, 2], size=int(mask_noise.sum()))
    rand_mat2 = np.random.rand(n, n)
    mask_adv = (new_grid == 1) & (rand_mat2 < q_adv)
    new_grid[mask_adv] = 0
    return new_grid

def evolve_with_pokes(seed: np.ndarray, n: int, radius: int, birth: List[int], survival: List[int],
                      T: int, p_noise: float, q_adv: float) -> List[np.ndarray]:
    trajectories = []
    grid = seed.copy()
    for _ in range(T):
        grid = update_grid(grid, n, radius, birth, survival)
        grid = apply_poke(grid, n, p_noise, q_adv)
        trajectories.append(grid.copy())
    return trajectories

# ---------------------------
# CL scoring (pure finite-protocol)
# ---------------------------

def connected_component_size(grid: np.ndarray, n: int, state: int = 1) -> int:
    visited = np.zeros_like(grid, dtype=bool)
    max_size = 0
    for i in range(n):
        for j in range(n):
            if grid[i, j] == state and not visited[i, j]:
                stack = [(i, j)]
                size = 0
                while stack:
                    x, y = stack.pop()
                    if visited[x, y]:
                        continue
                    visited[x, y] = True
                    size += 1
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < n and 0 <= ny < n and grid[nx, ny] == state and not visited[nx, ny]:
                            stack.append((nx, ny))
                max_size = max(max_size, size)
    return max_size

def compute_S(trajectories: List[np.ndarray], n: int, s_min: int, tau_hold: int) -> int:
    T = len(trajectories)
    persistent = 0
    for t in range(max(0, T - tau_hold + 1)):
        if all(connected_component_size(trajectories[t + k], n, 1) >= s_min for k in range(tau_hold)):
            persistent = 1
            break
    return persistent

def compute_M(trajectories: List[np.ndarray], n: int, m_min: int, theta_msg: float, S_schedule: Sequence[int]) -> int:
    count = 0
    core = slice(n // 4, 3 * n // 4)
    for t in S_schedule:
        if t >= len(trajectories):
            continue
        messenger_mass = np.sum(trajectories[t][core, core] == 2)
        if messenger_mass >= m_min:
            count += 1
    return 1 if (len(S_schedule) > 0 and count >= theta_msg * len(S_schedule)) else 0

def compute_L(trajectories: List[np.ndarray], n: int, T: int, L_cap_frac: float) -> float:
    total_mess = sum(np.sum(grid == 2) for grid in trajectories)
    L_cap = n * n * T * L_cap_frac
    return total_mess / max(1.0, L_cap)

def compute_CL_CA(trajectories: List[np.ndarray], cfg: Config) -> float:
    T = len(trajectories)
    schedules = [list(range(0, T, cfg.schedule_stride))]
    best = 0.0
    for s_min in cfg.s_mins:
        for th in cfg.tau_holds:
            S = compute_S(trajectories, cfg.n, s_min, th)
            for m_min in cfg.m_mins:
                for theta_msg in cfg.theta_msgs:
                    for sched in schedules:
                        M = compute_M(trajectories, cfg.n, m_min, theta_msg, sched)
                        score = cfg.w_S * S + cfg.w_M * M
                        if score > best:
                            best = score
    return float(best)

def compute_chi(trajectories: List[np.ndarray], cfg: Config) -> float:
    T = len(trajectories)
    n = cfg.n
    core = slice(int(n * cfg.chi_core_frac[0]), int(n * cfg.chi_core_frac[1]))
    tau_dec = T
    for t in range(cfg.chi_warmup, T):
        if connected_component_size(trajectories[t], n, state=1) < cfg.chi_s_min:
            tau_dec = t
            break
    occ = np.array([np.mean(tr[core, core] == 2) for tr in trajectories])
    if cfg.chi_smooth_w > 1:
        kernel = np.ones(cfg.chi_smooth_w) / cfg.chi_smooth_w
        occ_sm = np.convolve(occ, kernel, mode='same')
    else:
        occ_sm = occ
    tau_msg = next((t for t, v in enumerate(occ_sm) if v >= cfg.chi_theta), T)
    return float(tau_dec) / max(1.0, float(tau_msg))

# ---------------------------
# Budgets
# ---------------------------

def B_fuel(radius: int, T: int, n: int) -> float:
    return float(radius) * float(T) * (n ** 2) * 0.005

def B_cpx(radius: int, birth: List[int], survival: List[int]) -> float:
    return float(radius ** 2 + len(birth) + len(survival) + 1)

def B_leak(avg_L: float) -> float:
    return float(avg_L ** 2)

# ---------------------------
# Pokes & CRN Panel
# ---------------------------

def sample_poke(cfg: Config) -> Tuple[float, float]:
    p_noise = random.uniform(*cfg.p_noise_range)
    q_adv = random.uniform(*cfg.q_adv_range)
    return p_noise, q_adv

def make_poke_panel(seed: int, total_draws: int, cfg: Config) -> List[Tuple[float, float]]:
    rng_state = random.getstate()
    random.seed(seed)
    panel = [sample_poke(cfg) for _ in range(total_draws)]
    random.setstate(rng_state)
    return panel

def evaluate_pattern_on_panel(seed_grid: np.ndarray, radius: int, birth: List[int], survival: List[int],
                              poke_indices: Sequence[int], panel: List[Tuple[float, float]],
                              cfg: Config) -> Tuple[float, float]:
    cls = []
    leaks = []
    for idx in poke_indices:
        p_noise, q_adv = panel[idx]
        traj = evolve_with_pokes(seed_grid, cfg.n, radius, birth, survival, cfg.T, p_noise, q_adv)
        cl = compute_CL_CA(traj, cfg)
        L = compute_L(traj, cfg.n, cfg.T, cfg.L_cap_frac)
        cls.append(cl)
        leaks.append(L)
    inf_cl = float(np.min(cls)) if cls else 0.0
    avg_leak = float(np.mean(leaks)) if leaks else 0.0
    return inf_cl, avg_leak

def risk_sensitive_CL_on_panel(seed_grid: np.ndarray, radius: int, birth: List[int], survival: List[int],
                               poke_indices: Sequence[int], panel: List[Tuple[float, float]],
                               beta: float, cfg: Config) -> float:
    scores = []
    for idx in poke_indices:
        p_noise, q_adv = panel[idx]
        traj = evolve_with_pokes(seed_grid, cfg.n, radius, birth, survival, cfg.T, p_noise, q_adv)
        scores.append(compute_CL_CA(traj, cfg))
    scores = np.array(scores, dtype=float)
    if len(scores) == 0:
        return 0.0
    lse = np.log(np.mean(np.exp(-beta * scores)))
    return float(- (1.0 / beta) * lse)

# ---------------------------
# Objective
# ---------------------------

def objective_value(inf_cl: float, avg_leak: float, radius: int, birth: List[int], survival: List[int],
                    lambdas: Dict[str, float], cfg: Config) -> float:
    b_fuel = B_fuel(radius, cfg.T, cfg.n)
    b_cpx = B_cpx(radius, birth, survival)
    b_leak = B_leak(avg_leak)
    obj = inf_cl - lambdas["lambda_fuel"] * b_fuel - lambdas["lambda_cpx"] * b_cpx - lambdas["lambda_leak"] * b_leak
    return float(obj)

# ---------------------------
# Calibration
# ---------------------------

def calibrate_lambdas(cfg: Config, panel: List[Tuple[float, float]]) -> Tuple[Dict[str, float], Dict[str, float]]:
    n = cfg.n
    T = cfg.T
    draws = min(cfg.calibration_evals, len(panel))
    poke_indices = list(range(draws))

    CLs = []
    Bfuels = []
    Bcpxs = []
    Lnorms = []

    for _ in range(draws):
        seed_grid, radius, birth, survival = generate_random_pattern(n)
        sub_idx = poke_indices[:min(8, draws)]
        inf_cl, avg_leak = evaluate_pattern_on_panel(seed_grid, radius, birth, survival, sub_idx, panel, cfg)
        CLs.append(inf_cl)
        Bfuels.append(B_fuel(radius, T, n))
        Bcpxs.append(B_cpx(radius, birth, survival))
        Lnorms.append(avg_leak)

    med = {
        "CL": float(np.median(CLs) if CLs else 0.5),
        "B_fuel": float(np.median(Bfuels) if Bfuels else 1.0),
        "B_cpx": float(np.median(Bcpxs) if Bcpxs else 1.0),
        "L_norm": float(np.median(Lnorms) if Lnorms else 0.1),
        "CL_p95": float(np.percentile(CLs, 95)) if CLs else 0.9
    }

    denom = max(1e-9, med["CL"] / 6.0)
    lambda_fuel = denom / max(1e-9, med["B_fuel"])
    lambda_cpx  = denom / max(1e-9, med["B_cpx"])
    lambda_leak = denom / max(1e-9, med["L_norm"] ** 2 if med["L_norm"] > 0 else 0.01)

    lambdas = {
        "lambda_fuel": float(lambda_fuel),
        "lambda_cpx": float(lambda_cpx),
        "lambda_leak": float(lambda_leak),
    }
    return lambdas, med

# ---------------------------
# Optimizer
# ---------------------------

def make_restart_panel(cfg: Config, panel: List[Tuple[float, float]], restart_id: int) -> List[int]:
    random.seed(restart_id)
    total = cfg.panel_width
    if len(panel) <= total:
        return list(range(len(panel)))
    return random.sample(range(len(panel)), total)

def optimizer_single_seed(seed: int, cfg: Config, lambdas: Dict[str, float],
                          panel: List[Tuple[float, float]], outdir: str) -> Dict[str, Any]:
    random.seed(seed)
    np.random.seed(seed)

    best_obj_over_restarts = -1e9
    best_entry_over_restarts: Optional[Dict[str, Any]] = None

    jlog("optimizer begin", phase="opt", seed=seed)
    for r in range(1, cfg.opt_restarts + 1):
        jlog("restart begin", phase="opt", restart=r, restarts=cfg.opt_restarts)
        seed_grid, radius, birth, survival = generate_random_pattern(cfg.n)
        restart_panel_idx = make_restart_panel(cfg, panel, restart_id=(seed * 1000 + r))
        inf_cl, avg_leak = evaluate_pattern_on_panel(seed_grid, radius, birth, survival,
                                                     restart_panel_idx, panel, cfg)
        current_obj = objective_value(inf_cl, avg_leak, radius, birth, survival, lambdas, cfg)
        best_obj = current_obj
        best_params = (seed_grid.copy(), radius, birth[:], survival[:])
        iters = cfg.opt_iters

        for itn in range(1, iters + 1):
            cand_seed, cand_radius, cand_birth, cand_survival = mutate_pattern(
                seed_grid, radius, birth, survival, cfg.n
            )
            inf_cl_c, avg_leak_c = evaluate_pattern_on_panel(cand_seed, cand_radius, cand_birth, cand_survival,
                                                             restart_panel_idx, panel, cfg)
            cand_obj = objective_value(inf_cl_c, avg_leak_c, cand_radius, cand_birth, cand_survival, lambdas, cfg)
            if cand_obj > current_obj:
                seed_grid, radius, birth, survival = cand_seed, cand_radius, cand_birth, cand_survival
                current_obj = cand_obj
                if cand_obj > best_obj:
                    best_obj = cand_obj
                    best_params = (seed_grid.copy(), radius, birth[:], survival[:])

            if itn % 10 == 0:
                jlog("iter", phase="opt", restart=r, it=itn, iters=iters, best_obj=float(best_obj))

        entry = {
            "seed": seed,
            "restart": r,
            "best_objective": float(best_obj),
            "params": {
                "radius": best_params[1],
                "birth": best_params[2],
                "survival": best_params[3],
            }
        }
        snap_dir = os.path.join(outdir, f"seed_{seed:02d}", f"restart_{r:02d}")
        ensure_dir(snap_dir)
        save_json(os.path.join(snap_dir, "snapshot.json"), entry)

        jlog("restart end", phase="opt", restart=r, best_obj=float(best_obj))

        if best_obj > best_obj_over_restarts:
            best_obj_over_restarts = best_obj
            best_entry_over_restarts = {
                "seed": seed,
                "restart": r,
                "best_objective": float(best_obj),
                "seed_grid": best_params[0],
                "radius": best_params[1],
                "birth": best_params[2],
                "survival": best_params[3],
            }

    jlog("optimizer end", phase="opt", seed=seed,
         best_obj=float(best_obj_over_restarts),
         attainment_gap=None)
    return best_entry_over_restarts or {}

# ---------------------------
# Risk (finite β and β→∞) & Closure gaps (CRN)
# ---------------------------

def linear_fit_extrapolate_to_infty(beta_table: Dict[str, float]) -> Tuple[float, float]:
    """
    Fit r(β) = a + c/β via least squares; return (a, stderr_a).
    a is the β→∞ intercept used for the risk gate.
    """
    betas = np.array(sorted(int(k) for k in beta_table.keys()), dtype=float)
    vals = np.array([beta_table[str(int(b))] for b in betas], dtype=float)
    X = np.vstack([np.ones_like(betas), 1.0 / betas]).T
    coef, residuals, rank, s = np.linalg.lstsq(X, vals, rcond=None)
    a, c = float(coef[0]), float(coef[1])
    if len(betas) > 2 and residuals.size:
        sigma2 = float(residuals[0]) / (len(betas) - 2)
        cov = sigma2 * np.linalg.inv(X.T @ X)
        stderr_a = float(np.sqrt(max(0.0, cov[0, 0])))
    else:
        stderr_a = 0.0
    return a, stderr_a

def compute_risk_gap_pct(best_pat: Dict[str, Any], cfg: Config, panel: List[Tuple[float, float]],
                         lambdas: Dict[str, float]) -> Tuple[float, float, float, Dict[str, float], float, float]:
    """
    Returns:
      (gap_finbeta, gap_extrapolated, inf_cl, beta_table, risk_intercept, risk_intercept_stderr)
    """
    idxs = list(range(len(panel)))
    inf_cl, avg_leak = evaluate_pattern_on_panel(best_pat["seed_grid"], best_pat["radius"],
                                                 best_pat["birth"], best_pat["survival"],
                                                 idxs, panel, cfg)

    beta_table: Dict[str, float] = {}
    for b in cfg.beta_grid:
        val = risk_sensitive_CL_on_panel(best_pat["seed_grid"], best_pat["radius"],
                                         best_pat["birth"], best_pat["survival"],
                                         idxs, panel, b, cfg)
        beta_table[str(b)] = float(val)

    # finite-β gap (largest β)
    beta_max = max(cfg.beta_grid)
    rs_fin = beta_table[str(beta_max)]
    denom = max(1e-6, abs(inf_cl))
    gap_fin = 100.0 * max(0.0, rs_fin - inf_cl) / denom

    # β→∞ extrapolated gate
    a, stderr_a = linear_fit_extrapolate_to_infty(beta_table)
    gap_ex = 100.0 * max(0.0, a - inf_cl) / denom

    return float(gap_fin), float(gap_ex), float(inf_cl), beta_table, float(a), float(stderr_a)

def convex_mix(a: Tuple[float, float], b: Tuple[float, float], t: float) -> Tuple[float, float]:
    return (a[0]*(1-t) + b[0]*t, a[1]*(1-t) + b[1]*t)

def compute_closure_gap_pct(best_pat: Dict[str, Any], cfg: Config, panel: List[Tuple[float, float]]) -> float:
    N = cfg.closure_draws
    if len(panel) < 2:
        return 0.0
    rng = np.random.default_rng(123)
    pairs = rng.integers(0, len(panel), size=(N, 2))
    ts = rng.random(N)

    idxs_panel = list(range(len(panel)))
    inf_panel, _ = evaluate_pattern_on_panel(best_pat["seed_grid"], best_pat["radius"],
                                             best_pat["birth"], best_pat["survival"],
                                             idxs_panel, panel, cfg)
    cls = []
    for (i, j), t in zip(pairs, ts):
        p = convex_mix(panel[i], panel[j], float(t))
        traj = evolve_with_pokes(best_pat["seed_grid"], cfg.n, best_pat["radius"],
                                 best_pat["birth"], best_pat["survival"],
                                 cfg.T, p[0], p[1])
        cls.append(compute_CL_CA(traj, cfg))
    if len(cls) == 0:
        return 0.0
    inf_closure = float(np.min(cls))
    denom = max(1e-6, abs(inf_panel))
    gap_pct = 100.0 * max(0.0, inf_closure - inf_panel) / denom
    return float(gap_pct)

# ---------------------------
# Epi proxy (Spearman ρ²)
# ---------------------------

def epi_r2_around_best(best_pat: Dict[str, Any], cfg: Config, panel: List[Tuple[float, float]]) -> float:
    base_grid = best_pat["seed_grid"]
    base_radius = best_pat["radius"]
    base_birth = best_pat["birth"]
    base_surv = best_pat["survival"]
    idxs = list(range(min(cfg.panel_width, len(panel))))

    def dist(a_seed: np.ndarray, a_r: int, a_b: List[int], a_s: List[int]) -> float:
        d_seed = np.mean((a_seed != base_grid).astype(float))
        d_r = abs(a_r - base_radius) / 3.0
        def jacc(a, b):
            A, B = set(a), set(b)
            if not A and not B: return 0.0
            return 1.0 - len(A & B) / max(1, len(A | B))
        d_rules = 0.5 * (jacc(a_b, base_birth) + jacc(a_s, base_surv))
        return d_seed + d_r + d_rules

    base_inf, _ = evaluate_pattern_on_panel(base_grid, base_radius, base_birth, base_surv, idxs, panel, cfg)
    base_obj = base_inf

    D = []
    Y = []
    for _ in range(64):
        m_seed, m_r, m_b, m_s = mutate_pattern(base_grid, base_radius, base_birth, base_surv, cfg.n)
        inf_m, _ = evaluate_pattern_on_panel(m_seed, m_r, m_b, m_s, idxs, panel, cfg)
        D.append(dist(m_seed, m_r, m_b, m_s))
        Y.append(max(0.0, base_obj - inf_m))
    if len(D) < 3:
        return 0.0
    rho = spearmanr_np(np.array(D), np.array(Y))
    return float(max(0.0, min(1.0, rho * rho)))

def spearmanr_np(x: np.ndarray, y: np.ndarray) -> float:
    rx = rankdata(x)
    ry = rankdata(y)
    corr = np.corrcoef(rx, ry)[0,1]
    return float(corr)

def rankdata(a: np.ndarray) -> np.ndarray:
    temp = a.argsort()
    ranks = np.empty_like(temp, dtype=float)
    ranks[temp] = np.arange(len(a), dtype=float)
    _, inv, counts = np.unique(a, return_inverse=True, return_counts=True)
    sums = np.bincount(inv, weights=ranks)
    avg = sums / counts
    return avg[inv]

# ---------------------------
# Pass/Fail
# ---------------------------

def pass_fail_summary(best_objective: float, risk_gap_pct_gate: float, closure_gap_pct: float,
                      cfg: Config) -> Dict[str, Any]:
    return {
        "pass_risk_gap": bool(risk_gap_pct_gate <= cfg.risk_gap_pct_threshold),
        "pass_closure_gap": bool(closure_gap_pct <= cfg.closure_gap_pct_threshold),
        "pass_attainment": True,  # adjusted later vs ceiling
    }

# ---------------------------
# Main run
# ---------------------------

def cg(cfg: Config) -> Config:
    return cfg

def run(cfg: Config, outdir: str, mode: str):
    ensure_dir(outdir)
    sha1 = hashlib.sha1(repr(cfg).encode("utf-8")).hexdigest()
    jlog("start", phase="init", cfg_sha1=sha1)
    jlog("work plan", phase="init", work={
        "calibration_evals": cfg.calibration_evals,
        "opt_restarts": cfg.opt_restarts,
        "opt_iters": cfg.opt_iters,
        "rs_panels": cfg.rs_panels,
        "closure_draws": cfg.closure_draws,
        "workers": cfg.workers
    })

    total_panel_draws = max(cfg.rs_panels * cfg.panel_width, cfg.closure_draws)
    GLOBAL_PANEL = make_poke_panel(seed=12345, total_draws=total_panel_draws, cfg=cg(cfg))

    jlog("calibrating lambdas", phase="calibration")
    lambdas, medians = calibrate_lambdas(cfg, GLOBAL_PANEL)
    cfg.lambda_fuel = lambdas["lambda_fuel"]
    cfg.lambda_cpx = lambdas["lambda_cpx"]
    cfg.lambda_leak = lambdas["lambda_leak"]
    jlog("calibration done", phase="calibration", medians=medians, lambdas=lambdas)

    best_overall: Optional[Dict[str, Any]] = None
    seed_results: List[Dict[str, Any]] = []
    for sd in cfg.seeds:
        entry = optimizer_single_seed(sd, cfg, lambdas, GLOBAL_PANEL, outdir)
        if entry:
            seed_results.append(entry)
            if (best_overall is None) or (entry["best_objective"] > best_overall["best_objective"]):
                best_overall = entry

    if best_overall is None:
        jlog("no solution found", phase="finish")
        return

    # Risk: finite-β and β→∞ (gate)
    risk_gap_fin, risk_gap_ex, inf_cl, beta_table, risk_intercept, risk_intercept_stderr = compute_risk_gap_pct(
        best_overall, cfg, GLOBAL_PANEL, lambdas
    )
    # Closure-gap
    closure_gap_pct = compute_closure_gap_pct(best_overall, cfg, GLOBAL_PANEL)

    # χ at a median poke
    med_idx = len(GLOBAL_PANEL)//2
    p_med = GLOBAL_PANEL[med_idx]
    traj = evolve_with_pokes(best_overall["seed_grid"], cfg.n, best_overall["radius"],
                             best_overall["birth"], best_overall["survival"],
                             cfg.T, p_med[0], p_med[1])
    chi_val = compute_chi(traj, cfg)

    # epi proxy
    epi_val = epi_r2_around_best(best_overall, cfg, GLOBAL_PANEL)

    # attainment gap vs calibration p95 (absolute gap, as before)
    cl_p95 = medians.get("CL_p95", 0.85)
    attainment_gap = max(0.0, cl_p95 - float(best_overall["best_objective"]))

    micro_outside_cone_fraction = 0.0

    # Pass/fail uses EXTRAPOLATED risk gap
    passes = pass_fail_summary(float(best_overall["best_objective"]), float(risk_gap_ex), closure_gap_pct, cfg)
    passes["pass_attainment"] = bool(attainment_gap <= cfg.attainment_gap_threshold)

    summary = {
        "best_objective": float(best_overall["best_objective"]),
        "chi": float(chi_val),
        "inf_cl": float(inf_cl),
        "risk_gap_pct_finbeta": float(risk_gap_fin),   # transparency
        "risk_gap_pct": float(risk_gap_ex),            # GATE value (β→∞)
        "risk_intercept": float(risk_intercept),       # r(β) intercept at β→∞
        "risk_intercept_stderr": float(risk_intercept_stderr),
        "closure_gap_pct": float(closure_gap_pct),
        "attainment_gap": float(attainment_gap),
        "epi_r2": float(epi_val),
        "micro_outside_cone_fraction": float(micro_outside_cone_fraction),
        "passes": {
            **passes,
            "notes": {
                "chi_info": "chi>1 desirable but not a gate; report and discuss.",
                "risk_gate": "Pass uses β→∞ extrapolated risk; finite-β gap also reported."
            }
        },
        "beta_table": beta_table,
        "medians": medians,
        "lambdas": lambdas,
        "params_best": {
            "radius": best_overall["radius"],
            "birth": best_overall["birth"],
            "survival": best_overall["survival"],
        },
        "config": asdict(cfg)
    }

    save_json(os.path.join(outdir, "summary.json"), summary)
    jlog("finish", phase="finish")
    print(f"Done in {time.perf_counter() - START_TIME:.1f}s. Artifacts in: {outdir}")

# ---------------------------
# Loader (aggregate summaries)
# ---------------------------

def load_summaries(root: str) -> List[Dict[str, Any]]:
    out = []
    for dirpath, _, filenames in os.walk(root):
        if "summary.json" in filenames:
            try:
                out.append(load_json(os.path.join(dirpath, "summary.json")))
            except Exception:
                pass
    return out

def write_csv(rows: List[Dict[str, Any]], out_csv: str):
    if not rows:
        return
    keys = sorted({k for row in rows for k in row.keys()})
    with open(out_csv, "w") as f:
        f.write(",".join(keys) + "\n")
        for row in rows:
            vals = []
            for k in keys:
                v = row.get(k, "")
                if isinstance(v, (dict, list)):
                    v = json.dumps(v, separators=(",", ":"))
                vals.append(str(v))
            f.write(",".join(vals) + "\n")

def loader_main(root: str, out_csv: str):
    sums = load_summaries(root)
    rows = []
    for s in sums:
        rows.append({
            "best_objective": s.get("best_objective"),
            "chi": s.get("chi"),
            "inf_cl": s.get("inf_cl"),
            "risk_gap_pct": s.get("risk_gap_pct"),
            "risk_gap_pct_finbeta": s.get("risk_gap_pct_finbeta"),
            "closure_gap_pct": s.get("closure_gap_pct"),
            "attainment_gap": s.get("attainment_gap"),
            "epi_r2": s.get("epi_r2"),
            "pass_risk_gap": s.get("passes", {}).get("pass_risk_gap"),
            "pass_closure_gap": s.get("passes", {}).get("pass_closure_gap"),
            "pass_attainment": s.get("passes", {}).get("pass_attainment"),
            "params_best": json.dumps(s.get("params_best", {}), separators=(",", ":")),
            "config": json.dumps(s.get("config", {}), separators=(",", ":")),
        })
    ensure_dir(os.path.dirname(out_csv))
    write_csv(rows, out_csv)
    print(f"Wrote {len(rows)} rows to {out_csv}")

# ---------------------------
# CLI
# ---------------------------

START_TIME = time.perf_counter()

def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Coherence Theory — Sim 1 (CA)", allow_abbrev=False)

    # Common
    p.add_argument("-o", "--outdir", type=str, default="sims/sim01_ca_parallel", help="Output directory")
    p.add_argument("-j", "--workers", "--workers_count", type=int, default=10, dest="workers")

    # Optimizer
    p.add_argument("-R", "--opt-restarts", "--opt_restarts", type=int, default=8, dest="opt_restarts")
    p.add_argument("-I", "--opt-iters", "--opt_iters", type=int, default=120, dest="opt_iters")

    # Panels / closure
    p.add_argument("-P", "--rs-panels", "--rs_panels", type=int, default=16, dest="rs_panels")
    p.add_argument("-W", "--panel-width", "--panel_width", type=int, default=64, dest="panel_width")
    p.add_argument("-C", "--closure-draws", "--closure_draws", type=int, default=1600, dest="closure_draws")
    p.add_argument("-B", "--beta-grid", "--beta_grid", type=int, nargs="+", default=[10, 25, 50, 100, 200], dest="beta_grid")

    # Calibration
    p.add_argument("-E", "--calibration-evals", "--calibration_evals", type=int, default=96, dest="calibration_evals")

    # Mode / loader
    p.add_argument("-m", "--mode", type=str, default="run", choices=["run", "load"])
    p.add_argument("-r", "--load-root", "--load_root", type=str, default="sims", dest="load_root")
    p.add_argument("-O", "--load-csv", "--load_csv", type=str, default="sims/summary_aggregate.csv", dest="load_csv")

    return p.parse_args()

def main():
    args = parse_args()
    if args.mode == "load":
        loader_main(args.load_root, args.load_csv)
        return

    cfg = Config(
        workers=args.workers,
        opt_restarts=args.opt_restarts,
        opt_iters=args.opt_iters,
        rs_panels=args.rs_panels,
        panel_width=args.panel_width,
        closure_draws=args.closure_draws,
        beta_grid=tuple(args.beta_grid),
        calibration_evals=args.calibration_evals,
    )
    ensure_dir(args.outdir)
    run(cfg, args.outdir, mode="run")

if __name__ == "__main__":
    main()
