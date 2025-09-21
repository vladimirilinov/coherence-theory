#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bootstrap (HARDENED & UNASSAILABLE) — Sim 4: Poke Ensemble Robustness

Key properties:
- Outcome-free ε calibration: increase ε on a fixed schedule (with pre-registered adaptive ramp)
  until worst-permutation ε-net size M ≤ 403. No CL values are inspected during calibration.
- Exact sample sizing: the structured closure surrogate yields exactly `--samples` points.
- Holdout mesh check: report ε̂ = max(train, holdout) to prevent overfitting to the sample used for centers.
- Entropic (soft-min) CLβ aggregator; ablations; verbose progress prints.
- On calibration exhaustion, the run **does not crash**; it records FAIL, emits artifacts, and explains why.

Usage:
  python bootstrap_sim04_hardened.py --path ./coherence_sims_hardened --run \
    --eps 0.004 --samples 1500 --risk-eta 0.015
"""

import os, sys, json, math, time, argparse, pathlib, subprocess, hashlib

# ------------------------------- Helpers --------------------------------------
def ensure_dir(p: str) -> None:
    pathlib.Path(p).mkdir(parents=True, exist_ok=True)

def write(path: str, txt: str, mode=None) -> None:
    ensure_dir(os.path.dirname(path))
    with open(path, "w", encoding="utf-8") as f:
        f.write(txt)
    if mode is not None:
        os.chmod(path, mode)

def write_json(path: str, obj) -> None:
    ensure_dir(os.path.dirname(path))
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, indent=2, sort_keys=True)

def sha256_bytes(b: bytes) -> str:
    h = hashlib.sha256(); h.update(b); return h.hexdigest()

# ------------------------------- Defaults -------------------------------------
DEFAULT_BETA_GRID = [1, 3, 10, 30, 100, 300, 1000]
DEFAULT_CFG = dict(
    rng_seed=777,
    omega=0.20,
    ad_gamma=0.05,
    phase_p=0.05,
    heavy_tail_prob=0.01,
    bootstrap_B=2000,
    sanity=False,
    # calibration knobs (pre-registered, outcome-free)
    eps=0.004,
    eps_grow=1.25,           # starting multiplicative step (may auto-increase on stagnation)
    eps_sample_count=1500,
    risk_eta=0.015,
    beta_grid=DEFAULT_BETA_GRID,
    calib_max_steps=30,      # allow plenty of room to reach M<=403
    calib_adapt_factor=1.5,  # when stagnating, multiply growth by this (capped at 2.0)
    calib_stagnation_k=2,    # how many near-flat steps before adapting
)

# --------------------------- Self-contained runner ----------------------------
RUN_PY = r'''
# sim04 hardened runner (self-contained)
import os, json, math, time, argparse
from typing import List, Tuple
import numpy as np
import matplotlib.pyplot as plt

# ------------------ Bloch-affine primitives ------------------
def rot_x(th): c,s=math.cos(th),math.sin(th); return np.array([[1,0,0],[0,c,-s],[0,s,c]],float)
def rot_y(th): c,s=math.cos(th),math.sin(th); return np.array([[c,0,s],[0,1,0],[-s,0,c]],float)
def rot_z(th): c,s=math.cos(th),math.sin(th); return np.array([[c,-s,0],[s,c,0],[0,0,1]],float)
def dephasing_A(p): p=float(np.clip(p,0.0,0.5)); s=1-2*p; return np.diag([s,s,1.0])
def depolarizing_A(p): p=float(np.clip(p,0.0,1.0)); s=1-p; return np.eye(3)*s
def amplitude_damping_Ab(g): g=float(np.clip(g,0.0,1.0)); A=np.diag([np.sqrt(1-g),np.sqrt(1-g),1-g]); b=np.array([0,0,g],float); return A,b
def spectral_guard(A): s=np.linalg.norm(A,2); return A/s if s>1.0 else A
def compose(A1,b1,A2,b2): return A1@A2, A1@b2 + b1
def mix(A1,b1,A2,b2,t): t=float(np.clip(t,0,1)); return t*A1+(1-t)*A2, t*b1+(1-t)*b2
def diamond_ub(A1,b1,A2,b2): val=2.0*(float(np.linalg.norm(A1-A2,2))+float(np.linalg.norm(b1-b2,2))); return float(min(2.0,val))
def cl_reliability(A): ez=np.array([0,0,1.0]); return 0.5*(1.0+float(np.linalg.norm(A@ez,2)))

# Risk-sensitive soft-min (entropic)
def cl_beta_enumerated(cls: np.ndarray, beta: float) -> float:
    x = cls.astype(np.float64)
    y = -beta * x
    m = np.max(y)
    return float(-(m + np.log(np.mean(np.exp(y - m)))) / beta)

# ------------------ Poke samplers & closure surrogate ------------------
def sample_P_cone(rng, params):
    om,pg,ph=params["omega"],params["ad_gamma"],params["phase_p"]
    th=rng.normal(0,om,3)
    Arot=rot_x(th[0])@rot_y(th[1])@rot_z(th[2])
    Adep=depolarizing_A(abs(rng.normal(0,om/2)))
    Adeph=dephasing_A(np.clip(rng.normal(ph,ph/3),0,0.5))
    A_ad,b_ad=amplitude_damping_Ab(np.clip(rng.normal(pg,pg/3),0,1))
    return spectral_guard(Arot@Adep@Adeph@A_ad), b_ad

def sample_closure_cone(rng, params, heavy_prob=0.01):
    if rng.uniform()<heavy_prob:
        th=rng.normal(0,params["omega"]*3,3)
        Arot=rot_x(th[0])@rot_y(th[1])@rot_z(th[2])
        Adep=depolarizing_A(min(0.95,abs(rng.standard_cauchy())*0.05))
        Adeph=dephasing_A(min(0.45,abs(rng.standard_cauchy())*0.05))
        A=spectral_guard(Arot@Adep@Adeph); b=np.zeros(3)
    else:
        A,b=sample_P_cone(rng,params)
        if rng.uniform()<0.5:
            A2,b2=sample_P_cone(rng,params); A,b=compose(A,b,A2,b2)
        if rng.uniform()<0.5:
            A3,b3=sample_P_cone(rng,params); t=rng.uniform(); A,b=mix(A,b,A3,b3,t)
        A=spectral_guard(A)
    eps=abs(rng.normal(0,0.02)); A=spectral_guard((1-eps)*A+eps*np.eye(3)); b=(1-eps)*b
    return A,b

def structured_closure_sample(params,total,seed):
    """
    Produce exactly `total` points:
      ~60% random closure draws, ~20% dephasing line, ~20% amplitude-damping line,
      remaining filled by end-combos (compose/mix of three canonical endpoints).
    """
    rng=np.random.default_rng(seed); S=[]
    # quotas
    n_rand=int(round(total*0.60))
    n_deph=int(round(total*0.20))
    n_amp =int(round(total*0.20))
    # adjust to sum <= total; fill remainder with combos
    while n_rand+n_deph+n_amp>total:
        n_rand=max(0,n_rand-1)
    # 1) random closure draws
    for _ in range(n_rand):
        S.append(sample_closure_cone(rng,params,params["heavy_tail_prob"]))
    # 2) dephasing line
    if n_deph>0:
        for p in np.linspace(0.0,0.5,n_deph,endpoint=True):
            S.append((dephasing_A(p),np.zeros(3)))
    # 3) amplitude damping line
    if n_amp>0:
        for g in np.linspace(0.0,1.0,n_amp,endpoint=True):
            S.append(amplitude_damping_Ab(g))
    # 4) fill remainder with endpoint combos (compose/mix)
    ends=[(dephasing_A(0.5),np.zeros(3)), amplitude_damping_Ab(1.0), (depolarizing_A(1.0),np.zeros(3))]
    remain = total - len(S)
    if remain>0:
        pairs=[]
        for i in range(len(ends)):
            for j in range(len(ends)):
                pairs.append((ends[i], ends[j]))
        k=0
        while len(S)<total:
            (A1,b1),(A2,b2)=pairs[k%len(pairs)]
            if (k//len(pairs))%2==0:
                A,b=compose(A1,b1,A2,b2)
            else:
                A,b=mix(A1,b1,A2,b2,0.5)
            S.append((spectral_guard(A),b))
            k+=1
    assert len(S)==total
    return S

def greedy_eps_net(points, eps_dia):
    N=len(points); uncovered=set(range(N)); centers=[]; radii=[0.0]*N
    while uncovered:
        i=min(uncovered); centers.append(i)
        Ai,bi=points[i]; to_cover=[]
        for j in uncovered:
            Aj,bj=points[j]; d=diamond_ub(Ai,bi,Aj,bj)
            if d<=eps_dia: to_cover.append(j)
        for j in to_cover: uncovered.discard(j)
    for idx in range(N):
        A,b=points[idx]
        dmin=min(diamond_ub(A,b,points[c][0],points[c][1]) for c in centers)
        radii[idx]=dmin
    return centers, radii

def fixed_pattern_A(params):
    th=params["omega"]/2.0
    A=rot_z(th)@dephasing_A(min(0.1,params["phase_p"]))
    return spectral_guard(A)

def mesh_radius(points, centers):
    if not centers:
        return 0.0
    def d_to_net(A,b):
        return min(diamond_ub(A,b,centers[k][0],centers[k][1]) for k in range(len(centers)))
    return float(max(d_to_net(A,b) for (A,b) in points))

def build_net_with_perms(points, eps_dia, K=3, seed_base=0):
    N = len(points)
    Ms, centers_sets, radii_sets = [], [], []
    idx0 = np.arange(N)
    for s in range(K):
        rng_local = np.random.default_rng(int(seed_base + s))
        idx = idx0.copy(); rng_local.shuffle(idx)
        perm_points = [points[i] for i in idx]
        centers, radii = greedy_eps_net(perm_points, eps_dia)
        Ms.append(len(centers))
        centers_sets.append([perm_points[i] for i in centers])  # store actual (A,b)
        radii_sets.append(radii)
    worst = int(np.argmax(Ms))
    return Ms[worst], centers_sets[worst], radii_sets[worst], Ms

# ------------------ CLI & runner ------------------
def parse_args():
    ap=argparse.ArgumentParser()
    ap.add_argument("--config", required=True)
    ap.add_argument("--no-plots", action="store_true")
    return ap.parse_args()

def main():
    args=parse_args()
    cfg=json.load(open(args.config,"r"))
    rng=np.random.default_rng(int(cfg["rng_seed"]))
    basedir=os.path.dirname(args.config)
    plots=os.path.join(basedir,"plots"); os.makedirs(plots,exist_ok=True)
    results_csv=os.path.join(basedir,"results.csv")
    cert_md=os.path.join(basedir,"Certificate.md")

    print("[sim04] === BEGIN ===")
    print(f"[sim04] seed={cfg['rng_seed']}  samples={cfg['eps_sample_count']}  eps0={cfg['eps']}  grow0={cfg['eps_grow']}")

    # Structured train/holdout samples (fixed, preregistered)
    print("[sim04] building structured closure samples (train & holdout)…")
    sample_pts=structured_closure_sample(cfg, int(cfg["eps_sample_count"]), int(cfg["rng_seed"]))
    holdout_pts=structured_closure_sample(cfg, int(cfg["eps_sample_count"]), int(cfg["rng_seed"])+1)
    print(f"[sim04] samples ready. N_train={len(sample_pts)}  N_holdout={len(holdout_pts)}")

    # Outcome-free calibration loop
    M_target=403
    K_perm=3
    max_steps=int(cfg.get("calib_max_steps", 30))
    eps_try=float(cfg["eps"])
    eps_grow=float(cfg.get("eps_grow", 1.25))
    adapt=float(cfg.get("calib_adapt_factor", 1.5))
    stagn_k=int(cfg.get("calib_stagnation_k", 2))
    prev_M=None; stagn=0; calib_failed=False
    cal_trace=[]
    print(f"[sim04] calibrating ε (target M≤{M_target}, K_perm={K_perm}, max_steps={max_steps})…")
    for step in range(1, max_steps+1):
        M_worst, centers_w, radii_w, Ms_all = build_net_with_perms(sample_pts, eps_try, K_perm, seed_base=0)
        net_w = centers_w
        eps_hat_train = float(max(radii_w)) if radii_w else 0.0
        eps_hat_holdout = mesh_radius(holdout_pts, net_w)
        cal_trace.append({
            "step": step, "eps": eps_try, "Ms_all": Ms_all, "M_worst": int(M_worst),
            "eps_hat_train": eps_hat_train, "eps_hat_holdout": eps_hat_holdout
        })
        print(f"  [cal] step {step:02d}: eps={eps_try:.6g}  M_perms={Ms_all}  M_worst={M_worst}  "
              f"eps_hat(train,holdout)=({eps_hat_train:.4g},{eps_hat_holdout:.4g})")
        if M_worst <= M_target:
            centers = net_w
            eps_hat = max(eps_hat_train, eps_hat_holdout)
            break
        # stagnation detection (outcome-free)
        if prev_M is not None and M_worst >= 0.95*prev_M:
            stagn += 1
            if stagn >= stagn_k and eps_grow < 2.0:
                old = eps_grow
                eps_grow = min(2.0, eps_grow*adapt)
                print(f"  [cal] stagnation detected ({stagn} steps) -> increasing growth: {old:.3g} → {eps_grow:.3g}")
                stagn = 0
        else:
            stagn = 0
        prev_M = M_worst
        eps_try *= eps_grow
    else:
        calib_failed=True
        centers = net_w
        eps_hat = max(eps_hat_train, eps_hat_holdout)
        print(f"[sim04] calibration exhausted (M_worst={M_worst} > {M_target}). Proceeding (PASS will be FALSE).")

    # ε-net finalized
    M=len(centers); mu_star = 1.0/float(M)
    eta=float(cfg["risk_eta"])
    beta_need = math.ceil(math.log(1.0/mu_star)/max(1e-12, eta))
    print(f"[sim04] ε-net finalized: M={M}  μ*={mu_star:.6g}  ε̂={eps_hat:.6g}  β_need(η={eta})={beta_need}")

    # Compute CLs on ε-net under fixed pattern
    A_pat=fixed_pattern_A(cfg)
    net_cls=np.array([cl_reliability(A_pat @ A) for (A,b) in centers], float)
    min_net=float(np.min(net_cls))
    print(f"[sim04] ε-net CL stats: min={min_net:.6f}  mean={net_cls.mean():.6f}")

    # CLβ grid (soft-min)
    beta_grid = list(map(float, cfg["beta_grid"]))
    clb = {}
    print("[sim04] CLβ across β-grid:")
    for i,b in enumerate(beta_grid,1):
        clb[int(b)] = float(cl_beta_enumerated(net_cls, float(b)))
        print(f"  [{i}/{len(beta_grid)}] β={b:<6} -> CLβ={clb[int(b)]:.6f}")

    # Checklist & principled passes
    gap_at_300 = clb.get(300, float('inf')) - min_net
    pass_beta300 = (not calib_failed) and (M <= 403) and (gap_at_300 <= 0.02 + 1e-12)
    beta_satisfy = min((int(b) for b in beta_grid if int(b) >= beta_need), default=None)
    pass_by_need = (beta_satisfy is not None) and ((clb[int(beta_satisfy)] - min_net) <= eta + 1e-12)
    print(f"[sim04] gap@β=300 = {gap_at_300:.6f}  pass_checklist={pass_beta300}  pass_by_beta_need={pass_by_need}  calib_failed={calib_failed}")

    # Ablations
    def nonclosed(n=200):
        vals=[]
        for _ in range(n):
            th=np.random.default_rng().normal(0,cfg["omega"],3)
            A=rot_x(th[0])@rot_y(th[1])@rot_z(th[2])@dephasing_A(cfg["phase_p"])
            A=spectral_guard(A)
            vals.append(cl_reliability(A_pat@A))
        return np.array(vals,float)
    ab_a1 = nonclosed(200)

    def lr_off(n=150):
        vals=[]
        for _ in range(n):
            th=np.random.default_rng().normal(0,cfg["omega"]*4,3)
            A=rot_x(th[0])@rot_y(th[1])@rot_z(th[2])
            Adep=depolarizing_A(min(0.99,abs(np.random.default_rng().standard_cauchy())*0.2))
            Adeph=dephasing_A(min(0.49,abs(np.random.default_rng().standard_cauchy())*0.2))
            A_un = A@Adep@Adeph  # no spectral guard
            vals.append(cl_reliability(A_pat@A_un))
        return np.array(vals,float)
    ab_lr = lr_off(150)
    lr_flag = bool(np.min(ab_lr) < min_net - eps_hat/2.0)
    print(f"[sim04] ablations: nonclosed_min={float(np.min(ab_a1)):.6f}  lr_off_min={float(np.min(ab_lr)):.6f}  lr_guard_violation={lr_flag}")

    # Plots
    def plot_hist(values, outpath, M, min_net):
        plt.figure(figsize=(6,4))
        plt.hist(values, bins=30)
        plt.axvline(min_net, ls="--")
        plt.title(f"ε-net CLs (M={M}, min={min_net:.6f})")
        plt.tight_layout(); plt.savefig(outpath, dpi=150); plt.close()

    def plot_risk(beta_grid, clb, min_net, outpath):
        xs=[1.0/b for b in beta_grid]; ys=[clb[int(b)] for b in beta_grid]
        plt.figure(figsize=(6,4))
        plt.semilogx(beta_grid, ys, marker="o", label="CLβ (ε-net)")
        plt.axhline(min_net, ls="--", label="min over ε-net")
        plt.xlabel("β (log)"); plt.ylabel("CLβ"); plt.legend(); plt.tight_layout()
        plt.savefig(outpath, dpi=150); plt.close()

    print("[sim04] plotting…")
    plot_hist(net_cls, os.path.join(plots,"net_cls_hist.png"), M, min_net)
    plot_risk(beta_grid, clb, min_net, os.path.join(plots,"risk_convergence.png"))
    print("[sim04] plots saved.")

    # Certificate
    cert = f"""# Certificate — ε-net (calibrated), Lipschitz bracket, and CLβ
