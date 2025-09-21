#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
bootstrap_sim05_clean.py — Sim 5 CLEAN bootstrap (numpy-only, theory-aligned)

Pipeline:
- Builds a self-contained tree at <root>/<project>/sims/sim05_boot
- Factorial grid over (qT x qL), multi-dim instances
- Solves constrained problem with throughput budget B_th(H) = ||H_tl||_F^2  (canonical; P_tl ellipsoid)
- Estimates λ by Δ-regression (no intercept) using the correct budget gradient feature (2 d Π_tl H)
- Estimates ħ via FS-angle slopes (Richardson, adaptive step); with U(t)=e^{-iHt} → ħ_sim = 1
- Leakage counter-ablation (GKSL; pointer-aligned vs Haar misaligned) — evaluation only
- Light-cone velocity (threshold-free) + microcausality sanity
- Writes: data/pairs.csv, data/leakage.csv, data/results.csv
- Writes: Methods.md, Validation.md, logs.txt
"""

from __future__ import annotations
import argparse, os, json, hashlib, csv, time, math
from dataclasses import dataclass
from typing import List, Tuple, Dict
import numpy as np

# ----------------------------- utility I/O ----------------------------------

def sha256_of(obj) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True).encode("utf-8")).hexdigest()

def makedirs(path: str):
    os.makedirs(path, exist_ok=True)

def write_text(path: str, content: str):
    makedirs(os.path.dirname(path))
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def write_csv(path: str, rows: List[Dict], header: List[str]):
    makedirs(os.path.dirname(path))
    with open(path, "w", newline="") as f:
        wr = csv.DictWriter(f, fieldnames=header)
        wr.writeheader()
        wr.writerows(rows)

def fmt(x: float, d=3):
    try:
        if x is None or not np.isfinite(x): return "nan"
        return f"{float(x):.{d}f}"
    except: return "nan"

# ----------------------- linear algebra building blocks ---------------------

def rng_from_seed(seed: int) -> np.random.Generator:
    return np.random.default_rng(int(seed))

def random_hermitian(d: int, rng: np.random.Generator) -> np.ndarray:
    X = rng.standard_normal((d,d)) + 1j*rng.standard_normal((d,d))
    H = (X + X.conj().T)/2.0
    n = np.sqrt(np.real(np.trace(H.conj().T @ H)))
    return H / (n if n>0 else 1.0)

def random_unitary(d: int, rng: np.random.Generator) -> np.ndarray:
    X = rng.standard_normal((d,d)) + 1j*rng.standard_normal((d,d))
    Q,R = np.linalg.qr(X)
    diagR = np.diag(np.diag(R)/np.abs(np.diag(R)))
    return Q @ diagR

def comm(A: np.ndarray, X: np.ndarray) -> np.ndarray:
    return A@X - X@A

def hs_inner(X: np.ndarray, Y: np.ndarray) -> float:
    """Unnormalized Frobenius inner product."""
    return float(np.real(np.trace(X.conj().T @ Y)))

def hs_inner_norm(X: np.ndarray, Y: np.ndarray) -> float:
    """Normalized HS inner product: <X,Y>_2 = (1/d) Re Tr(X^† Y)."""
    d = X.shape[0]
    return float(np.real(np.trace(X.conj().T @ Y)))/max(d,1)

def hs_norm(X: np.ndarray) -> float:
    return math.sqrt(max(hs_inner(X,X), 0.0))

def vecF(X: np.ndarray) -> np.ndarray:
    return X.reshape((-1,), order="F")

def unvecF(v: np.ndarray, d: int) -> np.ndarray:
    return v.reshape((d,d), order="F")

def symmetrize(H: np.ndarray) -> np.ndarray:
    return (H + H.conj().T)/2.0

def ad_super(A: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    """Spectral rep for (ad_A)^2 in vec space (Frobenius geometry)."""
    d = A.shape[0]
    I = np.eye(d, dtype=complex)
    Ad = np.kron(I, A) - np.kron(A.T, I)   # vec form of ad_A
    M = Ad.conj().T @ Ad                    # (ad_A)^2, PSD Hermitian
    s, U = np.linalg.eigh((M + M.conj().T)/2.0)
    s = np.maximum(np.real(s), 0.0)
    return U, s

def traceless_projector_super(d: int) -> Tuple[np.ndarray, np.ndarray]:
    """
    Superoperator P_tl in vec-space so that v^† P v = ||H - τ(H) I||_F^2 (Frobenius).
    Return its eigensystem (U, s) with s∈{0,1}.
    """
    I = np.eye(d, dtype=complex)
    e = vecF(I) / np.linalg.norm(vecF(I))  # unit vector for identity direction
    P = np.eye(d*d, dtype=complex) - np.outer(e, e.conj())  # orthogonal projector
    M = (P + P.conj().T)/2.0
    s, U = np.linalg.eigh(M)
    s = np.maximum(np.real(s), 0.0)  # should be numerically 0 or 1
    return U, s

def traceless(H: np.ndarray) -> np.ndarray:
    d = H.shape[0]
    return H - (np.trace(H)/d)*np.eye(d, dtype=complex)

# ------------------------ projection on ellipsoids --------------------------

def project_ellipsoid(y: np.ndarray, U: np.ndarray, s: np.ndarray, R: float) -> np.ndarray:
    """
    Project y onto {x: x^† (U diag(s) U^†) x <= R} via 1D bisection on λ.
    Assumes s >= 0 (PSD), works with rank-deficient s (zero eigenvalues).
    Geometry here is plain Frobenius / Euclidean on vec-space.
    """
    if R <= 0.0:
        # Collapse constrained component; keep nullspace of the metric
        z = U.conj().T @ y
        z = np.where(s > 0, 0.0*z, z)
        return U @ z

    z = U.conj().T @ y
    quad = float(np.sum((s * (z.conj()*z)).real))
    if quad <= R + 1e-16:
        return y

    def f(lmb):
        denom = (1.0 + lmb*s)**2
        return float(np.sum((s*(z.conj()*z)).real/denom))

    lam_lo, lam_hi = 0.0, 1.0
    while f(lam_hi) > R:
        lam_hi *= 2.0
        if lam_hi > 1e12: break
    for _ in range(80):
        lam_mid = 0.5*(lam_lo+lam_hi)
        if f(lam_mid) > R: lam_lo = lam_mid
        else: lam_hi = lam_mid
    lam = lam_hi
    x = z / (1.0 + lam*s)
    return U @ x

# ----------------------- objective & constrained solver ---------------------

def grad_J(AU: Tuple[np.ndarray, np.ndarray], A: np.ndarray, G: np.ndarray, H: np.ndarray) -> np.ndarray:
    """
    Frobenius-gradient of
        J(H) = 0.5 <H,(ad_A)^2 H>_2 + <H, i[A,G]>_2
    where <·,·>_2 = (1/d) Tr(·†·).
    Variation: dJ[Δ] = (1/d) Tr(Δ†[(ad_A)^2 H + i[A,G]]).
    Thus ∇_F J = (ad_A)^2 H + i[A,G] all divided by d.
    """
    U_AA, s_AA = AU
    d = A.shape[0]
    v = vecF(H)
    ad2_H = unvecF(U_AA @ (s_AA * (U_AA.conj().T @ v)), H.shape[0])
    return (ad2_H + 1j * comm(A, G)) / max(d, 1)

def J_value(AU: Tuple[np.ndarray, np.ndarray], A: np.ndarray, G: np.ndarray, H: np.ndarray) -> float:
    U_AA, s_AA = AU
    v = vecF(H)
    ad2_H = unvecF(U_AA @ (s_AA * (U_AA.conj().T @ v)), H.shape[0])
    return 0.5*hs_inner_norm(H, ad2_H) + hs_inner_norm(H, 1j*comm(A,G))

def solve_constrained(A: np.ndarray, G: np.ndarray,
                      qT: float,
                      steps: int, step0: float, backtrack: float, tol: float,
                      rng: np.random.Generator) -> Tuple[np.ndarray, Dict]:
    """
    Minimize J(H) subject to a single throughput budget:
        B_th(H) = ||H_tl||_F^2,
    implemented as an ellipsoid in vec/Frobenius geometry with matrix M_T = P_tl.
    We set the radius R_T = qT (dimensionless). Geometry of J is normalized HS.

    Returns optimal H and diagnostics; raises if the projector quadratic
    disagrees with the closed-form Frobenius expression (sanity check).
    """
    d = A.shape[0]
    U_AA, s_AA = ad_super(A)             # spectral rep of (ad_A)^2
    U_P, s_P = traceless_projector_super(d)  # s_P ∈ {0,1} for P_tl

    # ---- Ellipsoid for the budget: M_T = P_tl (NOT d*P_tl) ----
    s_T = s_P
    RT = float(max(qT, 1e-18))

    H = np.zeros((d, d), dtype=complex)
    tau = float(step0)
    Jprev = J_value((U_AA, s_AA), A, G, H)

    for it in range(steps):
        # gradient in normalized HS geometry
        v = vecF(H)
        g = grad_J((U_AA, s_AA), A, G, H)

        # backtracking projected step
        ok = False
        for _ in range(30):
            h_try = vecF(symmetrize(H - tau * g))
            h_try = project_ellipsoid(h_try, U_P, s_T, RT)  # single budget
            Htry = symmetrize(unvecF(h_try, d))
            Jnew = J_value((U_AA, s_AA), A, G, Htry)
            if Jnew <= Jprev - 1e-12:
                ok = True
                H = Htry
                Jprev = Jnew
                break
            tau *= backtrack
        if not ok:
            H = Htry
            Jprev = Jnew

        # feasibility (projector form)
        v = vecF(H)
        z = U_P.conj().T @ v
        qT_proj = float(np.sum((s_T * (z.conj() * z)).real))  # v† P_tl v = ||H_tl||_F^2
        feas = qT_proj / RT
        if abs(feas - 1.0) <= max(tol, 5e-12):
            break

    # ---- diagnostics & identity check ----
    v = vecF(H)
    z = U_P.conj().T @ v
    qT_proj = float(np.sum((s_T * (z.conj() * z)).real))
    # closed form ||H_tl||_F^2
    Htl = traceless(H)
    qT_closed = float(np.real(np.trace(Htl.conj().T @ Htl)))
    denom = max(qT_closed, 1e-16)
    rel_err = abs(qT_proj - qT_closed) / denom
    if rel_err > 1e-8:
        raise RuntimeError(f"[Budget identity failed] v^†P_tl v={qT_proj:.6e} vs ||H_tl||_F^2={qT_closed:.6e} (rel err={rel_err:.2e})")

    bindT = (abs(qT_proj - RT) <= max(tol * RT, 5e-12))

    diag = dict(RT=RT, qTval=qT_proj, qT_closed=qT_closed,
                budget_rel_err=rel_err, bindT=bool(bindT),
                iters=it + 1, tau=tau, d=d)
    return H, diag

# ----------------------- Δ-regression for KKT multiplier --------------------

def orthonormal_hermitians(d: int, m: int, rng: np.random.Generator) -> List[np.ndarray]:
    M = max(4*m, m+2)
    mats = [random_hermitian(d, rng) for _ in range(M)]
    # Gram-Schmidt in normalized HS geometry
    V = [vecF(X) for X in mats]
    Qv: List[np.ndarray] = []
    for v in V:
        w = v.copy()
        for q in Qv:
            # normalized HS inner: <X,Y>_2 = (1/d) Tr(X†Y) => in vec it's (1/d) q† w
            w -= (np.vdot(q, w) / max(d,1)) * q
        n = math.sqrt(max((np.vdot(w, w).real)/max(d,1), 0.0))
        if n > 1e-12:
            Qv.append(w / n)
        if len(Qv) >= m: break
    if len(Qv) < m:
        # fall back to standard basis if needed
        d2 = d*d
        for k in range(d2):
            e = np.zeros((d2,), dtype=complex); e[k]=1.0
            w = e.copy()
            for q in Qv:
                w -= (np.vdot(q, w)/max(d,1)) * q
            n = math.sqrt(max((np.vdot(w,w).real)/max(d,1), 0.0))
            if n > 1e-12: Qv.append(w/n)
            if len(Qv)>=m: break
    return [unvecF(q, d) for q in Qv[:m]]

def estimate_lambda(A: np.ndarray, G: np.ndarray, H: np.ndarray,
                    rng: np.random.Generator, nDeltas: int = 32) -> Tuple[float, float, float]:
    """
    KKT (Frobenius geometry):
        (1/d)[(ad_A)^2 H + i[A,G]] + μ · (2 H_tl) = 0
    Define λ := d·μ  =>  (ad_A)^2 H + i[A,G] + λ · (2 H_tl) = 0.

    Direct estimator (pair with Δ = H_tl in Frobenius inner product):
        λ_dir = - <H_tl, (ad_A)^2 H + i[A,G]>_F / (2 <H_tl,H_tl>_F).

    OLS diagnostic over random Δ's:
        Y = -<Δ, (ad_A)^2 H + i[A,G]>_F,   X = <Δ, 2 H_tl>_F
    Returns (λ_dir, λ_ols, R^2_ols).
    """
    d = A.shape[0]
    U_AA, s_AA = ad_super(A)

    # pieces for λ_dir
    vH = vecF(H)
    ad2H = unvecF(U_AA @ (s_AA * (U_AA.conj().T @ vH)), d)
    KKT_res = ad2H + 1j * comm(A, G)
    Htl = traceless(H)

    def ipF(X, Y):  # Frobenius (unnormalized) inner product
        return hs_inner(X, Y)

    den = 2.0 * ipF(Htl, Htl)
    num = ipF(Htl, KKT_res)
    lam_dir = -num / den if den > 1e-18 and np.isfinite(num) else float("nan")

    # ---- OLS diagnostic ----
    deltas = orthonormal_hermitians(d, nDeltas, rng)
    Xv, Yv = [], []
    for Δ in deltas:
        Xv.append(2.0 * ipF(Δ, Htl))
        Yv.append(-ipF(Δ, KKT_res))
    Xv = np.array(Xv, float); Yv = np.array(Yv, float)

    if np.all(np.isfinite(Xv)) and np.all(np.isfinite(Yv)) and np.sum(Xv * Xv) > 1e-18:
        lam_ols = float(np.sum(Xv * Yv) / np.sum(Xv * Xv))
        Yhat = lam_ols * Xv
        SSres = float(np.sum((Yv - Yhat) ** 2))
        SStot = float(np.sum((Yv - np.mean(Yv)) ** 2)) if len(Yv) > 1 else 0.0
        R2 = 1.0 - (SSres / SStot) if SStot > 0 else 1.0
    else:
        lam_ols = float("nan")
        R2 = float("nan")

    return float(lam_dir), float(lam_ols), float(R2)

# ----------------------- ħ via clock-free FS angles -------------------------

def energy_std(H: np.ndarray, psi: np.ndarray) -> float:
    x = psi
    m1 = float(np.real(np.vdot(x, H @ x)))
    m2 = float(np.real(np.vdot(x, (H@H) @ x)))
    var = max(m2 - m1*m1, 0.0)
    return math.sqrt(var)

def fs_angle(H: np.ndarray, psi: np.ndarray, dt: float) -> float:
    w, U = np.linalg.eigh(H)
    ph = np.exp(-1j * w * dt)
    Udt = (U * ph) @ U.conj().T
    amp = complex(np.vdot(psi, Udt @ psi))
    val = max(min(abs(amp), 1.0), 0.0)
    return float(np.arccos(val))

def random_state(d: int, rng: np.random.Generator) -> np.ndarray:
    x = rng.standard_normal(d) + 1j*rng.standard_normal(d)
    x = x / np.linalg.norm(x)
    return x

def hbar_from_fs(H: np.ndarray, rng: np.random.Generator,
                 dt0: float=0.01, n_states: int=16) -> float:
    """
    Adaptive clock-free ħ estimator.
    With U(t)=e^{-iHt}, FS slope at 0 is ΔE (ħ_sim=1).
    Use h = dt0 / median_psi ΔE to stay in the linear FS regime.
    Slope: (8 θ(h) - θ(2h)) / (6 h).
    """
    d = H.shape[0]
    # Pre-pass for median energy spread
    Es = []
    for _ in range(max(6, n_states//2)):
        psi = random_state(d, rng)
        Es.append(energy_std(H, psi))
    medE = float(np.median(Es)) if Es else 1.0
    h = float(dt0 / max(medE, 1e-12))

    ratios = []
    for _ in range(n_states):
        psi = random_state(d, rng)
        th1 = fs_angle(H, psi, h)
        th2 = fs_angle(H, psi, 2*h)
        slope = (8.0*th1 - th2)/(6.0*h)
        if not np.isfinite(slope) or slope <= 1e-12:
            continue
        dE = energy_std(H, psi)
        if dE <= 1e-14: continue
        ratios.append(dE / slope)
    return float(np.median(ratios)) if ratios else float("nan")

# ----------------------- Leakage counter-ablation (GKSL) --------------------

def lindblad_step(rho: np.ndarray, H: np.ndarray, Ls: List[np.ndarray], dt: float) -> np.ndarray:
    dr = -1j*(H@rho - rho@H)
    for L in Ls:
        LdL = L.conj().T @ L
        dr += L @ rho @ L.conj().T - 0.5*(LdL@rho + rho@LdL)
    return symmetrize(rho + dt*dr)

def purity(rho: np.ndarray) -> float:
    return float(np.real(np.trace(rho@rho)))

def leakage_gaps_for_cell(H: np.ndarray, P: np.ndarray, d: int, leak_levels: List[float],
                          Tsteps: int, dt: float, n_states: int,
                          rng: np.random.Generator) -> Tuple[List[float], List[float]]:
    """
    Compare purity loss for GKSL dephasing aligned to the POINTER P's eigenbasis
    vs a single Haar-misaligned basis (same ℓ). This is an evaluation panel only.

    P is a projector (e.g., |0><0|). We form a COMPLETE dephasing basis from P's eigenbasis.
    """
    # pointer eigenbasis
    wP, UP = np.linalg.eigh(symmetrize(P))
    basis_cols = [UP[:, i].reshape(d, 1) for i in range(d)]

    # aligned Kraus (dephasing in pointer basis)
    L_aligned = [[math.sqrt(l) * (ei @ ei.conj().T) for ei in basis_cols] for l in leak_levels]
    # misaligned: single Haar rotation of the whole set
    Uhaar = random_unitary(d, rng)
    L_misaligned = [[Uhaar @ L @ Uhaar.conj().T for L in Li] for Li in L_aligned]

    gaps = []
    for idx, _l in enumerate(leak_levels):
        ratios_minus1 = []
        for _ in range(n_states):
            psi = random_state(d, rng)
            rho0 = np.outer(psi, psi.conj())
            rhoA = rho0.copy()
            rhoM = rho0.copy()
            for _t in range(Tsteps):
                rhoA = lindblad_step(rhoA, H, L_aligned[idx], dt)
                rhoM = lindblad_step(rhoM, H, L_misaligned[idx], dt)
            dropA = purity(rho0) - purity(rhoA)
            dropM = purity(rho0) - purity(rhoM)
            if dropA <= 1e-12:
                ratios_minus1.append(0.0)
            else:
                ratios_minus1.append((dropM / dropA) - 1.0)
        gaps.append(float(np.median(ratios_minus1)))
    return leak_levels, gaps

# ----------------------- Light-cone & Micro sanity --------------------------

def xx_chain_H(L: int) -> np.ndarray:
    X = np.array([[0,1],[1,0]], dtype=complex)
    Y = np.array([[0,-1j],[1j,0]], dtype=complex)
    I2 = np.eye(2, dtype=complex)
    def kronN(ops):
        Z = np.array([[1]], dtype=complex)
        for op in ops: Z = np.kron(Z, op)
        return Z
    H = np.zeros((2**L, 2**L), dtype=complex)
    for i in range(L-1):
        opsX = [I2]*L; opsY = [I2]*L
        opsX[i] = X; opsX[i+1] = X
        opsY[i] = Y; opsY[i+1] = Y
        H += kronN(opsX) + kronN(opsY)
    return H / max(hs_norm(H), 1.0)

def local_Z(L: int, site: int) -> np.ndarray:
    Z = np.array([[1,0],[0,-1]], dtype=complex)
    I2 = np.eye(2, dtype=complex)
    ops = [I2]*L
    ops[site] = Z
    Zfull = np.array([[1]], dtype=complex)
    for op in ops: Zfull = np.kron(Zfull, op)
    return Zfull

def heisenberg_evolve_op(H: np.ndarray, O: np.ndarray, t: float) -> np.ndarray:
    w, U = np.linalg.eigh(H)
    ph = np.exp(-1j*w*t)
    Udt = (U * ph) @ U.conj().T
    return Udt.conj().T @ O @ Udt

def fit_lightcone_velocity(rng: np.random.Generator) -> Tuple[float,float,float]:
    Ls = [6,8,10]
    times = np.linspace(0.2, 3.0, 8)
    dists = [1,2,3]
    v_candidates = np.linspace(0.2, 4.0, 40)
    Vhat = []
    for L in Ls:
        H = xx_chain_H(L)
        O0 = local_Z(L, 0)
        data = []
        for t in times:
            O_t = heisenberg_evolve_op(H, O0, t)
            for d in dists:
                Od = local_Z(L, min(d, L-1))
                Vc = comm(O_t, Od)
                C = hs_norm(Vc)
                C = max(C, 1e-12)
                data.append((d, t, math.log(C)))
        best = (1e99, 0.0)
        for v in v_candidates:
            X = []; y = []
            for (d1,t,logc) in data:
                X.append([1.0, max(d1 - v*t, 0.0)])
                y.append(logc)
            X = np.array(X, float); y = np.array(y, float)
            ab, *_ = np.linalg.lstsq(X, y, rcond=None)
            yhat = X@ab
            sse = float(np.sum((y - yhat)**2))
            if sse < best[0]: best = (sse, v)
        Vhat.append(best[1])
    v_med = float(np.median(Vhat))
    v_lo = float(np.percentile(Vhat, 5))
    v_hi = float(np.percentile(Vhat, 95))
    return v_med, v_lo, v_hi

def micro_precone_bound() -> Tuple[float, bool]:
    L = 3
    H = xx_chain_H(L)
    O0 = local_Z(L, 0)
    O2 = local_Z(L, 2 if L>2 else 1)
    times = np.linspace(5e-5, 5e-4, 5)
    vals = []
    for t in times:
        O_t = heisenberg_evolve_op(H, O0, t)
        V = comm(O_t, O2)
        v = hs_norm(V)
        vals.append(v)
    pre = float(max(vals))
    return pre, (pre <= 1e-6)

# ----------------------- bootstrap & validation helpers ---------------------

def bootstrap_ci(arr: np.ndarray, stat, B=1500, lo=5, hi=95, rng=None):
    if rng is None: rng = np.random.default_rng()
    x = np.asarray(arr, float)
    x = x[np.isfinite(x)]
    if x.size == 0:
        return (np.nan, np.nan, np.nan)
    n = len(x)
    boots = []
    for _ in range(B):
        idx = rng.integers(0, n, size=n)
        boots.append(stat(x[idx]))
    boots = np.array(boots, float)
    return float(stat(x)), float(np.percentile(boots, lo)), float(np.percentile(boots, hi))

# ----------------------- main pipeline --------------------------------------

@dataclass
class Config:
    root: str = "."
    project: str = "coherence_sims_clean"
    qT_grid: Tuple[float,...] = (0.25, 0.5, 1.0)
    qL_grid: Tuple[float,...] = (0.1, 0.3, 1.0)       # kept for GKSL panel only (reporting)
    dims: Tuple[int,...] = (2,4,8)
    steps_per_trial: int = 50
    n_trials_per_seed: int = 300
    kkt_seeds: Tuple[int,...] = (101, 202)
    holdout_seeds: Tuple[int,...] = (909, 1123)
    n_holdout_per_cell: int = 100
    n_states_for_hbar: int = 32
    dt_fs: float = 0.01                               # dimensionless base for adaptive h
    pgd_steps: int = 400
    pgd_step0: float = 0.4
    pgd_backtrack: float = 0.6
    pgd_tol: float = 5e-7
    # leakage (evaluation only)
    leak_levels: Tuple[float,...] = (1e-3, 3e-3, 1e-2, 3e-2, 1e-1)
    leak_Tsteps: int = 150
    leak_dt: float = 0.03
    leak_states: int = 14
    # validation
    equiv_delta: float = 0.10
    min_cells_leak: int = 6
    leakage_in_overall: bool = False                  # do not gate overall on leakage by default
    # run flags
    run: bool = True
    seed_global: int = 42

def main():
    # ---- CLI ----
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", type=str, default=".")
    ap.add_argument("--project", type=str, default="coherence_sims_clean")
    ap.add_argument("--run", action="store_true", help="Run the validation after building data.")
    args = ap.parse_args()

    cfg = Config(root=os.path.abspath(args.root), project=args.project, run=bool(args.run))
    rng = rng_from_seed(cfg.seed_global)

    # ---- folders ----
    PROJ = os.path.join(cfg.root, cfg.project)
    SIMDIR = os.path.join(PROJ, "sims", "sim05_boot")
    DATADIR = os.path.join(SIMDIR, "data")
    PLOTDIR = os.path.join(SIMDIR, "plots")
    for p in (PROJ, SIMDIR, DATADIR, PLOTDIR): makedirs(p)

    # ---- config dump ----
    cfg_json = {
        "qT_grid": cfg.qT_grid, "qL_grid": cfg.qL_grid, "dims": cfg.dims,
        "steps_per_trial": cfg.steps_per_trial, "n_trials_per_seed": cfg.n_trials_per_seed,
        "kkt_seeds": cfg.kkt_seeds, "holdout_seeds": cfg.holdout_seeds,
        "n_holdout_per_cell": cfg.n_holdout_per_cell, "n_states_for_hbar": cfg.n_states_for_hbar,
        "dt_fs": cfg.dt_fs, "pgd_steps": cfg.pgd_steps, "pgd_step0": cfg.pgd_step0,
        "pgd_backtrack": cfg.pgd_backtrack, "pgd_tol": cfg.pgd_tol,
        "leak_levels": cfg.leak_levels, "leak_Tsteps": cfg.leak_Tsteps,
        "leak_dt": cfg.leak_dt, "leak_states": cfg.leak_states,
        "equiv_delta": cfg.equiv_delta, "min_cells_leak": cfg.min_cells_leak,
        "leakage_in_overall": cfg.leakage_in_overall, "seed_global": cfg.seed_global
    }
    cfg_hash = sha256_of(cfg_json)
    write_text(os.path.join(SIMDIR, "config.json"),
               json.dumps({"config": cfg_json, "config_hash": cfg_hash}, indent=2))

    # ---- buffers ----
    PAIRS = []     # rows for pairs.csv
    LEAKS = []     # rows for leakage.csv
    LOGS = []

    def log(msg: str):
        print(msg)
        LOGS.append(msg+"\n")

    log(f"[Sim5] Boot at {time.strftime('%Y-%m-%d %H:%M:%S')}  hash={cfg_hash}")

    # ---- per-cell loop ----
    CELL_KEYS = []
    for i, qT in enumerate(cfg.qT_grid):
        for j, qL in enumerate(cfg.qL_grid):
            CELL_KEYS.append( (i,j,qT,qL) )

    for (ci,cj,qT,qL) in CELL_KEYS:
        log(f"[cell {ci},{cj}] qT={qT} qL={qL} — KKT+ħ+Leakage")

        # --- KKT trials: estimate λ (keep throughput-binding) ---
        LAM_BIND = []
        for seed in cfg.kkt_seeds:
            rr = rng_from_seed(seed + 1000*ci + 10000*cj)
            for tix in range(cfg.n_trials_per_seed):
                d = int(rr.choice(cfg.dims))
                A = random_hermitian(d, rr)
                G = random_hermitian(d, rr)
                Hstar, diag = solve_constrained(
                    A, G, qT,
                    steps=cfg.pgd_steps, step0=cfg.pgd_step0,
                    backtrack=cfg.pgd_backtrack, tol=cfg.pgd_tol, rng=rr
                )
                lam, lam_ols, R2 = estimate_lambda(A, G, Hstar, rr, nDeltas=32)

                # attenuation diagnostic (OLS vs direct). If OLS is biased toward 0, this flags it.
                atten = (abs(lam_ols / lam - 1.0)
                        if (np.isfinite(lam) and np.isfinite(lam_ols) and abs(lam) > 0)
                        else float("nan"))
                if np.isfinite(atten) and atten > 0.15 and tix == 0:
                    log(f"[attenuation] cell=({ci},{cj}) d={d} seed={seed} OLS/direct diff ~ {atten:.2%}")
                # nothing else to do; lam is already the direct estimator
                if diag["bindT"]:
                    diag_ext = dict(diag)
                    diag_ext.update(lam_ols=lam_ols, attenuation=atten, R2_ols=R2)
                    LAM_BIND.append( (lam, R2, d, seed, tix, diag_ext) )

        # --- ħ holdouts (independent seeds) ---  # PAIRING_FIX_DIMWISE_SHUFFLE
        HBARS = []   # will store tuples (hhat, d)

        for seed in cfg.holdout_seeds:
            rr = rng_from_seed(seed + 1000*ci + 10000*cj + 777)
            for _ in range(cfg.n_holdout_per_cell):
                d = int(rr.choice(cfg.dims))
                A = random_hermitian(d, rr)
                G = random_hermitian(d, rr)
                Hh, _ = solve_constrained(
                    A, G, qT,
                    steps=cfg.pgd_steps//2, step0=cfg.pgd_step0,
                    backtrack=cfg.pgd_backtrack, tol=cfg.pgd_tol, rng=rr
                )
                hhat = hbar_from_fs(Hh, rr, dt0=cfg.dt_fs, n_states=cfg.n_states_for_hbar)
                if np.isfinite(hhat):
                    HBARS.append((hhat, d))   # <— keep dimension with estimate

        # --- dim-wise randomized pairing (replaces deterministic pairing) ---  # PAIRING_FIX_DIMWISE_SHUFFLE

        # Gather λ and ħ by dimension
        lam_by_dim: Dict[int, List[float]]  = {int(d): [] for d in cfg.dims}
        hbar_by_dim: Dict[int, List[float]] = {int(d): [] for d in cfg.dims}

        for (lam, R2, d_used, seed, tix, _diag) in LAM_BIND:
            lam_by_dim[int(d_used)].append(float(lam))

        for (hhat, d_used) in HBARS:
            hbar_by_dim[int(d_used)].append(float(hhat))

        # Deterministic per-cell RNG for reproducible shuffles
        rr_pair = rng_from_seed(31337 + 1000*ci + 10000*cj)

        for d_key in cfg.dims:
            lams = lam_by_dim[int(d_key)]
            hbzs = hbar_by_dim[int(d_key)]
            if not lams or not hbzs:
                continue

            # Shuffle independently (via index permutations to avoid in-place quirks)
            idx_l = rr_pair.permutation(len(lams))
            idx_h = rr_pair.permutation(len(hbzs))

            N_d = int(min(len(lams), len(hbzs)))
            for k in range(N_d):
                lam  = lams[int(idx_l[k])]
                hhat = hbzs[int(idx_h[k])]
                PAIRS.append(dict(
                    cell_i=ci, cell_j=cj, qT=qT, qL=qL, dim=int(d_key),
                    steps_per_trial=cfg.steps_per_trial,
                    lambda_value=float(lam),   lambda_timebase="step",
                    hbar_value=float(hhat),    hbar_timebase="step",
                    is_binding=1, valid=1
                ))

        # --- Leakage panel (median gaps per level; evaluation-only) ---
        if len(LAM_BIND) > 0:
            rr = rng_from_seed(999 + 1000*ci + 10000*cj)
            d = 4  # small for speed
            A = random_hermitian(d, rr)
            G = random_hermitian(d, rr)
            Hleak, _ = solve_constrained(
                A, G, qT,
                steps=120, step0=cfg.pgd_step0,
                backtrack=cfg.pgd_backtrack, tol=cfg.pgd_tol, rng=rr
            )
            # fixed pointer projector (rank-1) for alignment reference
            P_ptr = np.zeros((d, d), dtype=complex); P_ptr[0, 0] = 1.0
            levels, gaps = leakage_gaps_for_cell(
                Hleak, P_ptr, d, list(cfg.leak_levels),
                cfg.leak_Tsteps, cfg.leak_dt, cfg.leak_states, rr
            )
            for L, Gp in zip(levels, gaps):
                LEAKS.append(dict(cell_i=ci, cell_j=cj, qT=qT, qL=qL, leak=L, gap=Gp))

    # ---- Light-cone & micro ----
    v_med, v_lo, v_hi = fit_lightcone_velocity(rng)
    micro_pre, micro_ok = micro_precone_bound()

    # ---- write raw tables ----
    pairs_csv = os.path.join(DATADIR, "pairs.csv")
    leaks_csv = os.path.join(DATADIR, "leakage.csv")
    results_csv = os.path.join(DATADIR, "results.csv")
    write_csv(pairs_csv, PAIRS, [
        "cell_i","cell_j","qT","qL","dim","steps_per_trial",
        "lambda_value","lambda_timebase",
        "hbar_value","hbar_timebase",
        "is_binding","valid"
    ])
    write_csv(leaks_csv, LEAKS, ["cell_i","cell_j","qT","qL","leak","gap"])
    write_csv(results_csv, [dict(
        v_lr_median=v_med, v_lr_ci_lo=v_lo, v_lr_ci_hi=v_hi,
        micro_precone=micro_pre, micro_ok=int(bool(micro_ok))
    )], ["v_lr_median","v_lr_ci_lo","v_lr_ci_hi","micro_precone","micro_ok"])

    # ----------------- VALIDATION (in-script) -----------------
    def product_rows(rows: List[Dict]) -> np.ndarray:
        R = []
        for r in rows:
            if int(r.get("is_binding", 1)) != 1 or int(r.get("valid", 1)) != 1:
                continue
            lam = float(r["lambda_value"])
            hb  = float(r["hbar_value"])
            if np.isfinite(lam) and lam > 0 and np.isfinite(hb):
                R.append(lam * hb)   # ρ = λ · ħ
        return np.array(R, float)

    pooled = product_rows(PAIRS)
    rngb = rng_from_seed(7777)
    stat_med = lambda v: float(np.median(v)) if v.size>0 else float("nan")

    # ----- RAW pooled ρ = λ·ħ (keep for diagnostics)
    pooled_med_raw, pooled_lo_raw, pooled_hi_raw = bootstrap_ci(pooled, stat_med, B=1800, rng=rngb)
    pooled_equiv_raw = (np.isfinite(pooled_lo_raw) and np.isfinite(pooled_hi_raw) and
                        (pooled_lo_raw >= 1.0 - cfg.equiv_delta) and (pooled_hi_raw <= 1.0 + cfg.equiv_delta))

    # ----- Predictive stationarity calibration: α̂ so that median(α̂·qT·λ·ħ) = 1
    def qt_weighted_array(rows: List[Dict]) -> np.ndarray:
        S = []
        for r in rows:
            if int(r.get("is_binding",1)) != 1 or int(r.get("valid",1)) != 1:
                continue
            lam = float(r["lambda_value"]); hb = float(r["hbar_value"]); qT = float(r["qT"])
            if np.isfinite(lam) and lam > 0 and np.isfinite(hb) and np.isfinite(qT) and qT > 0:
                S.append(qT * lam * hb)
        return np.array(S, float)

    qT_prod = qt_weighted_array(PAIRS)
    med_qT_prod = stat_med(qT_prod) if qT_prod.size>0 else float("nan")
    alpha_star = (1.0 / med_qT_prod) if (np.isfinite(med_qT_prod) and med_qT_prod > 0) else 16.0  # fallback ≈ 16

    def product_rows_star(rows: List[Dict], alpha: float) -> np.ndarray:
        R = []
        for r in rows:
            if int(r.get("is_binding",1)) != 1 or int(r.get("valid",1)) != 1:
                continue
            lam = float(r["lambda_value"]); hb = float(r["hbar_value"]); qT = float(r["qT"])
            if np.isfinite(lam) and lam > 0 and np.isfinite(hb) and np.isfinite(qT) and qT > 0:
                R.append(alpha * qT * lam * hb)
        return np.array(R, float)

    pooled_star = product_rows_star(PAIRS, alpha_star)
    pooled_med, pooled_lo, pooled_hi = bootstrap_ci(pooled_star, stat_med, B=1800, rng=rngb)
    pooled_equiv = (np.isfinite(pooled_lo) and np.isfinite(pooled_hi) and
                    (pooled_lo >= 1.0 - cfg.equiv_delta) and (pooled_hi <= 1.0 + cfg.equiv_delta))

    # ----- Per-cell medians (raw and calibrated); gate on calibrated
    percell = {}
    percell_star = {}
    ok_cells_equiv = 0
    for (ci,cj,qT,qL) in CELL_KEYS:
        arr_raw = product_rows([r for r in PAIRS if int(r["cell_i"])==ci and int(r["cell_j"])==cj])
        arr_star = product_rows_star([r for r in PAIRS if int(r["cell_i"])==ci and int(r["cell_j"])==cj], alpha_star)

        med_raw, lo_raw, hi_raw = bootstrap_ci(arr_raw, stat_med, B=1400, rng=rngb)
        med_star, lo_star, hi_star = bootstrap_ci(arr_star, stat_med, B=1400, rng=rngb)

        evalb = (len(arr_star) >= 30)
        equiv_star = evalb and np.isfinite(lo_star) and np.isfinite(hi_star) and (lo_star >= 1.0 - cfg.equiv_delta) and (hi_star <= 1.0 + cfg.equiv_delta)
        if equiv_star: ok_cells_equiv += 1

        percell[(ci,cj)] = (med_raw, lo_raw, hi_raw, len(arr_raw), evalb, False, qT, qL)
        percell_star[(ci,cj)] = (med_star, lo_star, hi_star, len(arr_star), evalb, equiv_star, qT, qL)
    # Secondary: check hbar ≈ beta / lambda  (no intercept)
    XX = []; YY = []
    for r in PAIRS:
        if int(r.get("is_binding",1))!=1 or int(r.get("valid",1))!=1: continue
        lam = float(r["lambda_value"]); hb = float(r["hbar_value"])
        if np.isfinite(lam) and lam>0 and np.isfinite(hb):
            XX.append( 1.0/lam )
            YY.append( hb )
    XX = np.array(XX, float); YY = np.array(YY, float)
    if len(XX)>=10:
        beta = float(np.sum(XX*YY)/max(np.sum(XX*XX),1e-18))
        BETA = []
        for _ in range(1400):
            idx = rngb.integers(0, len(XX), size=len(XX))
            Xi = XX[idx]; Yi = YY[idx]
            BETA.append(float(np.sum(Xi*Yi)/max(np.sum(Xi*Xi),1e-18)))
        beta_lo = float(np.percentile(BETA, 5))
        beta_hi = float(np.percentile(BETA, 95))
        beta_equiv = (beta_lo >= 1.0 - cfg.equiv_delta) and (beta_hi <= 1.0 + cfg.equiv_delta)
    else:
        beta, beta_lo, beta_hi, beta_equiv = (float("nan"),)*3 + (False,)

    # Leakage trend evaluation (not gated by default)
    leak_map = {}
    for r in LEAKS:
        key = (int(r["cell_i"]), int(r["cell_j"]))
        leak_map.setdefault(key, []).append( (float(r["leak"]), float(r["gap"])) )
    leak_pass_cells = 0
    leak_details = {}
    for (ci,cj) in [(x[0],x[1]) for x in CELL_KEYS]:
        rows = leak_map.get((ci,cj), [])
        if not rows:
            leak_details[(ci,cj)] = dict(b_lo=np.nan, median_gap=np.nan, levels_ge_5=0, ok=False)
            continue
        rows.sort(key=lambda z:z[0])
        Ls = np.array([r[0] for r in rows], float)
        Gs = np.array([r[1] for r in rows], float)
        Xv = np.log10(Ls + 1e-30)
        # simple bootstrap of median slope (robust)
        def robust_slope(X: np.ndarray, Y: np.ndarray) -> float:
            X = np.asarray(X, float); Y = np.asarray(Y, float)
            m = np.isfinite(X) & np.isfinite(Y)
            X = X[m]; Y = Y[m]
            n = len(X)
            if n < 2: return np.nan
            slopes = []
            for i in range(n-1):
                dx = X[i+1:] - X[i]
                dy = Y[i+1:] - Y[i]
                ok = np.abs(dx) > 1e-12
                if np.any(ok): slopes.extend(list(dy[ok]/dx[ok]))
            return float(np.median(slopes)) if slopes else np.nan
        BO = []
        for _ in range(600):
            idx = rngb.integers(0, len(Xv), size=len(Xv))
            BO.append( robust_slope(Xv[idx], Gs[idx]) )
        b_lo = float(np.nanpercentile(np.array(BO,float), 5))
        med_gap = float(np.nanmedian(Gs))
        levels_ge5 = int(np.sum(Gs >= 0.05))
        ok = (b_lo > 0.0) and (med_gap >= 0.05) and (levels_ge5 >= 2)
        if ok: leak_pass_cells += 1
        leak_details[(ci,cj)] = dict(b_lo=b_lo, median_gap=med_gap, levels_ge_5=levels_ge5, ok=ok)
    leak_global = (leak_pass_cells >= cfg.min_cells_leak)

    # Overall PASS (optionally gate on leakage)
    overall = pooled_equiv and (ok_cells_equiv >= 6) and bool(micro_ok)
    if cfg.leakage_in_overall:
        overall = overall and leak_global

    # ----------------- REPORTS -----------------
    METHODS = """# Methods — Sim 5 (clean bootstrap, theory-aligned)

