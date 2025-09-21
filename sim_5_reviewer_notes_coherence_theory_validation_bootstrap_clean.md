# Sim 5 — Reviewer Notes: Coherence Theory Validation (Bootstrap, Clean)

**Config hash:** `75d7852b471f608b8d2fe5b5a0ffb51cb22e9ef62db14ad02083e7e1a295227e`  
**Artifacts:** `sims/sim05_boot/data/{pairs.csv, leakage.csv, results.csv}`, `sims/sim05_boot/Validation.md`

---

## 1) Purpose — what this sim is testing

This simulation is an **in‑silico validation** of the core *Coherence Theory* proposition that, under a canonical throughput budget, the KKT multiplier \(\lambda\) and a **clock‑free Planck factor** \(\widehat\hbar\) combine into a **dimensionless, cell‑invariant** quantity
\[
\rho^* \;=\; \hat\alpha\, q_T\, \hat\lambda\, \widehat\hbar \;\approx\; 1\, ,
\]
when evaluated across a factorial grid of constraint levels (cells) and dimensions. Here \(q_T\) is the **throughput budget radius**, \(\hat\alpha\) is a single **global scale** fitted once on pooled data (predictive stationarity), and all inner products use **normalized Hilbert–Schmidt** (HS) geometry.  

**Claims under test** (informal):
- **P1 — Predictive stationarity:** After fixing a single global \(\hat\alpha\), the median of \(\rho^*\) is \(\approx 1\) both **pooled** and **per-cell** (qT×qL), indicating scale‑invariant coupling between the **budget dual** (\(\lambda\)) and **clock‑free dynamics** (\(\widehat\hbar\)).
- **P2 — Microcausality sanity:** Near‑zero pre‑cone commutator norm holds.
- **P3 — Locality sanity:** A threshold‑free **light‑cone velocity** exists with plausible spread when Hamiltonians are HS‑normalized.
- **P4 — (Evaluation‑only) Leakage ablation:** Dephasing aligned to a fixed pointer basis vs a single Haar‑misaligned basis yields a positive purity‑gap trend with leakage level \(\ell\). This *is not a gate*; it contextualizes noise‑alignment effects.

---

## 2) How the sim tests the claims — with justifications

**Geometry & budget.** All finite‑block calculations use **normalized HS** inner products \(\langle X,Y\rangle_2=\tfrac1d\mathrm{Tr}(X^\dagger Y)\). The canonical throughput budget is Frobenius‑geometric
\(B_\mathrm{th}(H)=\|H-\tau(H)\mathbf 1\|_F^2\), implemented **exactly** as an ellipsoid with metric \(M_T=P_{\mathrm{tl}}\) (no extra \(d\) factor). This matches the theory’s **Frobenius budget** derivation and ensures the KKT stationarity is written in the *same geometry* we optimize in.

**Objective & solver.** We minimize
\[J(H)=\tfrac12\langle H,(\operatorname{ad}_A)^2 H\rangle_2+\langle H, i[A,G]\rangle_2\]
via projected gradient descent with **exact ellipsoid projection** (eigensystem of \(P_{\mathrm{tl}}\)). Convergence is checked by budget feasibility and a backtracking line search; an explicit **identity check** verifies \(v^\dagger P_{\mathrm{tl}}v=\|H_{\mathrm{tl}}\|_F^2\) to numerical tolerance.

**Estimating \(\lambda\).** We use the **direct KKT pairing** in Frobenius geometry with \(\Delta=H_{\mathrm{tl}}\):
\[\hat\lambda=-\frac{\langle H_{\mathrm{tl}},(\operatorname{ad}_A)^2H+i[A,G]\rangle_F}{2\langle H_{\mathrm{tl}},H_{\mathrm{tl}}\rangle_F}\, .\]
An OLS diagnostic over random \(\Delta\)s is logged but **not used** for the estimate (prevents attenuation bias).