- Calibration target: M ≤ 403 (ensures log(M)/300 ≤ 0.02)
- Final M = {M}, μ* = 1/M = {1.0/M:.6g}
- ε̂ (max of train/holdout meshes) = {eps_hat:.6g}
- Pattern Lipschitz L = 1/2 ⇒ Deterministic bracket around min: [ {min_net - eps_hat/2:.6f}, {min_net + eps_hat/2:.6f} ]
- β_need(η={eta}) = {beta_need}
- Checklist gap at β=300 = {gap_at_300:.6f}
- pass_checklist = {pass_beta300}
- pass_by_beta_need = {pass_by_need}
- calibration_failed = {calib_failed}

## Calibration trace (outcome-free)
"""
    for e in cal_trace:
        cert += (f"- step {e['step']}: eps={e['eps']:.6g}, M_perms={e['Ms_all']}, "
                 f"M_worst={e['M_worst']}, eps_hat_train={e['eps_hat_train']:.6g}, "
                 f"eps_hat_holdout={e['eps_hat_holdout']:.6g}\n")
    open(cert_md,"w",encoding="utf-8").write(cert)
    print("[sim04] certificate written.")

    # Results TSV
    row = {
        "sim":"sim04_pokes_hardened",
        "commit":"bootstrap_hardened_unassailable",
        "seed": int(cfg["rng_seed"]),
        "config": cfg,
        "budgets": {"throughput": None, "complexity": None, "leakage": None},
        "CL": {"finite_protocol":"quantum_reliability","beta_grid":beta_grid,"CL_beta":clb,"min_net":min_net},
        "KPIs": {"eps_hat": float(eps_hat), "beta_need": int(beta_need), "gap_at_300": float(gap_at_300)},
        "diagnostics":{
            "net_size": int(M),
            "ablation_nonclosed_min": float(np.min(ab_a1)),
            "ablation_lr_off_min": float(np.min(ab_lr)),
            "lr_guard_violation_flag": bool(lr_flag),
            "calibration_failed": bool(calib_failed),
        },
        "passes": bool(pass_beta300),
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    }
    with open(results_csv,"w",encoding="utf-8") as f:
        f.write("sim\tcommit\tseed\tconfig\tbudgets\tCL\tKPIs\tdiagnostics\tpasses\ttimestamp\n")
        f.write("{sim}\t{commit}\t{seed}\t{config}\t{budgets}\t{CL}\t{KPIs}\t{diagnostics}\t{passes}\t{timestamp}\n".format(
            sim=row["sim"], commit=row["commit"], seed=row["seed"],
            config=json.dumps(row["config"], sort_keys=True),
            budgets=json.dumps(row["budgets"], sort_keys=True),
            CL=json.dumps(row["CL"], sort_keys=True),
            KPIs=json.dumps(row["KPIs"], sort_keys=True),
            diagnostics=json.dumps(row["diagnostics"], sort_keys=True),
            passes=str(row["passes"]).upper(),
            timestamp=row["timestamp"]
        ))
    print("[sim04] results.csv written.")
    print("[sim04] === END ===")

if __name__=="__main__":
    main()
'''

# ------------------------------ Bootstrap CLI ---------------------------------
def main():
    pa = argparse.ArgumentParser(description="Bootstrap Sim 4 (Hardened, Unassailable) with ε-net calibration.")
    pa.add_argument("--path", type=str, default="./coherence_sims_hardened", help="Project root to create")
    pa.add_argument("--run", action="store_true", help="Run sim immediately after scaffolding")
    pa.add_argument("--eps", type=float, default=DEFAULT_CFG["eps"], help="Starting ε for calibration")
    pa.add_argument("--eps-grow", type=float, default=DEFAULT_CFG["eps_grow"], help="Multiplicative step for ε (will adapt on stagnation)")
    pa.add_argument("--samples", type=int, default=DEFAULT_CFG["eps_sample_count"], help="Structured closure sample size for ε-net")
    pa.add_argument("--risk-eta", type=float, default=DEFAULT_CFG["risk_eta"], help="Target η for CLβ→min guarantee")
    pa.add_argument("--max-steps", type=int, default=DEFAULT_CFG["calib_max_steps"], help="Max calibration steps before recording failure")
    args = pa.parse_args()

    root = os.path.abspath(args.path)
    simdir = os.path.join(root, "sims", "sim04_pokes")
    plots = os.path.join(simdir, "plots")
    ensure_dir(plots)

    # README/Methods
    write(os.path.join(root,"README.md"), "# Coherence Sims — Hardened Sim 4\n")
    write(os.path.join(simdir,"README.md"), "# Sim 4 (Hardened, Unassailable)\n")
    write(os.path.join(simdir,"Methods.md"), "# Methods\n- Outcome-free ε calibration until M≤403 (with preregistered adaptive growth).\n- Holdout ε̂.\n- Soft-min CLβ.\n- No crash on calibration exhaustion; PASS=FALSE with full trace.\n")

    # Config (pre-registered)
    cfg = dict(DEFAULT_CFG)
    cfg.update(dict(
        eps=float(args.eps),
        eps_grow=float(args.eps_grow),
        eps_sample_count=int(args.samples),
        risk_eta=float(args.risk_eta),
        beta_grid=DEFAULT_BETA_GRID,
        calib_max_steps=int(args.max_steps),
    ))
    cfg_path = os.path.join(simdir, "config.json")
    write_json(cfg_path, cfg)
    print(f"[bootstrap] wrote config -> {cfg_path}")

    # Lock (no imports)
    cfg_hash = sha256_bytes(json.dumps(cfg, sort_keys=True).encode("utf-8"))
    lock_obj = {"config_hash": cfg_hash, "config": cfg}
    lock_path = os.path.join(simdir, "config.lock.json")
    write_json(lock_path, lock_obj)
    print(f"[bootstrap] wrote lock -> {lock_path}  (hash={cfg_hash})")

    # Runner
    run_path = os.path.join(simdir, "run.py")
    write(run_path, RUN_PY)
    print(f"[bootstrap] runner ready -> {run_path}")

    if args.run:
        print("[bootstrap] launching runner with calibrated ε-net…")
        cmd = [sys.executable, run_path, "--config", cfg_path]
        print("[bootstrap] RUN:", " ".join(cmd), f"(cwd={root})")
        subprocess.run(cmd, cwd=root, check=True)
        print("[bootstrap] run complete. See results and plots under sims/sim04_pokes/.")

if __name__ == "__main__":
    main()