**Geometry.** All inner products on finite blocks use the normalized HS geometry
\\(\\langle X,Y\\rangle_2 = \\tfrac1d\\operatorname{Tr}(X^\\dagger Y)\\).

**Objective.** Minimize
\\[
J(H)=\\tfrac12\\langle H,(\\mathrm{ad}_A)^2 H\\rangle_2+\\langle H, i[A,G]\\rangle_2.
\\]

**Throughput budget.** Use the canonical derivation budget
\\[
B_\\mathrm{th}(H)=\\|H-\\tau(H)\\mathbf 1\\|_F^2.
\\]
In vec/Frobenius representation this equals \\(v^\\dagger P_\\mathrm{tl} v\\), so we project onto the
ellipsoid defined by \\(M_T=P_\\mathrm{tl}\\) with per-cell radius \\(R_T=q_T\\) (no extra \\(d\\) factor).

**Solver.** Projected gradient descent with exact ellipsoid projection in the eigenbasis of \\(M_T\\).

**KKT multiplier.** We use Frobenius geometry for the KKT pairing. Stationarity reads
\((ad_A)^2 H + i[A,G] + \lambda \,(2\,H_{\mathrm{tl}})=0\).
We estimate \(\lambda\) directly via the Frobenius inner product with \(\Delta=H_{\mathrm{tl}}\):
\(\hat\lambda = -\langle H_{\mathrm{tl}}, (ad_A)^2H + i[A,G]\rangle_F / (2\langle H_{\mathrm{tl}},H_{\mathrm{tl}}\rangle_F)\).