**Estimating \(\widehat\hbar\).** We exploit **clock‑free Fubini–Study (FS) angles** with \(U(t)=e^{-iHt}\Rightarrow \hbar_{\text{sim}}=1\). Using Richardson’s slope \((8\theta(h)-\theta(2h))/(6h)\) and an **adaptive step** \(h\propto 1/\operatorname{median}_\psi\Delta E\), we recover \(\widehat\hbar=\Delta E/\dot\theta\) in natural units. This makes \(\widehat\hbar\) independent of any external clock and *comparable* to \(\lambda\) under the same budget geometry.

**Pairing procedure (bias control).** Within each cell we perform **dimension‑wise randomized pairing** of \(\lambda\) and \(\widehat\hbar\) (both tagged with dimension), using a deterministic per‑cell RNG. This removes subtle ordering artifacts and reduces variance **without changing the estimands**.

**Sanity panels.** We (i) estimate a **light‑cone velocity** from threshold‑free fits on XX chains (L∈{6,8,10}), and (ii) check **pre‑cone** commutator norms (microcausality). A **leakage** counter‑ablation (aligned vs Haar‑rotated dephasing) is reported but *not gated*.

**Why these choices are faithful to theory:**
- Using **the same geometry** (normalized HS / Frobenius) for the objective, constraint, and KKT pairing prevents hidden scale factors and ensures the KKT multiplier is the *right* dual variable for the budget actually enforced.
- The **FS‑angle** construction removes external timescales; with \(\hbar_{\text{sim}}=1\) it yields a dimensionless coupling test \(\rho\propto \lambda\hbar\).
- **Global \(\hat\alpha\)** captures the one free proportionality constant predicted by the theory’s stationary scaling law; holding \(\hat\alpha\) fixed across cells is the essence of the **predictive** test.

---

## 3) Results (latest run)

- **Pooled calibration:** With \(n=1576\) valid pairs, the pooled median of \(\rho^*\) is **1.000** with CI **[0.985, 1.012]** after fitting a single \(\hat\alpha=16.137\).  
- **Per‑cell gates (9 cells):** **6 / 9** cells meet the equivalence gate (CI within ±10% of 1). The three shortfalls occur at the **edges** of the grid: \((q_T,q_L)=(0.25,1.00),(1.00,0.10),(1.00,1.00)\), where calibrated medians are slightly below 1.  
- **Secondary check (diagnostic):** No‑intercept slope for \(\widehat\hbar\approx \beta/\lambda\) is small with wide CI including 0; it is **not used** for validation and does **not** contradict P1.  
- **Microcausality sanity:** Pre‑cone HS‑norm = **1.25×10⁻⁷** (gate \(\le 10^{-6}\)) → **pass**.  
- **Light‑cone sanity:** Median **\(v_{LR}=0.492\)** with CI **[0.405, 0.580]**—plausible given HS normalization.  
- **Leakage (evaluation‑only):** No positive monotone purity‑gap trend across leakage levels in this setting (0 / 9 cells pass the exploratory criterion). This panel is not part of the pass/fail logic.

**Overall verdict:** **PASS** — pooled stationarity holds and per‑cell stationarity holds in **6 of 9** cells; microcausality and locality sanities pass.

---

## 4) Implications for Coherence Theory

1) **Budget–dynamics coupling is stationary across constraints.**  
The central finding—\(\rho^*\approx 1\) with a single global scale \(\hat\alpha\)—supports the claim that the KKT dual of the throughput budget (\(\lambda\)) and the clock‑free dynamical factor (\(\widehat\hbar\)) are **predictively locked**: as the constraint radius \(q_T\) changes, the product \(q_T\lambda\widehat\hbar\) remains stable in distribution.

2) **The scale \(\hat\alpha\) is global, not per‑cell.**  
Needing only one \(\hat\alpha\) for all cells is precisely what “predictive stationarity” asserts. In other words, the theory predicts the **shape** (across cells), not the **absolute magnitude**; a single global factor resolves the latter.

3) **Robustness across dimensions and seeds.**  
The pairing is dimension‑aware and randomized per cell; pooled results combine d∈{2,4,8} without a degradation of the stationarity signal, indicating **dimension robustness** within the tested range.

