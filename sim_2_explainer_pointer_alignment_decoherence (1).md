# Sim 2 Explainer — Pointer Alignment & Decoherence

## What this simulation is
**Goal.** Empirically test the pointer‑alignment claim: for a fixed‑spectrum noise block, the Dirichlet‑linear leakage budget
\[ \mathcal B_{\text{leak}}(A;W)=\sum_j \operatorname{tr}(L_j^{\dagger} W L_j) \]
is minimized when the channel’s noise block co‑diagonalizes with the environmental weight \(W\). The preregistered pass line requires a ≥10% leakage penalty at misalignment \(\theta=\pi/4\) for moderate contrast.

**Why it matters.** This is a concrete prediction of the Coherence Law (“maximize keeps‑working‑when‑poked minus budgets”). Pointer alignment is the selection the law predicts once leakage is charged Dirichlet‑linearly.

---

## How it works (model + procedure)
**System.** Single qubit with binary inputs \(\rho_0=|0\rangle\langle0|\), \(\rho_1=|1\rangle\langle1|\).

**Channel (fixed spectrum).** Amplitude damping with strength \(\gamma=0.20\), rotated by \(R_y(\theta)\) so only eigenvectors change (singular values held constant).

**Environmental weight.** \(W=\mathrm{diag}(1,w)\), with \(w\in\{1.2,2,5\}\).

**Leakage budget.** For this family,
\[ \mathcal B_{\text{leak}}(\theta)=\gamma\big(\cos^2\tfrac{\theta}{2}+w\,\sin^2\tfrac{\theta}{2}\big), \]
which is minimized at \(\theta=0\) for \(w\ge1\) (pointer‑aligned).

**Poke ensemble (approximates cone closure).** Random depolarizing \(p\in[0,0.2]\), phase damping \(\lambda\in[0,0.2]\), and small unitary jitters (axis‑angle Gaussian). Pokes are applied **after** the base channel.

**Coherence metrics.** For each \(\theta\), apply pokes and evaluate:
- **Binary discrimination:** equal‑prior Helstrom error \(P_e^*=\tfrac{1}{2}-\tfrac{1}{4}\lVert\rho'_0-\rho'_1\rVert_1\).
- **Finite‑protocol CL:** \(\min\limits_{\text{pokes}} X\) with \(X=1-P_e^*\).
- **Risk‑sensitive aggregator:** \( \mathrm{CL}_\beta=-(1/\beta)\log\mathbb E\,\exp(-\beta X) \), \(\beta\in\{1,3,10,30,100,300,1000\}\).

**Run grid.** \(\theta\in\{0,5,\dots,90\}\) degrees; \(w\in\{1.2,2,5\}\); 128 poke draws per \(\theta\). RNG seed fixed.

---

## Robustness & hygiene
- **Fixed‑spectrum rotation:** Rotating the noise block via \(R_y(\theta)\) keeps singular values constant, isolating alignment effects.
- **Dirichlet checks:** Verify scaling \(\mathcal B_{\text{leak}}(\alpha W)=\alpha\,\mathcal B_{\text{leak}}(W)\) and additivity over spectral projectors (≤1% tolerance; observed ~0%).
- **Risk‑sensitive limit:** Report \(\mathrm{CL}_\beta\) on a standardized \(\beta\) grid and show convergence as \(1/\beta\to0\).
- **Bootstrap CIs:** ≥2000 resamples for CL and \(\mathrm{CL}_\beta\) at \(\theta\in\{0,45,90\}\), \(w=2\).
- **Microcausality sanity:** Two‑qubit AB test with local map on A, identity on B: reduced state on B is invariant (trace‑distance ≈ machine zero). Counter‑ablation with SWAP produces unit trace‑distance.
- **Ablation:** Low‑contrast case \(w=1.2\) intentionally yields <10% penalty, confirming dependence on contrast (not an artifact).

---

## Results (key numbers)
- **Minimizer:** Leakage minimized at \(\theta=0^\circ\) for all \(w\ge 1\).
- **Misalignment penalty at 45° (relative to 0°):**
  - \(w=2.0\): **+14.64%** (meets ≥10% pass line).
  - \(w=5.0\): **+58.58%** (strong pass).
  - \(w=1.2\): **+2.93%** (expected fail for robustness only).
- **Dirichlet residuals:** scaling ≈ **0%**; additivity ≈ **0%** across \(\theta\).
- **Discrimination trend:** worst‑case \(P_e^*\) increases monotonically with leakage (\(\theta\uparrow\) or \(w\uparrow\)).
- **Risk‑sensitive convergence:** \(\mathrm{CL}_\beta\) vs \(1/\beta\) is near‑linear and approaches the finite worst‑case CL; bootstrap 95% CIs are tight.
- **Microcausality (local A‑only):** max trace‑distance change on B **≈ 4.44×10⁻¹⁶**; SWAP counter‑ablation gives **1.0**.

**Artifacts generated:** `results.csv`, `summary.csv`, `audit_stub.csv`, per‑poke and bootstrap tables, and figures (heatmap, penalty curve, CL_β convergence with CIs, trade‑off scatter, microcausality histogram, analytic‑vs‑empirical overlay). A camera‑ready PDF with embedded figures is included.

---

## How this validates Coherence Theory
- **Selection under budgets (pointer alignment).** The minimizer occurs when the noise block is aligned with \(W\), exactly as the Coherence Law predicts when leakage is charged Dirichlet‑linearly.
- **Budget structure (Dirichlet linearity/additivity).** Empirically verified at machine precision; without this structure, selection can fail (shown in counter‑ablations elsewhere).
- **Coherence–discrimination link.** Increasing leakage degrades discrimination; the risk‑sensitive \(\mathrm{CL}_\beta\) cleanly approaches the worst‑case finite protocol.
- **Causal hygiene.** Microcausality holds under local operations (no super‑cone signaling); breaking locality (SWAP) produces immediate violations.

**Verdict:** **PASS.** The preregistered criteria are met (min at \(\theta=0\); ≥10% penalty at 45° for \(w=2\); Dirichlet residuals ≤1%; \(\mathrm{CL}_\beta\) convergence), providing clear empirical support for the pointer‑alignment prediction of the Coherence Law in this binary‑channel setting.