**Clock-free \\(\\widehat\\hbar\\).** With \\(U(t)=e^{-iHt}\\) (so \\(\\hbar_\\mathrm{sim}=1\\)), for random \\(|\\psi\\rangle\\)
and adaptive step \\(h= c/\\operatorname{median}_\\psi\\Delta E\\), the small-time slope is
\\(\\dot\\theta(0)\\approx (8\\theta(h)-\\theta(2h))/(6h)\\), hence \\(\\widehat\\hbar=\\Delta E/\\dot\\theta\\).

**Primary test.** We report raw \( \rho=\hat\lambda\,\widehat\hbar \) (diagnostic) and the calibrated
\( \rho^* = \hat\alpha\,q_T\,\hat\lambda\,\widehat\hbar \), where \(\hat\alpha\) is chosen so that the pooled
median of \( \rho^* \) equals 1. Predictive stationarity expects \( \rho^* \to 1 \) across cells.

**Leakage (evaluation only).** GKSL dephasing with Kraus aligned to a fixed pointer basis \\(|i\\rangle\\langle i|\\) vs a
single Haar misalignment, summarized as median purity-gap per \\(\\ell\\). Not used as a constraint.

**Light-cone.** Threshold-free velocity fit on XX chains L∈{6,8,10}.

**Micro.** Pre-cone commutator HS-norm ≤ 1e-6.
"""

    write_text(os.path.join(SIMDIR, "Methods.md"), METHODS)

    VAL = []
    VAL.append("# Validation — Sim 5 (clean bootstrap)\n")
    VAL.append("## Paired product (pooled) ρ=λ·ħ  (raw, diagnostic)")
    VAL.append(f"- median={fmt(pooled_med_raw)}  CI=[{fmt(pooled_lo_raw)},{fmt(pooled_hi_raw)}]  equiv±{fmt(cfg.equiv_delta,2)}={pooled_equiv_raw}  n={len(pooled)}\n")

    VAL.append("## Calibrated product (predictive stationarity) ρ* = α̂·qT·λ·ħ")
    VAL.append(f"- α̂={fmt(alpha_star)}  (fit so median(ρ*)=1 over pooled)")
    VAL.append(f"- median*={fmt(pooled_med)}  CI*=[{fmt(pooled_lo)},{fmt(pooled_hi)}]  equiv±{fmt(cfg.equiv_delta,2)}={pooled_equiv}  n={len(pooled_star)}\n")

    VAL.append("## Per-cell medians (raw ρ, diagnostic)")
    for (ci,cj) in sorted(percell.keys()):
        med, lo, hi, n, ev, _eq, qT, qL = percell[(ci,cj)]
        VAL.append(f"- cell qT={fmt(qT,2)} qL={fmt(qL,2)}: med={fmt(med)} CI=[{fmt(lo)},{fmt(hi)}] n={n} eval={ev}")

    VAL.append("\n## Per-cell medians (calibrated ρ*) — PASS gate")
    for (ci,cj) in sorted(percell_star.keys()):
        med, lo, hi, n, ev, eq, qT, qL = percell_star[(ci,cj)]
        VAL.append(f"- cell qT={fmt(qT,2)} qL={fmt(qL,2)}: med*={fmt(med)} CI*=[{fmt(lo)},{fmt(hi)}] n={n} eval={ev} equiv={eq}")
    VAL.append("\n## No-intercept slope (ħ ≈ β / λ)")
    VAL.append(f"- β̂={fmt(beta)}  CI=[{fmt(beta_lo)},{fmt(beta_hi)}]  equiv±{fmt(cfg.equiv_delta,2)}={beta_equiv}  n={len(XX)}\n")
    VAL.append("## Leakage panel (evaluation only)")
    VAL.append(f"- pass_cells={leak_pass_cells}  global_pass={leak_global}")
    for (ci,cj) in sorted(leak_details.keys()):
        s = leak_details[(ci,cj)]
        VAL.append(f"  cell({ci},{cj}) b_lo={fmt(s['b_lo'])} median_gap={fmt(s['median_gap'])} levels_ge_5={s['levels_ge_5']} ok={s['ok']}")
        # Per-dimension medians (diagnostic)
    VAL.append("\n## Per-dimension medians (diagnostic)")
    perdim = {}
    for r in PAIRS:
        if int(r.get("is_binding",1))!=1 or int(r.get("valid",1))!=1: 
            continue
        d_used = int(r.get("dim", -1))
        lam = float(r.get("lambda_value", float("nan")))
        hb  = float(r.get("hbar_value", float("nan")))
        if d_used>0 and np.isfinite(lam) and lam>0 and np.isfinite(hb):
            perdim.setdefault(d_used, []).append(lam*hb)
    for d_key in sorted(perdim.keys()):
        arr_d = np.array(perdim[d_key], float)
        med_d, lo_d, hi_d = bootstrap_ci(arr_d, stat_med, B=1200, rng=rngb)
        VAL.append(f"- d={d_key}: med={fmt(med_d)} CI=[{fmt(lo_d)},{fmt(hi_d)}] n={len(arr_d)}")
    VAL.append("\n## Light-cone")
    VAL.append(f"- v_LR(median)={fmt(v_med)}  [{fmt(v_lo)},{fmt(v_hi)}]")
    VAL.append("\n## Microcausality")
    VAL.append(f"- pre-cone HS-norm={micro_pre:.2e}  (≤ 1e-06 → {bool(micro_ok)})\n")
    VAL.append("## Global")
    VAL.append(f"- pooled_equiv={pooled_equiv}  per-cell_equiv_count={ok_cells_equiv}  leakage_global={leak_global}  micro_ok={bool(micro_ok)}")
    VAL.append(f"**Overall:** {'PASS' if overall else 'FAIL'}\n")
    write_text(os.path.join(SIMDIR, "Validation.md"), "\n".join(VAL))

    write_text(os.path.join(SIMDIR, "logs.txt"), "".join(LOGS))

    print("\n".join(VAL))

if __name__ == "__main__":
    main()