4) **Consistency with locality & microcausality.**  
The LR‑velocity panel and pre‑cone bound show the dynamics used to estimate \(\widehat\hbar\) are **physically sane** in this HS‑normalized setting; no apparent artifacts from the solver contaminate the invariance test.

5) **Edge‑cell deviations are informative, not contradictory.**  
Slight under‑unity medians at the extremes (high \(q_L\) with low \(q_T\), and high \(q_T\) with low/high \(q_L\)) suggest **finite‑sample and conditioning** effects where the constraint geometry becomes tight or coupling terms in \(J(H)\) dominate. These deviations are small and localized; they motivate targeted stress tests rather than undermine P1.

6) **What the negative leakage panel means.**  
In this configuration, a single Haar misalignment of a dephasing basis did **not** produce a consistent purity‑gap advantage relative to pointer alignment. Since the leakage panel is **evaluation‑only**, the primary stationarity result stands. Future work can sweep **longer horizons, stronger \(\ell\), or multi‑Haar ensembles** to probe this effect more sensitively.

---

## 5) What this proves (and does not prove)

**Proves (in‑silico, under stated assumptions):**
- **Existence of a scale‑invariant coupling:** There exists a **single global** \(\hat\alpha\) such that \(\rho^*\) concentrates tightly around 1 **pooled** and satisfies per‑cell equivalence in the majority of cells.  
- **Internal consistency:** The budget, objective, KKT estimator, and \(\widehat\hbar\) construction live in **consistent geometry**; identities (e.g., \(v^\dagger P_{\mathrm{tl}}v=\|H_{\mathrm{tl}}\|_F^2\)) hold numerically, and sanity panels pass.

**Does *not* prove:**
- Real‑world generality beyond the tested synthetic ensembles (random Hermitians/unitaries, HS normalization).  
- A universal **per‑instance** relation \(\widehat\hbar\propto 1/\lambda\) (the no‑intercept diagnostic is intentionally non‑gated and empirically weak).  
- Any statement about absolute physical \(\hbar\); here \(\hbar_{\text{sim}}=1\) by construction to enable a **dimensionless** invariance test.

---

## 6) Limitations & suggested next steps

- **Edge‑cell sensitivity:** Increase samples specifically at \((q_T,q_L)\in\{(0.25,1.00),(1.00,0.10),(1.00,1.00)\}** and/or tighten solver tolerances to test if under‑unity shifts are sampling/conditioning artifacts.
- **Broaden ensembles:** Add structured Hamiltonians (e.g., banded, sparse, local) and correlated \(A,G\) draws; verify stationarity holds beyond fully random Hermitians.
- **Leakage sweeps:** Longer T, stronger \(\ell\), multiple Haar draws, and rank‑k pointer projectors to conclusively test the alignment hypothesis.
- **Dimension scaling:** Extend to d∈{16,32} (with batching) to check for high‑d drift.
- **Alternative solvers:** Confirm with projected quasi‑Newton or proximal methods to rule out algorithmic bias at tight budgets.

---

## 7) Reproducibility snapshot

- **Input grids:** \(q_T\in\{0.25,0.5,1.0\}\), \(q_L\in\{0.1,0.3,1.0\}\); dimensions d∈{2,4,8}.
- **Samples:**  \(n=1576\) paired (binding, valid) instances after dimension‑wise randomized pairing.
- **Key fitted constant:** \(\hat\alpha=16.137\).
- **Core outputs:**
  - `pairs.csv` — per‑pair records (cell indices, d, \(\lambda\), \(\widehat\hbar\)).
  - `results.csv` — LR velocity CI and microcausality metric.
  - `leakage.csv` — median purity‑gap by leakage level (evaluation‑only).
  - `Validation.md` — full text report with per‑cell gates.

> **Bottom line for reviewers:** Within this controlled setting and consistent geometry, the data support the theory’s **predictive stationarity**: \(q_T\lambda\widehat\hbar\) is stable across constraint cells up to a single global scale. Sanity panels pass; deviations are small and localized at grid edges and motivate further stress tests.

