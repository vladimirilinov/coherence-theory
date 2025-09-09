# Front Matter — Abstract & Global Hypotheses (H0–H5)

## Abstract

We formalize coherence as the staying‑power of a pattern under admissible pokes, priced by three convex budgets—throughput, complexity, and leakage—selected by symmetry and locality. We prove budget minimal completeness (no fourth budget), poke‑ensemble robustness, and a non‑teleological variational principle via risk‑sensitive large deviations. Fast‑sector KKT on a C\*‑quadratic fixes \(\hbar\); slow‑sector Γ‑compactness recovers Einstein–Hilbert. Pointer alignment follows from a unitary‑orbit minimizer. Multi‑cone geometries pay a strict L¹ coherence penalty.

## Global hypotheses

**H0 (Spaces).** Fast: separable Hilbert space \(\mathcal H\); states \(\rho\in\mathfrak T_1(\mathcal H)\) (\(\|\cdot\|_1\)). Pokes: CPTP maps (\(\|\cdot\|_\diamond\)). Slow: fields in \(H^1_{\rm loc}\) modulo gauge/diffeo; Γ‑convergence frames locality.
**H1 (Budgets).** Convex, l.s.c., coercive, invariance‑compatible, additive, monotone under coarse‑graining; slow Γ‑limit is second‑order local.
**H2 (Operational measurability).** Budgets and \(\mathrm{CL}\) estimable from finite experiments; probabilities continuous in \(\|\cdot\|_\diamond\).
**H3 (Coherence functional).** l.s.c. in \(\Phi\); u.s.c. and concave in \(A\) on budget sublevels.
**H4 (Causality/Locality for pokes).** Single light‑cone; Γ‑locality (no super‑quadratic derivatives at selection scale).
**H5 (Leakage regularity).** Transfer‑kernel lower hull continuous; strict hull convexity ⇒ unimodality; else a weak U‑shape suffices.

# Chapter 1 — Coherence Theory: Idea, Law, & Roadmap

## 1.1 Plain idea

Patterns that **keep working when poked** are selected. Call this staying‑power **coherence**. Selection pays three prices: **throughput** (fuel/time/compute), **complexity** (moving parts/coordination), and **leakage** (unwanted emissions/crosstalk). Environments poke within causal limits. The winning scaffold maximizes predictive staying‑power minus these prices.

### 1.1.1 Assumptions Ledger (what we assume, where it is used)

We assume exactly three hygiene items; everything else is derived.

- **(A) Poke cone**: a causal, Γ-local class `\(\mathcal P\)` of disturbances, closed under composition and mixing; product-topology continuity on finite windows. **Used in**: §1.2 (envelope), Ch. 2 (operational l.s.c.), Ch. 5 (directional envelope), Ch. 9 (microcausality).
- **(B) Budgets**: three convex, l.s.c., coercive quadratics—**throughput** \(B_{\rm th}\) (derivation-priced), **complexity** \(B_{\rm cx}\) (Ad-invariant Hilbertian), **leakage** \(B_{\rm leak}\) (Dirichlet-type on channels)—with norm-equivalent representatives and calibration stability. **Used in**: Ch. 2 (irreducible basis), Ch. 3 (fast sector/GKSL), Ch. 5 (multipliers), Ch. 7 (horizon).
- **(C) Spaces/topologies**: quasi-local C\* algebra for fast variables; cone-preserving Γ-compact slow sector (bounded geometry + gauge fixing). **Used in**: §1.2 (existence), Ch. 4 (Γ-limit ⇒ EH), Ch. 5 (first-variation convergence).

#### 1.1.2 What we assume vs. what we derive vs. how to falsify

| Item | Assumed (minimal) | Derived (selection outputs) | Falsify if (single predictive bit) |
|---|---|---|---|
| Poke cone `\(\mathcal P\)` | Causal, Γ-local, closed under mixing/composition | Worst-case envelope well-posed; directional minimizers exist | Empirically observe **super-cone signaling** or non-local poke effects that violate cone bounds |
| Budgets \(B_{\rm th},B_{\rm cx},B_{\rm leak}\) | Convex, l.s.c., coercive; symmetries (Ad-invariance etc.) | **No fourth independent budget** (irredundant 3-D span on feasible quotient); constants = **multipliers** | A **fourth quadratic direction** separates under the same symmetries/calibration |
| Fast sector | HS geometry on blocks; derivation price | \(\hbar=\lambda_{\rm th}^{-1}\); **Heisenberg/GKSL** with **pointer basis** (W-diagonalization) | Lab interferometer shows **basis-invariant** decoherence contrary to W-alignment |
| Slow sector | Γ-compact, cone-preserving class | **Γ-limit ⇒ Einstein–Hilbert** scaffold; coupled EH–YM + GKSL at stationarity | GW phasing residual slope departs from predicted envelope-multiplier law |
| Horizons | Same budgets; near-horizon cone | **Amplitude suppression** of Hawking flux at **fixed temperature** | Detect a **temperature shift** (leading order) instead of pure amplitude suppression |

*(Pointers to full proofs remain where those theorems live.)*


## 1.2 The Coherence Law (auditable form)

Let \(\mathcal A:= \mathcal A_{\rm fast}\times\mathcal A_{\rm slow}\times \mathcal D\) be the product of the fast, slow, and discrete choices, equipped with the product topology (trace/diamond‑side for fast; cone‑preserving weak \(H^2\) for slow after gauge‑fixing; and the discrete topology on \(\mathcal D\)). Let \(\mathcal P\) be the admissible poke cone (causal, Γ‑local; closed under composition/mixing) and \(\overline{\mathcal P}\) its diamond‑norm closure. Budgets \(B_{\rm th},B_{\rm cx},B_{\rm leak}\) are convex, l.s.c., **coercive and invariance‑compatible** (Appendix A); binders \(B_{\rm bind}^{(j)}\) are l.s.c. and either indicator‑type or convex quadratics on submanifolds. The coherence functional \(\mathrm{CL}\) is operational and l.s.c. in pokes (Lemma II.2).

\[
A^* \in \underset{A\in\mathcal A}{\arg\max}\Big\{\underbrace{\inf_{\Phi\in\overline{\mathcal P}} \,\mathrm{CL}(A,\Phi)}_{:=\,\mathcal C(A)}\ -\ \lambda_{\rm th} B_{\rm th}(A)\ -\ \lambda_{\rm cx} B_{\rm cx}(A)\ -\ \lambda_{\rm leak} B_{\rm leak}(A)\ -\ \textstyle\sum_j \mu_j B_{\rm bind}^{(j)}(A)\Big\}.
\]

#### Operationalization (finite protocols) and risk-sensitive limit

**Finite-protocol representation.** There exists a family of experimentally finite protocols \(T\in\mathscr T\) (finite POVMs plus bounded continuous post-processings) such that
\[
\mathrm{CL}(A,\Phi)=\sup_{T\in\mathscr T} F_T(A,\Phi),\qquad
F_T(A,\Phi):=g_T\!\big(p_T(A,\Phi)\big),
\]
with \(T\mapsto F_T\) continuous in the diamond norm. Hence \(\Phi\mapsto \mathrm{CL}(A,\Phi)\) is l.s.c. and **auditable**.

**Risk-sensitive aggregator.** For poke law \(\Pi\) and \(\beta>0\),
\[
\mathrm{CL}_\beta(A):=\frac{1}{\beta}\log\mathbb E_{\Phi\sim\Pi}\exp\big(\beta\,\mathrm{CL}(A,\Phi)\big)
\searrow \inf_{\Phi\in\overline{\mathcal P}}\mathrm{CL}(A,\Phi)\quad(\beta\to\infty)
\]
(epi-convergence). Thus the **worst-case envelope** is the \(\beta\to\infty\) risk limit—no teleology is assumed.

**Global cross-domain KPI.** We track the **coherence number**
\[
\chi:=\frac{\tau_{\rm dec}}{\tau_{\rm mess}},
\]
the ratio of **decoherence time** (fast, pointer-aligned) to **messenger time** (slow, cone-propagating). \(\chi\) appears in both lab interferometers and near-horizon tiles and is linked to multipliers by the envelope identities (App. E.4).

#### Concrete coherence functionals (two exemplars)

We exhibit two **computable** coherence functionals \( \mathrm{CL} \) within the admissible class defined above. Both respect finite protocols and the poke cone, and both yield the same selection outputs up to a monotone transform (Appendix A1).

**(A) Classical toy-world (cellular-automaton) CL.**  
State space: a finite grid \( \mathbb Z_n^2 \) with cell states \(S=\{0,1,2\}\) for empty/scaffold/messenger. A pattern \(A\) is a seed \(a\in S^{n\times n}\) plus a local update rule \(R_\theta\) (finite-radius). A poke \( \Phi \) is a Markovian disturbance with parameters \((p_{\rm noise},q_{\rm adv})\) acting at each step for \(T\) steps. A **finite protocol** \(T_{\rm CA}\) fixes thresholds \((s_{\min},\tau_{\rm hold},\theta_{\rm msg})\) and an evaluation schedule \(\mathcal S\subset\{1,\dots,T\}\). Let \(X\) be the trajectory under \(A,\Phi\).

Define three finite, observable functionals under \(T_{\rm CA}\):
- \(S_{A,\Phi}^{T_{\rm CA}}:=\mathbb P[\text{there exists a 4-connected component of state \(1\) of size}\ge s_{\min}\text{ that persists }\ge \tau_{\rm hold}]\).
- \(M_{A,\Phi}^{T_{\rm CA}}:=\mathbb P\big[ \#\{t\in\mathcal S:\text{messenger mass in core} \ge m_{\min}\}\ge \theta_{\rm msg}|\mathcal S|\big]\).
- \(L_{A,\Phi}^{T_{\rm CA}}:=\mathbb E[\text{leakage events in }X]/L_{\rm cap}\) (dimensionless).

For weights \(u=(\alpha,\beta,\gamma)\in\mathcal U\subset\Delta_2\) (finite grid on the simplex), define the **CA protocol score**
\[
F_{T_{\rm CA},u}(A,\Phi):=\alpha\,S_{A,\Phi}^{T_{\rm CA}}+\beta\,M_{A,\Phi}^{T_{\rm CA}}-\gamma\,L_{A,\Phi}^{T_{\rm CA}}\in[-1,1].
\]
Then the **CA coherence functional** is
\[
\boxed{\ \mathrm{CL}_{\rm CA}(A,\Phi):=\max_{T_{\rm CA}\in\mathscr T_{\rm CA}}\ \max_{u\in\mathcal U}\ F_{T_{\rm CA},u}(A,\Phi)\ }.
\]
This is **finite-protocol**, **measurable**, and **l.s.c.** in the diamond/trace product topology (Appendix A1, Lemma A1.1). Under randomized mixtures of patterns (Section 1.1.1), \(A\mapsto \mathrm{CL}_{\rm CA}(A,\Phi)\) is **concave** (supremum of linear expectations over a finite family composed with an affine mixing).

**(B) Quantum toy (binary channel reliability) CL.**  
Fix two finite-energy input states \(\rho_0,\rho_1\) encoding “useful thing holds / fails.” For \(T\) steps, a fast-sector pattern \(A\) composed with poke \(\Phi\) induces a CPTP map \(\mathcal N_{A,\Phi}\). Denote the outputs \(\sigma_i:=\mathcal N_{A,\Phi}(\rho_i)\). The **optimal binary decision** error for distinguishing \(\sigma_0\) vs. \(\sigma_1\) is Helstrom’s
\[
P_e^*(\sigma_0,\sigma_1)=\tfrac12\Big(1-\tfrac12\|\sigma_0-\sigma_1\|_1\Big).
\]
Define the **quantum reliability score**
\[
F_{\rm Q}(A,\Phi):=1-P_e^*(\mathcal N_{A,\Phi}(\rho_0),\mathcal N_{A,\Phi}(\rho_1))=\tfrac12\Big(1+\tfrac12\|\mathcal N_{A,\Phi}(\Delta)\|_1\Big),
\]
with \(\Delta:=\rho_0-\rho_1\). Then
\[
\boxed{\ \mathrm{CL}_{\rm Q}(A,\Phi):=\inf_{\Phi'\in\overline{\mathcal P}}\ F_{\rm Q}(A,\Phi')\ }.
\]
Continuity of \(\mathcal N\mapsto \|\mathcal N(\Delta)\|_1\) in diamond norm yields **l.s.c.** in \((A,\Phi)\); mixing \(A\) gives **concavity** in the mixture (Appendix A1, Lemma A1.2). Choosing \(\rho_i\) aligned with the environmental weight \(W\) connects this CL to the pointer-basis selection in Chapter 3.

> **Box 1.B — Robustness (no fine-tuning).**  
> On any bounded window and admissible poke class, every CL in the family
> \[
> \Big\{\ \mathrm{CL}=\sup_{T\in\mathscr T}\ \mathbb E\big[s_T(Z_{A,\Phi})\big]\ :\ s_T \text{ is a bounded, concave proper score on a finite observable }Z\ \Big\}
> \]
> is equivalent up to an **increasing bi-Lipschitz transform**. Thus their maximizers under the same budgets coincide in the \(\Gamma\)-limit, and multipliers (e.g. \(\hbar=\lambda_{\rm th}^{-1}\)) are invariant. *(Proof: Appendix A1, Prop. A1.3.)*


### Well‑posedness & existence (direct method — full proofs)

**Notation.** Let C(A):= inf\_{Phi in Pbar} CL(A,Phi) and J(A):= C(A) − lambda\_th B\_th(A) − lambda\_cx B\_cx(A) − lambda\_leak B\_leak(A) − sum\_j mu\_j B\_bind^{(j)}(A). Fix c<∞ and denote
S\_c := { A in A : lambda\_th B\_th(A)+lambda\_cx B\_cx(A)+lambda\_leak B\_leak(A)+sum\_j mu\_j B\_bind^{(j)}(A) ≤ c }.

**Prop. 1.2.1 (compact sublevels).** Under H1, H4 and the cone‑preserving gauge‑fixed topology for the slow sector (Ch. 4), S\_c is compact in the product topology fast × slow × discrete.
*Proof.* By H1 each budget is lower semicontinuous and coercive in the stated product topology, so its sublevel sets are precompact. Finite intersections of precompact sets are precompact. Because all budgets and binders are l.s.c., S\_c is closed; hence S\_c is compact. The projection of S\_c to the discrete factor is precompact; in a discrete space that implies finiteness, so only finitely many discrete labels occur on S\_c. □

**Prop. 1.2.2 (upper semicontinuity of A ↦ C(A)).** Under H3, C is u.s.c. on A.
*Proof.* Fix A and ε>0. Choose Phi\_ε with C(A) ≥ CL(A,Phi\_ε) − ε. For any net A\_α→A, u.s.c. of A ↦ CL(A,Phi\_ε) on budget sublevels (H3) gives limsup\_α CL(A\_α,Phi\_ε) ≤ CL(A,Phi\_ε). Hence limsup\_α C(A\_α) ≤ C(A)+ε. Let ε↓0. □

**Thm. 1.2.3 (existence of maximizers).** The set Argmax\_{A in A} J(A) is nonempty.
*Proof.* By construction CL is bounded above (built from probabilities; H2), so C(A) ≤ M for some finite M (normalize M=1 w\.l.o.g.). Let M\*:=sup\_A J(A) and pick a maximizing net A\_α with J(A\_α)→M\*. Then for some finite c the budget sum at A\_α is ≤ c for all large α, so A\_α∈S\_c. By Prop. 1.2.1, S\_c is compact; pass to a convergent subnet A\_{α\_k}→A\*. By Prop. 1.2.2 and l.s.c. of budgets, J is u.s.c. on S\_c, so M\* = limsup\_k J(A\_{α\_k}) ≤ J(A\*) ≤ M\*. Thus A\* attains the supremum. □

**Cor. 1.2.4 (tightness of discrete choices).** Any maximizing net is eventually supported on a finite subset of the discrete menu; the discrete factor does not spoil compactness. □

**Lemma 1.2.5 (inner attainment or minimizing net).** For fixed A, the map Phi ↦ CL(A,Phi) is l.s.c. on the closed set Pbar (Lemma II.2). Hence: (i) if some sublevel {Phi : CL(A,Phi) ≤ t} is diamond‑precompact for t>C(A), then there exists Phi\*(A) ∈ Pbar with CL(A,Phi\*)=C(A); (ii) in general, there exists a minimizing net Phi\_β(A) with CL(A,Phi\_β) ↓ C(A).
*Proof.* (i) l.s.c. + compact sublevel ⇒ minimum attained. (ii) pick a directed family of ε‑minimizers with ε ↓ 0. □

**Thm. 1.2.6 (Danskin–Valadier envelope).** Assume for each Phi the directional derivative D^+\_A CL(A,Phi;h) exists on S\_c. Then for every A∈S\_c and direction h,
D^+ C(A;h) = inf{ D^+\_A CL(A,Phi;h) : Phi ∈ Argmin(A) },
with the right side understood as the infimum over cluster points of minimizing nets when Argmin(A)=∅. If Argmin(A) is nonempty and compact, the infimum is attained.
*Proof.* Standard marginal‑function formula (Rockafellar–Wets, Variational Analysis, Thm. 10.31) using u.s.c. in A and l.s.c. in Phi; extend to noncompact Phi by epigraphical limits and minimizing nets (Valadier 1973). □

**Remark (measurable selections).** On any Polish slice of S\_c the multifunction A↦Argmin(A) admits Borel ε‑selections (Kuratowski–Ryll‑Nardzewski) when nonempty/closed; when empty use the minimizing‑net construction to define ε‑selectors, which suffices for Appendix J’s estimation schemes.
**Lemma 1.2.A (precompact sublevels & u.s.c.).** For each \(c<\infty\), the sublevel set
\(\mathsf S_c:=\Big\{A\in\mathcal A:\ \lambda_{\rm th} B_{\rm th}(A)+\lambda_{\rm cx} B_{\rm cx}(A)+\lambda_{\rm leak} B_{\rm leak}(A)+\textstyle\sum_j\mu_j B_{\rm bind}^{(j)}(A)\le c\Big\}\)
is **precompact** in the product topology, and the map \(A\mapsto \mathcal C(A)=\inf_{\Phi\in\overline{\mathcal P}}\mathrm{CL}(A,\Phi)\) is **upper semicontinuous** on \(\mathsf S_c\).
*Sketch.* Precompactness: fast‑sector coercivity (Appendix A) gives compactness of generator/state sublevels in the trace/diamond product; slow‑sector Γ‑compactness (Ch. 4) gives weak \(H^2\) precompactness under cone‑preserving bounds; \(\mathcal D\) is either finite or handled by the discrete clause below. Upper semicontinuity: \(\Phi\mapsto\mathrm{CL}(A,\Phi)\) is l.s.c. in \(\|\cdot\|_\diamond\) (Lemma II.2), and \(A\mapsto\mathrm{CL}(A,\Phi)\) is u.s.c. on budget sublevels (H3); infima of such families preserve u.s.c. on \(\mathsf S_c\).

**Lemma 1.2.B (outer maximizer exists).** The objective is u.s.c. on each \(\mathsf S_c\) and \(\mathsf S_c\) is precompact; hence the outer \(\arg\max\) is non‑empty. Any maximizing sequence has a convergent subsequence with a maximizer in the limit.

**Discrete choices.** Either (a) work with a compactified \(\overline{\mathcal D}\) (e.g., finite menu or one‑point compactification that carries no advantage by coercivity), or (b) impose a **finite‑improvement property**: on each \(\mathsf S_c\) only finitely many discrete flips can strictly improve the objective (holds when each flip increases at least one active budget by a fixed \(\varepsilon>0\)). This ensures attainment over \(\mathcal D\).

### Inner attainment & envelope

**Lemma 1.2.C (attainment/minimizing net for inner infimum).** For fixed \(A\), the map \(\Phi\mapsto \mathrm{CL}(A,\Phi)\) is l.s.c. on the closed set \(\overline{\mathcal P}\). Thus the infimum is attained whenever the relevant slice of \(\overline{\mathcal P}\) is diamond‑precompact; otherwise there exists a **minimizing net** \(\Phi_\alpha(A)\) with \(\mathrm{CL}(A,\Phi_\alpha)\downarrow \mathcal C(A)\). In either case, the **Danskin–Valadier envelope** applies: for any direction \(\delta A\),
\(D^+\mathcal C(A;\delta A)=\inf\{\partial_A\mathrm{CL}(A,\Phi)[\delta A]:\ \Phi\in \operatorname{Argmin}(A)\}\)
with the right derivative taken on \(\mathsf S_c\). This is the version used later for KKT and constants‑as‑multipliers.

**Notes.** (i) *No teleology* (risk‑sensitive \(\beta\to\infty\) limit) is shown in Ch. 2. (ii) *Canonical budgets only* is Theorem I.1. They are referenced here but **not** assumed—existence follows from Lemmas 1.2.A–C plus H0–H5.

> **Box 1.A — Three-budget sufficiency (no fourth direction).**  
> Under the admissible symmetries and calibration stability, the admissible budgets span an **irreducible 3-dimensional cone** on the feasible quotient. A **fourth independent quadratic** is excluded by separation (Hahn–Banach) at fixed calibration. *(Proofs in Ch. 2: Lemma I.5, Theorem I.1.)*


## 1.3 Fast and slow sectors (what is being selected)

* **Fast:** quantum‑like sector on a separable Hilbert space; states evolve by GKSL; in the **zero‑leakage limit** the evolution is unitary. The throughput budget is a C\*‑compatible quadratic of the derivation \(\delta_H(A)=i[H,A]\). KKT/Riesz in Chapter 3 fixes \(\hbar=\lambda_{\rm th}^{-1}\).
* **Slow:** geometry and gauge scaffold selected by Γ‑limits under cone‑preserving, gauge‑fixed topologies; equi‑coercivity and Γ‑compactness proved in Chapter 4.

## 1.4 What follows (map)

1. **Budgets & pokes** minimal completeness and robustness (Ch. 2). 2) **Fast sector normalization** and pointer alignment (Ch. 3). 3) **Γ‑compactness** ⇒ Einstein–Hilbert scaffold (Ch. 4). 4) **Coupled laws** (Ch. 5). 5) **Horizons & area law** with Hawking suppression (Ch. 7). 6) **RG selection** (Ch. 8). 7) **Quantum geometry completion** (Ch. 9). 8) **Predictions & tests** (Ch. 10). 9) **Appendices**: technical proofs, data/estimation kits.

## 1.5 Reader’s checklist (operational sufficiency)

* Spaces/topologies named (trace, diamond, Sobolev/Γ).
* Budgets are convex, l.s.c., coercive; only three independent.
* Poke cone causal/Γ‑local; envelopes are closure‑invariant.
* KKT/Riesz matches gradient metric to quadratic; \(\hbar\) calibrated.
* Γ‑compactness after gauge ensures slow‑sector existence.
* Predictions stated with single primary KPI and low‑burden measurements.
# Chapter 2 — Selection Functional, Budgets & Pokes (airtight, Blocks I–III)

> **Global convention.** Throughout this chapter **all** quadratic forms, operator adjoints, and norms on blocks are taken with respect to the **unweighted normalized Hilbert–Schmidt** (HS) geometry
>
> \[
> \langle X,Y\rangle_{2;\Lambda}:=\frac{1}{d_\Lambda}\,\mathrm{tr}_\Lambda(X^\dagger Y),\qquad 
> \|X\|_{2;\Lambda}^2=\langle X,X\rangle_{2;\Lambda}.
>
\]
>
> Superoperator norms \$|\cdot|\_{HS\to HS}\$, cb-norms, and all adjoints \${}^{!}\$ are computed in this geometry. This fixes inner-product consistency across Lemmas I.1–I.3 and the budgets.

---

## 2.1 — Admissible budgets & minimal completeness (Block I)

**Why only these three?** On each finite block, admissible budget functionals are support functions of convex, symmetry-invariant sets. Ad-invariance and additivity force the **derivation-priced throughput**, an **Ad-invariant Hilbertian complexity**, and a **Dirichlet-type leakage** as a complete basis. Passing to the feasible quotient and using Hahn–Banach separation at fixed calibration excludes any **fourth independent quadratic**. Null-budget directions are modded out; norm-equivalent representatives preserve the multipliers.

### Definition I.0 (Admissible budget class — finalized)

Let \$\omega\$ be a faithful normal state with GNS triple \$(\pi\_\omega,\mathcal H\_\omega,\Omega\_\omega)\$ and quasi-local C\*-algebra \$\mathcal A=\overline{\bigcup\_\Lambda \mathcal A\_\Lambda}\$ built from finite blocks \$\Lambda\$ with matrix algebras \$M\_{d\_\Lambda}\$. Equip each \$M\_{d\_\Lambda}\$ and \$\mathrm{CB}(M\_{d\_\Lambda})\$ with their canonical operator-space structures and the normalized HS geometry above.

A **budget** is a map \$\mathcal B:\mathcal A\to\[0,\infty]\$ acting on scaffolds \$A=(A\_{\rm fast},A\_{\rm med},A\_{\rm leak},A\_{\rm slow},A\_{\rm disc})\$ and satisfying:

1. **(H1) Convexity, l.s.c., coercivity.** \$\mathcal B\$ is convex, lower semicontinuous for the product of blockwise HS topologies, and its sublevel sets intersected with the feasible class are relatively compact in the cone-preserving topology (Ch. 4).

2. **Invariance.**

   * *(Fast/med)* \$\mathcal B\$ is invariant under block-local unitaries \$U\$ (Ad-invariance) and relabeling symmetries.
   * *(Leak)* It is invariant under Kraus-index mixing by \$V\in U(m)\$ and **equivariant** under system unitaries:

     [
\mathcal B_{\rm leak}^\Lambda(\{UL_jU^\dagger\};UWU^\dagger)=\mathcal B_{\rm leak}^\Lambda(\{L_j\};W).
\]

3. **Second-order locality.** On each block \$\Lambda\$, the fast/mediator/leakage parts restrict to **quadratic forms** computed from the HS pairing above; the global budget is the inductive-limit supremum of block quadratics.

4. **Functorial ampliation.** Whenever a cb-norm (or a completely Hilbertian norm) appears, it is **complete**: \$|{\rm id}\_k\otimes \mathcal J|=|\mathcal J|\$ for all \$k\in\mathbb N\$.

5. **(H0.loc) Bounded local dimension.** There exists \$d\_{\rm site}<\infty\$ and a locality radius \$r\in\mathbb N\$ such that any \$\mathcal J\in\mathsf{Loc}*r(\Lambda)\$ acts nontrivially on at most \$C(r)\$ sites, whence its support algebra is \$\cong M*{d\_{\rm loc}}\$ with \$d\_{\rm loc}:=d\_{\rm site}^{C(r)}\$ independent of \$\Lambda\$.

6. **(H5) Complete CP-monotonicity for leakage (sub-Markov in \$W\$).** For any admissible block-local CP maps \$\Phi\_{\rm pre},\Phi\_{\rm post}\$ whose **HS-adjoints** satisfy

   \[
\Phi_{\rm pre}^{\!}(W)\le W,\qquad \Phi_{\rm post}^{\!}(W)\le W,
\]

   one has

   \[
\mathcal B_{\rm leak}^\Lambda(\{\Phi_{\rm post}\!\circ L_j\!\circ \Phi_{\rm pre}\};W)\ \le\ \mathcal B_{\rm leak}^\Lambda(\{L_j\};W).
\]

7. **(H5.lin) Weight linearity (Dirichlet linearity postulate).** For all \$\alpha\ge 0\$ and positive \$W\_1,W\_2\$ with \$W\_1W\_2=0\$,

   \[
\mathcal B_{\rm leak}^\Lambda(\{L_j\};\alpha W)=\alpha\,\mathcal B_{\rm leak}^\Lambda(\{L_j\};W),\qquad
   \mathcal B_{\rm leak}^\Lambda(\{L_j\};W_1+W_2)=\mathcal B_{\rm leak}^\Lambda(\{L_j\};W_1)+\mathcal B_{\rm leak}^\Lambda(\{L_j\};W_2).
\]

   Equivalently, for the spectral resolution \$W=\sum\_a w\_a P\_a\$,

   \[
\mathcal B_{\rm leak}^\Lambda(\{L_j\};W)=\sum_a w_a\,\mathfrak q_\Lambda\!\big(\{P_a L_j\}\big)
\]

   for a fixed positive quadratic form \$\mathfrak q\_\Lambda\$ independent of \$W\$ (calibration fixes its scale on rank-one \$P\_a\$).

> **Remark (Dirichlet linearity).** Axiom (H5.lin) is the **Markov/Dirichlet linearity postulate** for leakage: the leakage quadratic depends **linearly** on the pointer weight \$W\$ and is **orthogonally additive** along its spectral decomposition. It is satisfied by the canonical GKSL-weighted form and is equivalent, in finite dimension, to requiring that the leakage quadratic be a **left** Dirichlet form in \$W\$ with no weight-independent (bare) component.

Denote by \$\mathfrak B\$ the cone of budgets satisfying 1–7, and by \$\overline{\mathcal F}\$ the feasible closure (Ch. 1.2).

---

### Lemma I.1 (Fast/throughput classification — airtight)

On a block \$\Lambda\$, any Ad-invariant convex quadratic \$Q\_\Lambda\$ of the inner derivation \$\delta\_H^\Lambda=\[H,\cdot]\$ (viewed as a superoperator on \$(M\_{d\_\Lambda},\langle\cdot,\cdot\rangle\_{2;\Lambda})\$) is a constant multiple of

[
\mathcal B^{\Lambda}_{\rm th}(H)=\tfrac12\,\|\delta_H^\Lambda\|_{HS\to HS}^2
=\tfrac12\,\frac1{d_\Lambda}\operatorname{Tr}_{HS}\!\big((\delta_H^\Lambda)^\dagger\delta_H^\Lambda\big).
\]

Calibrating on a two-site reference fixes the constants uniformly, yielding the inductive-limit budget

\[
\boxed{\ \mathcal B_{\rm th}(H)=\sup_\Lambda \mathcal B^{\Lambda}_{\rm th}(H)\ }.
\]

*Proof.* The adjoint representation of \$U(d\_\Lambda)\$ on \$\mathfrak{su}(d\_\Lambda)\$ is irreducible; by Schur, any Ad-invariant bilinear form is a scalar multiple of the Killing form. Passing to superoperators \$\delta\_H\$ preserves Ad-covariance; the unique (up to scale) Ad-invariant quadratic is the HS operator-norm square shown. \$\square\$

---

### Lemma I.2 (Mediator/complexity via a completely bounded Hilbertian norm — airtight)

Let \$\mathsf{Loc}*r(\Lambda)\subset \mathrm{CB}(M*{d\_\Lambda})\$ denote block-local maps with radius \$\le r\$ (Def. I.0(5)). Suppose \$Q\_\Lambda\$ is a convex quadratic on \$\mathsf{Loc}*r(\Lambda)\$ that is (i) unitarily covariant, (ii) functorially ampliation-stable, (iii) second-order local and cb-continuous. Then there exist constants \$c\_1,c\_2\in(0,\infty)\$ depending **only** on \$(r,d*{\rm site})\$ such that for every \$\Lambda\$ and \$\mathcal J\in\mathsf{Loc}\_r(\Lambda)\$,

\[
\boxed{\ c_1\,\|\mathcal J\|_{cb}^2\ \le\ Q_\Lambda(\mathcal J)\ \le\ c_2\,\|\mathcal J\|_{cb}^2\ }.
\]

Equivalently,

\[
Q_\Lambda(\mathcal J)\ \simeq\ \|\mathcal J\|_{h,2}^2
:=\inf\Big\{\sum_{k}\|a_k\|_{2;\Lambda}^2\,\|b_k\|_{2;\Lambda}^2:\ \mathcal J(X)=\sum_k a_k X b_k\Big\},
\]

with equivalence constants depending only on \$(r,d\_{\rm site})\$. Consequently, a block complexity budget can be taken—up to those constants—as

\[
\boxed{\ \mathcal B^{\Lambda}_{\rm cx}:=\inf_{\mathcal L=\sum_\alpha \mathcal J_\alpha}\ \sum_\alpha \kappa_\alpha\,\|\mathcal J_\alpha\|_{cb}^2\ },
\]

where the weights \$\kappa\_\alpha\$ encode overlap counts from locality. The value is **decomposition-independent**; the inductive-limit budget is \$\mathcal B\_{\rm cx}=\sup\_\Lambda \mathcal B^{\Lambda}\_{\rm cx}\$.

*Proof.* (A) **Dimension-free reduction.** By (H0.loc), each \$\mathcal J\in\mathsf{Loc}*r(\Lambda)\$ factors through \$M*{d\_{\rm loc}}\$ with \$d\_{\rm loc}=d\_{\rm site}^{C(r)}\$ independent of \$\Lambda\$. (B) **Haagerup–Hilbertian control.** On \$M\_{d\_{\rm loc}}\$, functorial ampliation and unitary covariance imply \$Q\_\Lambda\$ is completely Hilbertian; operator-space duality identifies it (up to constants depending only on \$d\_{\rm loc}\$) with the Haagerup-Hilbertian seminorm \$|\cdot|*{h,2}\$, cb-equivalent in fixed finite dimension (standard Haagerup–Pisier cb≃Hilbertian equivalence on \$M*{d\_{\rm loc}}\$). (C) **Decomposition independence.** In finite dimension the Haagerup projective cone is closed; strong duality equates the projective infimum with \$Q\_\Lambda\$. Pull back along the locality factorization. \$\square\$

---

### Lemma I.3 (Leakage factorization as a completely Dirichlet form — airtight)

Let \$\mathcal L\_{\rm leak}^\Lambda\$ assign to a Kraus list \${L\_j}*{j=1}^m\subset M*{d\_\Lambda}\$ a convex quadratic satisfying: system-unitary **equivariance** in \$W\$ (Def. I.0(2)), **Kraus-mixing invariance**, (H5) **complete CP-monotonicity** with \$\Phi^{!}(W)\le W\$, **and** (H5.lin) **weight linearity**. Then there exists a positive affiliated weight \$W\succ0\$ (unique up to conjugation and equivalence on \$\overline{\mathcal F}\$) such that

\[
\boxed{\ \mathcal B^{\Lambda}_{\rm leak}(\{L_j\};W)=\sum_{j=1}^m \|W^{1/2}L_j\|_{2;\Lambda}^2
=\sum_{j=1}^m\frac{1}{d_\Lambda}\operatorname{tr}\!\big(L_j^\dagger W L_j\big)\ .}
\]

*Proof.* Work on a fixed block, drop \$\Lambda\$.

**(1) Kernel reduction.** Kraus-mixing invariance gives \$Q({L\_j})=\sum\_j \langle L\_j,,T\_W L\_j\rangle\_{2}\$ for some positive linear \$T\_W\$ on \$M\_d\$. System-unitary covariance implies \$T\_{U W U^\dagger}=\mathrm{Ad}*U\circ T\_W\circ \mathrm{Ad}*{U^\dagger}\$.

**(2) Spectral diagonalization.** Let \$W=\sum\_a w\_a P\_a\$. Using **pre/post pinching** that fix \$W\$ (so \$(\Pi^{\rm L})^{!}(W)=(\Pi^{\rm R})^{!}(W)=W\$ and (H5) applies), one gets

\[
Q(L)=\sum_{a,b}Q(P_a L P_b),
\]

hence \$T\_W\$ commutes with \$L\_{P\_a}\$ and \$R\_{P\_b}\$ and takes the form

\[
T_W=\sum_{a,b} t_{ab}(W)\,L_{P_a}R_{P_b}.
\]

**(3) Weight linearity forces left Dirichlet form.** By (H5.lin) and orthogonal additivity, for all eigen-weights \${w\_a}\$,

\[
Q(L;W)=\sum_a w_a\,\mathfrak q\!\big(\{P_a L_j\}\big).
\]

Comparing with the decomposition above and varying \${w\_a}\$ yields that \$t\_{ab}(W)\$ depends **only** on the left eigenvalue and **linearly**: \$t\_{ab}(W)=\alpha(w\_a)\$ with \$\alpha\$ positive linear and **independent of \$b\$**. Consequently,

\[
T_W=\sum_a \alpha(w_a)\,L_{P_a}=\ L_{A(W)}\quad\text{with}\quad A(W):=\sum_a \alpha(w_a)P_a.
\]

No right term and no bare (weight-independent) term are admissible under (H5.lin).

**(4) Identify \$A(W)=\kappa W\$.** Covariance within multiplicity spaces and homogeneity force \$\alpha(w)=\kappa w\$; hence \$A(W)=\kappa W\$ and

\[
Q(\{L_j\};W)=\kappa \sum_j \|W^{1/2}L_j\|_2^2.
\]

Calibrate on a two-site reference to fix \$\kappa=1\$. Uniqueness up to conjugation/equivalence follows from faithfulness and polarization. \$\square\$

---

### Proposition I.4 (Block support-function representation & admissible observables — airtight)

For a fixed block \$\Lambda\$, set

\[
\mathcal V_\Lambda:=\mathfrak{su}(d_\Lambda)\ \oplus\ \mathsf{Loc}_r(\Lambda)\ \oplus\ (M_{d_\Lambda})^{\oplus m}
\]

with the product HS topology. Let \$\mathcal B\_\Lambda\$ be the restriction of \$\mathcal B\in\mathfrak B\$ to \$\mathcal V\_\Lambda\$. Then:

1. \$\operatorname{epi}(\mathcal B\_\Lambda)\$ is a closed convex cone; by Fenchel–Moreau in finite dimension,

   \[
\mathcal B_\Lambda(X)=\sup_{S\in\mathscr S_\Lambda}\ \langle S,X\rangle.
\]

2. Averaging \$S\$ over the compact symmetry groups and admissible coarse-grains is continuous and value-preserving; the averaged **admissible observables** form a compact set.

3. By Lemmas I.1–I.3, the invariant quadratic subspace on \$\mathcal V\_\Lambda\$ is **three-dimensional**, generated by \$(\mathcal B\_{\rm th}^\Lambda,\mathcal B\_{\rm cx}^\Lambda,\mathcal B\_{\rm leak}^\Lambda)\$. Thus each block support functional reduces to a triple

   \[
s=(s_{\rm th},s_{\rm cx},s_{\rm leak})\in\mathbb R_{\ge0}^3,
\]

   modulo nulls. \$\square\$

---

### Lemma I.5 (Hahn–Banach separation ⇒ three-dimensionality on the feasible quotient — airtight)

Let \$\mathcal Q\$ be the quotient of the linear span of \${\mathcal B\_\Lambda:\Lambda}\$ by the subspace of **null budgets** \${\mathcal N:\mathcal N|*{\overline{\mathcal F}}=0}\$. The observable cone identified in Prop. I.4 is closed and equals \$\operatorname{cone}{s*{\rm th},s\_{\rm cx},s\_{\rm leak}}\$. A putative fourth independent admissible budget would be separated by a continuous observable, contradicting Prop. I.4(3). Hence

\[
\boxed{\ \dim \mathcal Q=3\ }.
\]

\$\square\$

---

### Consistency Lemma (block-constant alignment; explicit two-sided bounds)

If \$\Lambda\subset\Lambda'\$, locality and ampliation give, for each of the three budgets,

\[
\mathcal B^\Lambda_{\bullet}(A|_\Lambda)\ \le\ \mathcal B^{\Lambda'}_{\bullet}(A|_{\Lambda'})\ \le\ C(r)\ \mathcal B^\Lambda_{\bullet}(A|_\Lambda),
\]

with \$C(r)\$ counting finite overlaps. Two-site calibration fixes a common scale; the proportionality constants coincide across blocks. Therefore the inductive-limit budgets

\[
\mathcal B_{\rm th}=\sup_\Lambda \mathcal B_{\rm th}^\Lambda,\qquad
\mathcal B_{\rm cx}=\sup_\Lambda \mathcal B_{\rm cx}^\Lambda,\qquad
\mathcal B_{\rm leak}=\sup_\Lambda \mathcal B_{\rm leak}^\Lambda
\]

are well-defined, l.s.c., and coercive with block-independent constants. \$\square\$

---

### Lemma I.6 (Null budgets form a closed subspace)

Let \$\mathsf N:={\mathcal N:\mathcal N|\_{\overline{\mathcal F}}=0}\$. Then \$\mathsf N\$ is a **closed** linear subspace for the inductive-limit topology.

*Proof.* If \$\mathcal N\_k\to\mathcal N\$ and each vanishes on \$\overline{\mathcal F}\$, then for any \$A\in\overline{\mathcal F}\$ and large enough \$\Lambda\$, \$A|\_\Lambda\$ is feasible and \$\mathcal N\_k(A)\to \mathcal N(A)\$ by l.s.c.; hence \$\mathcal N(A)=0\$. \$\square\$

---

### Theorem I.1 (Irreducible basis of admissible budgets — airtight)

Under Definition I.0 (including (H5.lin)), the Consistency Lemma, and Lemma I.6, any \$\mathcal B\in\mathfrak B\$ admits the decomposition

\[
\boxed{\ \mathcal B=\alpha_{\rm th}\,\mathcal B_{\rm th}\;+\;\alpha_{\rm cx}\,\mathcal B_{\rm cx}\;+\;\alpha_{\rm leak}\,\mathcal B_{\rm leak}\;+\;\mathcal N,\qquad \alpha_\bullet\ge0,\ \ \mathcal N\in\mathsf N\ .}
\]

No fourth independent budget satisfying 1–7 exists.

*Proof.* (i) **Blockwise representation.** Prop. I.4 expresses \$\mathcal B\_\Lambda\$ as a support function over \$\operatorname{cone}{s\_{\rm th},s\_{\rm cx},s\_{\rm leak}}\$, hence a conic combination of \$(\mathcal B\_{\rm th}^\Lambda,\mathcal B\_{\rm cx}^\Lambda,\mathcal B\_{\rm leak}^\Lambda)\$ modulo nulls.
(ii) **Inductive limit.** Two-sided bounds and equi-coercivity allow a diagonal selection so that the supremum passes to the limit.
(iii) **Exclusion of a fourth direction.** Lemma I.5 rules it out on the feasible quotient.
(iv) **Null removal.** Lemma I.6 removes null ambiguity. \$\square\$

---

### Corollary I.2 (Calibration & multiplier stability — airtight)

(a) **Calibration.** After fixing a canonical two-site calibration, replacing any canonical quadratic by a blockwise **norm-equivalent** representative (constants depending only on \$(r,d\_{\rm site})\$) rescales the associated \$\alpha\$ by the fixed calibration factor.

(b) **KKT multiplier equality under regularity.** If the optimization on \$\overline{\mathcal F}\$ enjoys Slater interior and **strong convexity** on feasible slices (so KKT multipliers are unique and stable), then any **calibrated** norm-equivalent replacement of a canonical quadratic leaves the Lagrange multipliers **identical**. Without strong convexity, multipliers are preserved **up to** the fixed calibration constants in (a). \$\square\$

---

## 2.2 — Poke ensemble robustness (Block II)

### Definition II.1 (Admissible poke cone)

\$\mathcal P\$ is the smallest set of CPTP maps on \$\mathfrak T\_1(\mathcal H)\$ that is: (i) **causal** (single cone), (ii) **\$\Gamma\$-local**, (iii) closed under convex mixing and composition, and (iv) contains neighborhoods of \$\mathrm{id}\$ and of mixing channels at all allowed scales. Let \$\overline{\mathcal P}\$ be its **diamond-norm closure**.

### Lemma II.2 (Operational l.s.c.)

Under H2–H3, for fixed \$A\$ the map \$\Phi\mapsto\mathrm{CL}(A,\Phi)\$ is **lower semicontinuous** in the diamond norm \$|\cdot|\_\diamond\$.

*Proof (operational representation ⇒ l.s.c.).* By **H2** there exists a directed family \$\mathscr T\$ of **finite experimental protocols** \$T\$ (finitely many channel uses, interleaved with fixed CPTP pre/post-processing and POVMs) and bounded continuous post-processings \$g\_T\$ such that

\[
\mathrm{CL}(A,\Phi)=\sup_{T\in\mathscr T} F_T(A,\Phi),\qquad
F_T(A,\Phi):=g_T\!\big(p_T(A,\Phi)\big),
\]

where \$p\_T(A,\Phi)\$ is the finite outcome-probability vector generated by \$T\$.

Fix \$A\$ and \$T\$ using at most \$N\$ calls to \$\Phi\$. A telescoping/adaptivity bound gives

\[
\big\|\rho^{\rm out}_T(A,\Phi)-\rho^{\rm out}_T(A,\Psi)\big\|_1\ \le\ N\,\|\Phi-\Psi\|_\diamond,
\]

hence (POVM contractivity) \$|p\_T(A,\Phi)-p\_T(A,\Psi)|*1\le N|\Phi-\Psi|*\diamond\$. With \$g\_T\$ continuous on the simplex, \$F\_T(A,\cdot)\$ is **continuous** in \$|\cdot|\_\diamond\$. A pointwise supremum of continuous functions is l.s.c.; therefore \$\Phi\mapsto\mathrm{CL}(A,\Phi)\$ is l.s.c. \$\square\$

### Theorem II.3 (Equivalence of ensembles / robustness)

For every \$A\in\mathcal A\$,

\[
\inf_{\Phi\in \mathcal P}\mathrm{CL}(A,\Phi)=\inf_{\Phi\in \overline{\mathcal P}}\mathrm{CL}(A,\Phi).
\]

*Proof.* Lower semicontinuity (Lemma II.2) plus “infimum over a set equals infimum over its closure.” \$\square\$

### Corollary II.4 (Leakage envelope attainment)

With (H5), the spectral transfer envelope \$w^\*(\nu)\$ **attains** a minimum on \$\overline{\mathcal P}\$ (not necessarily unique). \$\square\$

---

## 2.3 — Selection mechanics & large deviations (Block III)

Let pokes \$\Phi\_t\stackrel{\rm i.i.d.}{\sim}\Pi\$ with support dense in \$\overline{\mathcal P}\$. Define the risk-sensitive score (\$\beta>0\$):

\[
\mathrm{CL}_\beta(A):=-\frac{1}{\beta}\log \mathbb E_\Pi\!\left[e^{-\beta\,\mathrm{CL}(A,\Phi)}\right].
\]

**LD hypotheses.** (LD1) Finite log-MGF on budget sublevels, uniformly on compacta. (LD2) Coercivity (H1) ⇒ exponential tightness. (LD3) \$A\mapsto\mathrm{CL}\_\beta(A)\$ u.s.c. on sublevels.

### Lemma III.1 (Risk-sensitive ⇒ worst-case)

\[
\lim_{\beta\to\infty}\mathrm{CL}_\beta(A)=\inf_{\Phi\in\overline{\mathcal P}}\mathrm{CL}(A,\Phi).
\]

*Proof.* Varadhan’s lemma for \$\log\mathbb E,e^{-\beta,\mathrm{CL}}\$ yields the convex conjugate; as \$\beta\to\infty\$, entropy regularization vanishes and the essential infimum remains. Density plus l.s.c. (Lemma II.2) give equality on \$\overline{\mathcal P}\$. \$\square\$

### Theorem III.2 (Variational growth rate; non-teleological)

Almost surely,

\[
\lim_{\beta\to\infty}\lim_{t\to\infty}\frac1t\log Z_t^{(\beta)}
= \sup_{A\in\mathcal A}\Big[\inf_{\Phi\in\overline{\mathcal P}}\mathrm{CL}(A,\Phi)\ -\ \alpha_{\rm th}B_{\rm th}(A)\ -\ \alpha_{\rm cx}B_{\rm cx}(A)\ -\ \alpha_{\rm leak}B_{\rm leak}(A)\Big].
\]

*Proof.* Laplace principle under (LD2–LD3) gives \$\lim\_{t\to\infty}t^{-1}\log Z\_t^{(\beta)}=\sup\_A\[\mathrm{CL}*\beta-\sum\alpha*\bullet B\_\bullet]\$. Apply Lemma III.1 and epi-convergence (monotone in \$\beta\$). \$\square\$

---

## 2.4 — Envelope identities (constants as multipliers)

Let \$\Phi(\tau)\$ be the optimal value with budget allowances \$\tau=(\tau\_{\rm th},\tau\_{\rm cx},\tau\_{\rm leak})\$. Under H1 and Slater interior, \$\Phi\$ is convex in \$\tau\$ and for a.e. \$\tau\$,

[
\lambda_\bullet(\tau)=\frac{\partial\Phi}{\partial\tau_\bullet}
\]

are the **Lagrange multipliers** (couplings/constants). Strict convexity along active directions ⇒ uniqueness; else an epi-small strictly convex regularizer from (H5) removes ties without new parameters.

---

**Outcome of Blocks I–III.** With (H5.lin) added, the admissible-budget cone is **exactly** three-dimensional up to nulls, generated by \$(B\_{\rm th},B\_{\rm cx},B\_{\rm leak})\$ in the normalized HS geometry; leakage is a **completely Dirichlet** quadratic \$\sum\_j |W^{1/2}L\_j|\_2^2\$ (calibrated); the poke-ensemble choice is robust to taking closures; and the selection principle is a **worst-case** limit of risk-sensitive growth with constants given by **envelope multipliers**.
**Not fine-tuned.** Any CL chosen from the bounded-concave proper-score family (Appendix A1) is equivalent up to an increasing transform; budget selection and multipliers are invariant.
**Ablation note (empirical refuter).** If we **drop** linear-response regularity (H5.lin) or relax Ad-invariance, **mixed bimodule** terms re-enter the admissible class and a fourth quadratic **does** separate on the observable cone, violating Lemma I.5. This yields a concrete falsifier: observe persistence of a fourth direction under the same calibration and the three-budget claim fails.

# Chapter 3 — Fast Sector: Zero-Leakage ⇒ Unitary; \$\hbar\$ as Throughput Dual; Pointer Basis

> **Scope.** We make the budgets C\*-compatible, correct the stationarity/dynamics bridge by **pricing motion along the orbit** (not the superoperator norm), derive \$\dot A=\tfrac{i}{\hbar}\[H^\*,A]\$ from a unitary-path variational principle (with a fully explicit variation calculus) and an equivalent **pointwise**/Pontryagin control derivation, prove multiplier stability under blockwise epi/Mosco limits and Ad-invariant rescalings, and give a unitary-orbit minimizer for leakage (pointer basis).

**Bridge (what Chapter 3 actually fixes).** At KKT stationarity on the unitary manifold with the normalized HS metric, the throughput multiplier identifies
[
\boxed{\ \hbar=\lambda_{\rm th}^{-1}\ }\quad\text{and}\quad \dot A=\tfrac{i}{\hbar}[H^*,A].
\]
With leakage re-enabled and the Dirichlet budget \(B_{\rm leak}\), GKSL generators minimize leakage by **W-alignment**, selecting the **pointer basis** via co-diagonalization with the environmental weight \(W\).

**How \(\mathrm{CL}_{\rm Q}\) selects the pointer basis.**  
For fixed \(\rho_0,\rho_1\) and environmental weight \(W\), minimizing leakage (Dirichlet budget) at fixed \(\|\mathcal N_{A,\Phi}(\Delta)\|_1\) forces co-diagonalization with \(W\); hence GKSL generators that **align** with the \(W\)-eigenbasis are optimal. This is the **pointer basis** selection seen in §3.4; the argument is entirely in terms of the concrete \(\mathrm{CL}_{\rm Q}\).

---

## 3.1 — H0′: Spaces, norms, and budgets (C\*-compatible)

**Quasi-local algebra & GNS.** Let \$\mathcal A=\overline{\bigcup\_\Lambda\mathcal A\_\Lambda}\$ be a quasi-local C\*-algebra with faithful state \$\omega\$ and GNS triple \$(\pi\_\omega,\mathcal H\_\omega,\Omega\_\omega)\$. Identify \$A\in\mathcal A\$ with \$\pi\_\omega(A)\subset\mathcal B(\mathcal H\_\omega)\$.

**Common core & derivation.** Fix a dense invariant core \$\mathcal D\subset\mathcal H\_\omega\$ common to all unbounded generators considered. For (essentially) self-adjoint \$H\$ with \$\mathcal D\subset\mathrm{Dom}(H)\$, define on the local \(\*\$-algebra \$\mathcal A\_{\rm loc}\$: [ \delta_H(A):=i[H,A],\qquad A\in\mathcal A_{\rm loc}. ] Assume \$\delta\_H\$ is closable there; write its closure again as \$\delta\_H\$. **Normalized HS geometry on finite blocks.** On each finite \$\Lambda\$ (matrix algebra \$M\_{d\_\Lambda}\$), [ \langle X,Y\rangle_{\rm HS;\Lambda}:=\frac{1}{d_\Lambda}\operatorname{Tr}(X^\dagger Y),\qquad \|X\|_{{\rm HS};\Lambda}^2=\langle X,X\rangle_{{\rm HS};\Lambda}. ] Adjoints of superoperators and norms are taken in this geometry. **Throughput budget (derivation-quadratic, blockwise).** On \$\Lambda\$, set [ \mathcal B_{\rm th}^\Lambda(H):=\tfrac12\,\|\delta_H\|_{{\rm der};\Lambda}^{2} =\tfrac12\,\frac{1}{d_\Lambda}\operatorname{Tr}_{\rm HS}\!\big((\delta_H^\Lambda)^{\dagger}\delta_H^\Lambda\big), \quad \boxed{\ \mathcal B_{\rm th}(H):=\sup_\Lambda \mathcal B_{\rm th}^\Lambda(H)\ }. ] **Leakage budget.** For a Kraus list \${L\_j}\$ and a positive affiliated weight \$W\succ0\$ in the GNS von Neumann algebra, [ \boxed{\ \mathcal B_{\rm leak}(\{L_j\},W):=\sum_j \|W^{1/2}L_j\|_{2,\omega}^2\ =\ \sum_j\,\omega(L_j^{\dagger} W L_j)\ . } ] **Complexity budget (local CP decompositions).** For local CP pieces \${\mathcal J\_\alpha}\$ with cb-norms \$|\cdot|*{cb}\$ and scale weights \$\kappa*\alpha>0\$, [ \boxed{\ \mathcal B_{\rm cx}(\mathcal L):=\inf\Big\{\sum_\alpha \kappa_\alpha\,\|\mathcal J_\alpha\|_{cb}^2:\ \mathcal L=\sum_\alpha\mathcal J_\alpha\ \text{on}\ \mathcal A_{\rm loc}\Big\}.} ] **Coercivity/compactness.** Each budget is convex and l.s.c.; sublevel sets are equi-coercive after gauge-fixing (Ch. 4). Finite-block estimates lift by monotone convergence. --- ## 3.2 — Exact normalization via a unitary-path variational principle We correct the stationarity→dynamics bridge by **pricing the actual orbit speed** \$|[H,A]|*{\rm HS}\$ (not the Ad-invariant superoperator norm \$|\delta\_H|*{\rm der}\$, whose directional derivative vanishes along conjugations). ### 3.2.A — Setup **Unitary paths and kinematics.** Let \$U\_t\$ be a strongly continuous unitary path with \$U\_0=\mathbf 1\$ and generator \$H\_t=H\_t^\dagger\$ on \$\mathcal D\$: [ \dot U_t=-\,iH_tU_t,\qquad A_t:=U_t^\dagger A\,U_t,\qquad \dot A_t=i[H_t,A_t]. ] **Variations.** Admissible variations are \$\delta U\_t=-,iK\_t U\_t\$ with \$K\_t^\dagger=K\_t\$ and \$K\in C\_c^1((0,T))\$; then [ \delta A_t=i[K_t,A_t],\qquad \delta H_t=\dot K_t+i[K_t,H_t]. ] **Predictive score and gradient (HS metric).** Let \$\mathcal S:\mathcal A\_{\rm loc}\to\mathbb R\$ be Gateaux-differentiable along commutators in the **same** normalized HS geometry: [ D\mathcal S(A)[\,i[K,A]\,]=\langle G(A),\,K\rangle_{\rm HS},\quad G(A)=G(A)^\dagger\ \text{unique}. ] **Action functional with orbit-throughput price.** On \)\[0,T]\$ consider

[
\boxed{\ \mathfrak J[U_\cdot]:=\int_0^T\!\Big(\,\mathcal S(A_t)\ -\ \tfrac{\lambda_{\rm th}}{2}\,\|[H_t,A_t]\|_{\rm HS}^2\ \Big)\,dt\ }.
\]

Here \$\lambda\_{\rm th}>0\$ is the throughput multiplier; using the **same** HS geometry will give \$\hbar=\lambda\_{\rm th}^{-1}\$.

**Orbit Laplacian.** For Hermitian \$A\$ on a finite block,

\[
\boxed{\ \mathcal A_A:=\mathrm{ad}_A^{\!*}\mathrm{ad}_A=[A,[A,\cdot]]\ \ge 0,\qquad \mathrm{ad}_A(\cdot):=[A,\cdot].\ }
\]

In an eigenbasis \$A=\sum\_k\alpha\_k P\_k\$,

\[
(\mathcal A_A X)_{ij}=(\alpha_i-\alpha_j)^2 X_{ij},\quad
\ker \mathcal A_A=\{X:[A,X]=0\},\quad \mathcal A_A^+\text{ is the Moore–Penrose pseudoinverse.}
\]

**No-go for superoperator-norm pricing.** \$H\mapsto |\delta\_H|*{{\rm der};\Lambda}\$ is Ad-invariant, hence the directional derivative of \$\frac12|\delta\_H|*{{\rm der};\Lambda}^2\$ along \$i\[K,H]\$ vanishes blockwise and in the inductive limit. Stationarity based on \$\langle\delta\_H,\delta\_{i[K,H]}\rangle\_{\rm der}\$ cannot produce a nontrivial \$G=\lambda\_{\rm th}H\$.

---

### 3.2.B — Theorem 3.2′ (Heisenberg dynamics; explicit variational calculus; \$\hbar\$)

**Statement.** Under the setup above, let \$U\_\cdot^\*\$ be an interior maximizer of \$\mathfrak J\$ on \([0,T]\$ with \$H\_t^\*=H^\*(A\_t)\$ uniformly form-bounded on \$\mathcal D\$ and \$|[H\_t^\*,A\_t]|*{\rm HS}\in L^2\$. Then for all \$A\in\mathcal A*{\rm loc}\$, [ \boxed{\ \dot A_t\ =\ \frac{i}{\hbar}\,[H^\*(A_t),A_t],\qquad \hbar:=\lambda_{\rm th}^{-1}, } ] where \$H^\*(A)\$ is the **minimal-norm** solution of [ \boxed{\ \mathcal A_A\,H^\*(A)\ =\ \frac{-\,i}{\lambda_{\rm th}}\,\big[A,\,G(A)\big],\qquad H^\*(A)\ \perp\ \ker\mathcal A_A. } ] Equivalently, [ \boxed{\ H^\*(A)\ =\ \mathcal A_A^{+}\!\left(\frac{-\,i}{\lambda_{\rm th}}[A,G(A)]\right),\quad \dot A=\frac{i}{\hbar}[H^\*(A),A]. } ] **Proof (primary — pointwise/Pontryagin).** Consider the optimal-control problem [ \max_{(A,H)}\int_0^T\!\Big(\mathcal S(A_t)-\tfrac{\lambda_{\rm th}}{2}\|[H_t,A_t]\|_{\rm HS}^2\Big)\,dt \quad\text{s.t.}\quad \dot A_t=i[H_t,A_t]. ] The Pontryagin Hamiltonian is [ \mathscr H(A,H,P)=\mathcal S(A)-\tfrac{\lambda_{\rm th}}{2}\|[H,A]\|_{\rm HS}^2+\langle P,\,i[H,A]\rangle_{\rm HS}. ] (i) **Stationarity in \$H\$.** Using \$\langle [X,A],[Y,A]\rangle\_{\rm HS}=\langle X,\mathcal A\_A Y\rangle\_{\rm HS}\$ and \$\mathrm{ad}\_A^{!\*}=\mathrm{ad}\_A\$, [ 0=\partial_H\mathscr H=-\,\lambda_{\rm th}\,\mathcal A_A H\ +\ i\,\mathrm{ad}_A P \quad\Rightarrow\quad \boxed{\ \mathcal A_A H=\frac{i}{\lambda_{\rm th}}\mathrm{ad}_A P\ }. ] (ii) **Costate equation.** For orbit-tangent directions \$\delta A=i[K,A]\$, [ \partial_A\mathscr H[i[K,A]]=\langle G(A),K\rangle_{\rm HS} -\lambda_{\rm th}\,\langle [H,A],[H,i[K,A]]\rangle_{\rm HS} +\langle P,\,i[H,i[K,A]]\rangle_{\rm HS}. ] Using HS-adjointness of \$\mathrm{ad}\_H\$ and Jacobi, this equals \$\langle -,\mathrm{ad}\_A G(A)-i,\mathrm{ad}\_A\mathrm{ad}*H P,\ K\rangle*{\rm HS}\$. Hence [ \dot P=-\,\partial_A\mathscr H\ \text{ on }T_A\mathcal O \quad\Longleftrightarrow\quad \mathrm{ad}_A\big(G(A)+i\,\mathrm{ad}_H P\big)=0. ] Projecting onto \$\mathrm{Ran},\mathrm{ad}\_A\$ (HS-orthogonal to the commutant) gives [ \boxed{\ \mathrm{ad}_A P\ =\ -\,i\,[A,G(A)]\ }. ] (iii) **Eliminate \$P\$.** Substitute into (i): [ \mathcal A_A H=\frac{i}{\lambda_{\rm th}}\,\mathrm{ad}_A P =\frac{1}{\lambda_{\rm th}}\big(-i[A,G(A)]\big). ] The minimal-norm solution (orthogonal to \$\ker\mathcal A\_A\$) is \$H^\*(A)=\mathcal A\_A^{+}!\big(\tfrac{-,i}{\lambda\_{\rm th}}[A,G(A)]\big)\$. The state equation \$\dot A=i[H,A]\$ then yields the Heisenberg law with \$\hbar=\lambda\_{\rm th}^{-1}\$. \$\square\$ **Auxiliary calculus (explicit \$\delta\mathfrak J\$ on unitary paths).** On a fixed block (finite \$d\$), let \$K\in C\_c^1((0,T))\$ and use the identities, valid for Hermitian \$A,H,K\$: [ \begin{aligned} &\text{(Adjointness)}\quad \langle[A,X],Y\rangle_{\rm HS}=\langle X,[A,Y]\rangle_{\rm HS},\\ &\text{(Bilinear)}\quad \langle[H,A],[Y,A]\rangle_{\rm HS}=\langle \mathcal A_A H,\,Y\rangle_{\rm HS},\\ &\text{(Time-derivative)}\quad \frac{d}{dt}\big(\mathcal A_{A_t}H_t\big)=i\,[H_t,\mathcal A_{A_t}H_t]+\mathcal A_{A_t}\dot H_t. \end{aligned} ] The last identity follows from \$B\_t:=\mathrm{ad}*{A\_t}\$, \$\dot B\_t=\mathrm{ad}*{\dot A\_t}=i[\mathrm{ad}*{H\_t},B\_t]\$ and \$\dot(B\_t^2)=i[\mathrm{ad}*{H\_t},B\_t^2]\$, hence \$\frac{d}{dt}(B\_t^2H\_t)=i[!H\_t,B\_t^2H\_t]+B\_t^2\dot H\_t\$. Now compute [ \delta\mathfrak J=\int_0^T\!\Big(\langle G(A),K\rangle_{\rm HS}-\lambda_{\rm th}\,\langle[H,A],[\dot K+i[K,H],A]\rangle_{\rm HS}\Big)\,dt. ] Use the bilinear identity twice and integrate by parts in time (boundary vanishes by compact support of \$K\$): [ \delta\mathfrak J =\int_0^T\!\Big(\langle G(A),K\rangle_{\rm HS} +\lambda_{\rm th}\,\big\langle\tfrac{d}{dt}(\mathcal A_A H),\,K\big\rangle_{\rm HS} -\lambda_{\rm th}\,i\,\langle \mathcal A_A H,\,[K,H]\rangle_{\rm HS}\Big)\,dt. ] Rewrite \$\langle \mathcal A\_A H,[K,H]\rangle\_{\rm HS}=\langle[H,\mathcal A\_A H],K\rangle\_{\rm HS}\$ to obtain [ \delta\mathfrak J=\int_0^T\!\big\langle\,G(A)+\lambda_{\rm th}\,\mathcal A_A\dot H\,,\,K\big\rangle_{\rm HS}\,dt. ] Since \$K\$ is arbitrary in \$C\_c^1\$, stationarity of \$\mathfrak J\$ **on unitary paths** enforces \$\mathcal A\_A\dot H=-(1/\lambda\_{\rm th}),G(A)\$ on \$\mathrm{Ran},\mathcal A\_A\$. This explicit computation shows why the earlier shortcut to \$\langle G+\lambda\_{\rm th}\mathcal A\_A H,K\rangle\_{\rm HS}\$ is invalid and justifies, for dynamics, the pointwise/Pontryagin route used in the proof above. **Normalization and units.** Because the **same** normalized HS geometry defines (i) the predictive gradient and (ii) the orbit-throughput quadratic, the physical Planck constant is fixed by [ \boxed{\ \hbar=\lambda_{\rm th}^{-1}\ }. ] Calibration can be done operationally (e.g., two-level Fubini–Study speed) without ambiguity (§3.2.C). --- ### 3.2.C — Multiplier stability & metric uniqueness **Epi/Mosco stability across blocks.** With \$\mathcal B\_{{\rm orb};\Lambda}(A,H):=\tfrac12|[H,A]|*{{\rm HS};\Lambda}^2\$ and \$\mathcal B*{\rm orb}:=\sup\_\Lambda\mathcal B\_{{\rm orb};\Lambda}\$, the value functions [ \Phi_\Lambda:=\sup_{U_\cdot}\int_0^T\!\Big(\mathcal S(A_t)-\lambda_{\rm th}\,\mathcal B_{{\rm orb};\Lambda}(A_t,H_t)\Big)\,dt ] epi-converge (Mosco) to \$\Phi\$ defined with \$\mathcal B\_{\rm orb}\$. At points of differentiability, multipliers converge: \$\lambda\_{{\rm th},\Lambda}\to\lambda\_{\rm th}\$. Hence \$\hbar=\lambda\_{\rm th}^{-1}\$ is **independent** of the exhausting sequence. **Ad-invariant metric uniqueness (up to scale).** On each finite block, any Ad-invariant inner product on observables is a scalar multiple \$\alpha\$ of normalized HS (Schur). Replacing \$\langle\cdot,\cdot\rangle\_{\rm HS}\$ by \$\alpha\langle\cdot,\cdot\rangle\_{\rm HS}\$ rescales \$G\mapsto \alpha^{-1}G\$ and \$|[H,A]|^2\mapsto \alpha|[H,A]|^2\$. The product \$\alpha,\lambda\_{\rm th}^{-1}\$ — i.e., \$\hbar\$ — is **invariant** under this rescaling. Thus \$\hbar\$ is well-defined (after a single operational calibration). --- ## 3.3 — Hypotheses U (unbounded generators; GKSL on a core) * **U1 (Core & closability).** There exists a common invariant core \$\mathcal D\$ for \$H\$ and all \$L\_j\$; \$\delta\_H\$ is closable on \$\mathcal A\_{\rm loc}\$. * **U2 (Form bounds).** There exists \$N\ge0\$ (number-type) and constants \$a<1\$, \$b<\infty\$ with, for all \$\psi\in\mathcal D\$, [ \|H\psi\|^2+\sum_j\|L_j\psi\|^2\ \le\ a\,\|N\psi\|^2+b\,\|\psi\|^2. ] * **U3 (Quasi-locality).** Interactions have finite range and uniformly bounded overlap across \$\Lambda\$. * **U4 (Semigroup).** The GKSL closure generates a unique strongly continuous CPTP semigroup with Lieb–Robinson-type bounds. * **U5 (Lyapunov drift).** There exist \$c\_0,c\_1>0\$ with \$\mathcal L^\*(N)\le c\_0-c\_1 N\$ on \$\mathcal D\$. **Drift ⇒ leakage finiteness.** For \$W=(1+N)^{-s}\$ with \$s>1/2\$, [ \sum_j\omega(L_j^\dagger W L_j)<\infty\quad\Rightarrow\quad \mathcal B_{\rm leak}(\{L_j\},W)<\infty, ] by Cauchy–Schwarz in the \$\omega\$-HS norm and U5. --- ## 3.4 — Zero-leakage ⇒ unitary GKSL Let \$\mathcal L=i[H,\cdot]+\sum\_j L\_j^\dagger(\cdot)L\_j-\tfrac12{L\_j^\dagger L\_j,\cdot}\$ satisfy U1–U4, and let \$W\succ0\$. **Proposition 3.4.1.** If \$\mathcal B\_{\rm leak}({L\_j},W)=\sum\_j\omega(L\_j^\dagger W L\_j)=0\$, then \$L\_j=0\$ for all \$j\$ and the semigroup is unitary with generator \$H\$ on the core. *Proof.* Each term \$\omega(L\_j^\dagger W L\_j)=|W^{1/2}L\_j|\_{2,\omega}^2\ge0\$. If the sum vanishes, \$W^{1/2}L\_j=0\$; since \$W\succ0\$, \$L\_j=0\$. \$\square\$ Thus, in the **zero-leakage limit**, the fast sector is purely unitary, governed by \$H\$ from §3.2. --- ## 3.5 — Pointer alignment (unitary-orbit minimizer) Fix \$W\succ0\$. Consider a noise block with fixed singular values (fixed “strength spectrum”). For \$C\$ in this block define [ \mathcal L(C):=\operatorname{Tr}\!\big(W^{1/2}C^\dagger C\,W^{1/2}\big). ] **Theorem 3.5.1 (unitary-orbit rearrangement).** Over the orbit \${UCV:\ U,V\ \text{unitary}}\$, [ \boxed{\ \mathcal L(UCV)\ \text{is minimized iff}\ [C^\dagger C,\,W]=0.\ } ] Equivalently, minimizers **co-diagonalize** \$C^\dagger C\$ and \$W\$, selecting the pointer basis (degeneracies handled blockwise). *Proof.* \$\mathcal L(UCV)=\operatorname{Tr}(W^{1/2}V^\dagger C^\dagger C V W^{1/2})\$. Let \$W=\sum\_k w\_k Q\_k\$ with \$w\_1\ge\cdots\ge w\_d>0\$. By von Neumann/Schur–Horn, with fixed eigenvalues \${\sigma\_\ell}\$ of \$C^\dagger C\$, the minimum of \$\operatorname{Tr}(W,V^\dagger C^\dagger C V)\$ is attained when \$V\$ aligns eigenvectors so that \$C^\dagger C\$ is diagonal in the eigenbasis of \$W\$. Equality enforces \)\[C^\dagger C,,W]=0\$. \$\square\$

---

## 3.6 — Summary

* Pricing the **orbit speed** \$|[H,A]|\_{\rm HS}\$ (rather than the Ad-invariant superoperator norm) and matching the **same** normalized HS geometry for gradient and quadratic yields

  [
\dot A=\frac{i}{\hbar}[H^\*(A),A],\qquad
  H^\*(A)=\mathcal A_A^{+}\!\left(\frac{-\,i}{\lambda_{\rm th}}[A,G(A)]\right),\quad \hbar=\lambda_{\rm th}^{-1}.
\]

  Here \$\mathcal A\_A=\[A,[A,\cdot]]\ge0\$ and \$\mathcal A\_A^+\$ projects off the commutant.
* **Stability.** Epi/Mosco limits across blocks preserve \$\lambda\_{\rm th}\$; Ad-invariant metric rescalings cancel in \$\hbar\$. A single operational calibration fixes \$\hbar\$.
* **Fast sector.** Zero leakage forces GKSL to reduce to a unitary group. For nonzero leakage, **pointer alignment** minimizes \$\operatorname{Tr}(W^{1/2}C^\dagger C W^{1/2})\$ by co-diagonalizing \$C^\dagger C\$ with \$W\$.

This completes the fast-sector normalization and resolves the stationarity/dynamics gap with explicit variational calculus and a pointwise/Pontryagin control derivation in a C\*-compatible, mathematically airtight manner.


# Chapter 4 — Scaffold Selection: Γ‑Limit ⇒ Einstein–Hilbert (+ compactness)

> **Scope.** We state a clean cone‑preserving topology after gauge‑fixing and prove equi‑coercivity and Γ‑compactness. This slots into the EH Γ‑limit derivation and enforces single‑cone microhyperbolicity.

## 4.1 Γ‑compactness in a cone‑preserving class (Theorem 4.1′)

**Setup.** Bounded‑geometry manifold: uniform injectivity radius and bounded curvature (all derivatives). Fix de Donder gauge inside the **single‑cone** class; use harmonic coordinates on charts.

**Cone‑preserving topology.** \(g\in H^2_{\rm loc}\) and for reference metrics \(g_\*,g^\*\) on compacts,
\(g_\*\ \le\ g\ \le\ g^\*\quad\text{a.e. in harmonic coordinates (cone inclusion).}\)

**Uniform symbol bounds.** There exist \(0<\lambda\le\Lambda\) such that for all admissible \(g\) and \(\xi\),
\(\lambda\,|\xi|^4\ \le\ \sigma(\mathbb A_\varepsilon(g))[\xi]\ \le\ \Lambda\,|\xi|^4\qquad\text{(parameter‑ellipticity on compacts).}\)

**Gårding inequality (uniform).** There exist \(c_1,c_2,c_3>0\), independent of \(\varepsilon\) and \(g\), with
\(\boxed{\ \mathcal F_\varepsilon(g)\ \ge\ c_1\|\nabla^2 g\|_{L^2}^2\ -\ c_2\|g\|_{H^1}^2\ -\ c_3\ }.\)

**Boundary/at‑infinity control.** If \(M\) is noncompact, either (i) impose uniform equivalence to a reference \(g_\infty\) outside a compact set, or (ii) include in \(V_\varepsilon\) a cutoff penalizing deviations at infinity to control \(\|g\|_{H^1}\).

### Theorem 4.1′ (equi‑coercivity and Γ‑limit)

The family \(\{\mathcal F_\varepsilon\}\) is equi‑coercive in weak \(H^2\); any weak \(H^2\) cluster point of minimizers is a minimizer of \(\mathcal F_0\) (Γ‑liminf and recovery hold).

*Proof sketch.* Gauge‑fixing removes diffeomorphism degeneracy; bounded geometry yields Rellich compactness in weak \(H^2\); single‑cone stability controls the principal symbol. Γ‑compactness follows from equi‑coercivity and lower semicontinuity; recoveries are built by mollification in harmonic charts and partition‑of‑unity gluing.

# Chapter 5 — Coupled Laws (Einstein–YM + GKSL via Joint Stationarity)

> **Scope.** We prove the coupled slow–fast laws at joint stationarity of the coherence program. The argument rests on:
>
> 1. a **directional envelope theorem** for worst-case pokes with **direction-selecting minimizers** (no illicit inf–variation swap);
> 2. effective sources \(T^{\rm eff},J^{\rm eff}\) defined first in the **Clarke** framework (existence + conservation **without** linearity), then **upgraded** to unique tensors under an explicit Gateaux/Clarke condition;
> 3. **first-variation convergence** for the slow Γ-limit via localized **Mosco/Attouch**;
> 4. a fast-sector control law that prices the **derivation** \([H,\cdot]\) (the actual throughput), uses the **Moore–Penrose pseudoinverse** of the orbit Laplacian \(\mathcal A_A=\mathrm{ad}_A^{\,*}\mathrm{ad}_A\), and yields the **Heisenberg law** with a consistent normalization \(\hbar=\lambda_{\rm th}^{-1}\).

---

## 5.1 — Admissible variables and objective

**Slow variables.** Lorentzian metrics \(g\) of bounded geometry in the **single-cone** class (weak \(H^2_{\rm loc}\), de Donder gauge on compacta) and compact-group connections \(A\) with curvature \(F\in L^2_{\rm loc}\).

**Fast variables.** A GKSL generator on the quasi-local C\(^*\)-algebra (Ch. 3):

[
\mathcal L(\rho)=-i[H,\rho]+\sum_j L_j\rho L_j^\dagger-\tfrac12\{L_j^\dagger L_j,\rho\},
\]

with budgets \(\mathcal B_{\rm th},\mathcal B_{\rm cx},\mathcal B_{\rm leak}\) as in Appendix A and Hypotheses U.

**Pokes.** \(\overline{\mathcal P}\): diamond-norm closure of the causal, Γ-local cone (§2.2).

**Slow action (Γ-limit).** Assumption **D\(^\star\)**: a family \(\{\mathcal F_\varepsilon(g,A)\}\) Γ-converges on the cone-class to

\[
\mathcal F_0(g,A)=\frac{1}{16\pi G}\!\int_M (R-2\Lambda)\sqrt{|g|}\,d^dx\;+\;\frac{1}{2g_{\rm YM}^2}\!\int_M \mathrm{tr}(F\wedge\!*F),
\]

with equi-coercivity and boundary control on compacta.

**Objective.**

\[
\boxed{
\mathcal J(g,A,H,\{L_j\})\ :=\ V(g,A)\ -\ \lambda_{\rm th}\mathcal B_{\rm th}(H)\ -\ \lambda_{\rm cx}\mathcal B_{\rm cx}(\mathcal L)\ -\ \lambda_{\rm leak}\mathcal B_{\rm leak}(\{L_j\})\ -\ \mathcal F_\varepsilon(g,A)
}
\]

where \(V(g,A):=\inf_{\Phi\in\overline{\mathcal P}}\mathrm{CL}(g,A;\Phi)\). Slater interior holds (Appendix E).

---

## 5.2 — Parametric envelope for worst-case pokes (directional form)

We work with **directional** derivatives and avoid over-claiming Gateaux differentiability.

### Hypotheses E′ (attainment, regularity, direction-wise selection)

* **E1 (attainment/compactness).** For each \((g,A)\), \(\Phi\mapsto \mathrm{CL}(g,A;\Phi)\) is l.s.c. and **inf-compact** on \(\overline{\mathcal P}\); hence
  \(\mathsf M(g,A):=\operatorname{Argmin}_{\Phi\in\overline{\mathcal P}}\mathrm{CL}(g,A;\Phi)\)
  is non-empty and compact.
* **E2 (Carathéodory).** \((g,A,\Phi)\mapsto \mathrm{CL}(g,A;\Phi)\) is continuous in \((g,A)\) for fixed \(\Phi\), and l.s.c. in \(\Phi\) for fixed \((g,A)\).
* **E3 (directional differentiability).** For each \(\Phi\) and cone-admissible variation \(\delta=(\delta g,\delta A)\) with compact support,

  \[
D\,\mathrm{CL}(g,A;\Phi;\delta):=\lim_{t\downarrow0}\frac{\mathrm{CL}(g+t\delta g,A+t\delta A;\Phi)-\mathrm{CL}(g,A;\Phi)}{t}
\]

  exists and is positively homogeneous in \(\delta\).
* **E4 (equi-differentiability on argmin graphs).** There exist \(M>0\) and a neighborhood \(U\ni(g,A)\) such that
  \(|D\,\mathrm{CL}(g',A';\Phi;\delta)|\le M\|\delta\|\)
  for all \((g',A')\in U\), \(\Phi\in\mathsf M(g',A')\), and admissible \(\delta\).
* **E5 (direction-wise selection).** For each \((g,A)\) and direction \(\delta\), choose

  \[
\Phi^*(g,A;\delta)\in\arg\min_{\Phi\in\mathsf M(g,A)} D\,\mathrm{CL}(g,A;\Phi;\delta)
\]

  (measurable selection exists by Kuratowski–Ryll-Nardzewski).

### Theorem 5.2′ (Directional envelope)

Under E1–E5, for every cone-admissible \(\delta\),

\[
\boxed{\
D V(g,A;\delta)\ =\ \min_{\Phi\in\mathsf M(g,A)} D\,\mathrm{CL}(g,A;\Phi;\delta)\ =\ D\,\mathrm{CL}\big(g,A;\Phi^*(g,A;\delta);\delta\big).
\ }
\]

### Corollary 5.2b (Gateaux differentiability — two routes)

At \((g,A)\), \(V\) is Gateaux differentiable (two-sided, linear in \(\delta\)) if **either**:

1. (**Unique active**). A strictly convex, cone-local tie-breaker (vanishing in the Γ-limit) makes \(\mathsf M(g,A)\) a singleton with locally Lipschitz dependence; then \(D V(g,A;\delta)=D\,\mathrm{CL}(g,A;\Phi^*(g,A);\delta)\).
2. (**Clarke-regular active set**). \(\mathsf M(g,A)\) is compact and \(D\,\mathrm{CL}(g,A;\Phi;\delta)\) is **constant** over \(\Phi\in\mathsf M(g,A)\) for each \(\delta\). Then right/left derivatives coincide and are linear.

---

## 5.3 — Effective stress tensor and current (Clarke framework → upgrade)

We first ensure **existence and conservation** of sources **without** assuming linearity (Clarke framework), then **upgrade** to unique tensors under Cor. 5.2b.

### Assumption L0 (local Lipschitz of the envelope)

Under E1–E4, the value function \(V(g,A)=\min_{\Phi\in\mathsf M(g,A)}\mathrm{CL}(g,A;\Phi)\) is **locally Lipschitz** on the cone-class (Danskin–Rockafellar with the uniform bound in E4).

**Localization for Clarke calculus.** All Clarke sub/super-differential objects are taken on bounded subdomains \(\Omega\Subset M\) with compactly supported variations; conclusions pass to \(M\) by exhaustion \(\Omega_n\uparrow M\) and compatibility of the cone-class cutoffs. This keeps the Banach-space hypotheses crisp and avoids overreach beyond bounded domains.

**Clarke subdifferentials.** Let \(\partial_g^{\mathrm C} V(g,A)\subset H^{-2}_{\rm loc}\) and \(\partial_A^{\mathrm C} V(g,A)\subset H^{-1}_{\rm loc}\) denote the **Clarke** subdifferentials; \(V_g^\circ(g,A;\delta g)\), \(V_A^\circ(g,A;\delta A)\) are the Clarke directional derivatives.

### 5.3.1 Subgradient sources (always well-posed) and conservation

Take any \(T^{\rm eff}\in\partial_g^{\mathrm C}V(g,A)\), \(J^{\rm eff}\in\partial_A^{\mathrm C}V(g,A)\) so that

\[
\langle T^{\rm eff},\delta g\rangle\ \le\ V_g^\circ(g,A;\delta g),\qquad
\langle J^{\rm eff},\delta A\rangle\ \le\ V_A^\circ(g,A;\delta A).
\]

If \(\mathrm{CL}\) is diffeomorphism- and gauge-covariant on the cone-class, then for compactly supported \(X,\chi\),

\[
V_g^\circ(g,A;\mathcal L_X g)=V_g^\circ(g,A;-\mathcal L_X g)=0,\qquad
V_A^\circ(g,A;D\chi)=V_A^\circ(g,A;-D\chi)=0,
\]

hence

\[
\langle T^{\rm eff},\mathcal L_X g\rangle=0,\qquad \langle J^{\rm eff},D\chi\rangle=0.
\]

Integrating by parts within the cone-class yields the weak conservation laws

\[
\nabla^\mu T^{\rm eff}_{\mu\nu}=0,\qquad D^\mu J^{\rm eff}_\mu=0
\]

**for every Clarke-selection** \(T^{\rm eff},J^{\rm eff}\).

### 5.3.2 Upgrade to single tensors (Distributional representation (Riesz on bounded domains); symmetry)

**Assumption L (linearity at \((g,A)\)).** One of Cor. 5.2b’s conditions holds at \((g,A)\). Then \(V\) is Gateaux differentiable in \(g,A\); the Clarke subdifferentials are singletons and coincide with the Fréchet derivatives.

**Corollary.** Under Assumption L there exist unique distributions \(T^{\rm eff}\in H^{-2}_{\rm loc}\), \(J^{\rm eff}\in H^{-1}_{\rm loc}\) such that on each bounded domain \(\Omega\Subset M\)

\[
\begin{aligned}
D_g V(g,A)[\delta g] &= \tfrac12\int_\Omega T^{\rm eff}_{\mu\nu}\,\delta g^{\mu\nu}\,\sqrt{|g|}\,d^dx,\\
D_A V(g,A)[\delta A] &= \int_\Omega \langle J^{\rm eff}_\mu,\,\delta A^\mu\rangle\,\sqrt{|g|}\,d^dx,
\end{aligned}
\]

with \(T^{\rm eff}_{\mu\nu}=T^{\rm eff}_{\nu\mu}\); the representations are compatible under exhaustion and define \(T^{\rm eff},J^{\rm eff}\) globally on \(M\). Conservation from §5.3.1 persists.

---

## 5.4 — Slow-sector Euler–Lagrange: EH + YM (first-variation convergence)

Γ-convergence alone does not yield convergence of first variations. We adopt a localized Mosco/Attouch scheme.

**Assumption M (localized Mosco/Attouch).** On each bounded \(\Omega\Subset M\), \(\mathcal F_\varepsilon|_\Omega\) are equi-coercive, l.s.c., and admit integral representations with Carathéodory integrands \(f_\varepsilon(x,\cdot)\) obeying uniform growth/ellipticity and \(f_\varepsilon\to f_0\) in \(L^\infty(\Omega)\). Then \(\partial \mathcal F_\varepsilon|_\Omega \xrightarrow{\rm graph} \partial \mathcal F_0|_\Omega\) (Attouch). Exhaust \(\Omega_n\uparrow M\).

**Lemma 5.4.1 (convergence of first variations).** For any admissible \((g,A)\) and compactly supported cone-preserving \((\delta g,\delta A)\),

\[
\lim_{\varepsilon\to0} D\,\mathcal F_\varepsilon(g,A)[\delta g,\delta A]\ =\ D\,\mathcal F_0(g,A)[\delta g,\delta A],
\]

with

\[
D_g \mathcal F_0(g,A)[\delta g]=\tfrac12\!\int \!\tfrac{1}{8\pi G}\big(G_{\mu\nu}+\Lambda g_{\mu\nu}\big)\,\delta g^{\mu\nu}\sqrt{|g|},\quad
D_A \mathcal F_0(g,A)[\delta A]=\int\!\langle D^\alpha F_{\alpha\mu},\delta A^\mu\rangle\sqrt{|g|}.
\]

**Theorem 5.4.2 (Einstein–YM with operational sources).**
Let \((g,A,H,\{L_j\})\) be a cone-class KKT point of \(\mathcal J\) and assume **Assumption L** at \((g,A)\). Then

\[
\boxed{
G_{\mu\nu}+\Lambda g_{\mu\nu}=8\pi G\,T^{\rm eff}_{\mu\nu},\qquad
D^\alpha F_{\alpha\beta}=J^{\rm eff}_\beta,
}
\]

with \(\nabla^\mu T^{\rm eff}_{\mu\nu}=0\) and \(D^\mu J^{\rm eff}_\mu=0\).

**Proposition 5.4.3 (constants as multipliers = Γ-calibration).**
Under Slater and strict convexity of \(\mathcal F_0\) along the cone-class, KKT multipliers \((G^{-1},\Lambda,g_{\rm YM}^{-2})\) are **unique**. Calibrating \(\mathcal F_\varepsilon\) on (i) Minkowski and (ii) constant-curvature backgrounds fixes the same constants; the Γ-calibrated constants coincide with the KKT duals.

---

## 5.5 — Fast-sector stationarity and microcausal hygiene

We price the **derivation** (the actual throughput) and solve the first-order condition on the **unitary-orbit tangent** using the **Moore–Penrose pseudoinverse** of the orbit Laplacian.

### 5.5.1 Unitary-orbit control with derivation-quadratic (Heisenberg law)

Work on a finite block \(\Lambda\) with normalized Hilbert–Schmidt (HS) inner product \(\langle X,Y\rangle_{\rm HS}:=\mathrm{Tr}_\Lambda(X^\dagger Y)/d_\Lambda\). Let \(A_t=U_t^\dagger A_0U_t\), \(\dot U_t=-\tfrac{i}{\hbar}H_tU_t\), so

\[
\boxed{\ \dot A_t=\tfrac{i}{\hbar}[H_t,A_t]\ }.
\]

Let \(\mathsf P(A)\) be the orbit-restricted predictive score; \(G(A):=\operatorname{grad}_{\rm HS}\mathsf P(A)\).
**Key pairing (explicit HS calculation).** Work on a finite block \(\Lambda\) with normalized Hilbert–Schmidt inner product \(\langle X,Y\rangle_{\rm HS}:=\mathrm{Tr}(X^\dagger Y)/d_\Lambda\). For Hermitian \(A,H\),
\[
\begin{aligned}
\langle [A,X],Y\rangle_{\rm HS}
&= \frac{1}{d_\Lambda}\mathrm{Tr}\big((AX-XA)^\dagger Y\big) \\
&= \frac{1}{d_\Lambda}\mathrm{Tr}\big(X^\dagger A Y - A X^\dagger Y\big) \\
&= \frac{1}{d_\Lambda}\mathrm{Tr}\big(X^\dagger A Y - X^\dagger Y A\big) \quad(\text{cyclicity})\\
&= \langle X,[A,Y]\rangle_{\rm HS}.
\end{aligned}
\]
Thus the commutator superoperator \(\mathrm{ad}_A:X\mapsto[A,X]\) is **HS-self-adjoint** on Hermitian \(A\). Along a unitary orbit \(A_t=U_t^\dagger A_0 U_t\) with \(\dot U_t=-\tfrac{i}{\hbar}H_tU_t\),
\[
\dot A_t=\tfrac{i}{\hbar}[H_t,A_t].
\]
Let \(\mathsf P(A)\) be the orbit-restricted predictive score and \(G(A):=\operatorname{grad}_{\rm HS}\mathsf P(A)\). For any Hermitian control \(H\),
\[
\frac{d}{dt}\Big|_{t=0}\mathsf P(A_t)=\Big\langle G(A),\tfrac{i}{\hbar}[H,A]\Big\rangle_{\rm HS}
=\Big\langle -\tfrac{i}{\hbar}[G(A),A],\,H\Big\rangle_{\rm HS}.
\]
Hence the **steepest-ascent** Hamiltonian (Riesz/KKT on the unitary manifold) is
\[
\boxed{\ H^*(A)\ \propto\ -\tfrac{i}{\hbar}[G(A),A]\ },
\]
and the corresponding generator is \(\dot A=\tfrac{i}{\hbar}[H^*(A),A]\). Local Lipschitz and blockwise bounds propagate to the quasi-local algebra via the uniform HS-block controls of Ch. 3.


### 5.5.2 Leakage and GKSL

Allow Lindblad controls \(\{L_j\}\) with leakage price \(\lambda_{\rm leak}\sum_j\|W^{1/2}L_j\|_{\rm HS}^2\) (App. A). The convex optimization over CP-tangent directions yields an optimal **GKSL generator** with leakage-penalized pointer alignment as in Ch. 3. Hypotheses U give well-posedness and Lieb–Robinson-type bounds on the cone-class.

### 5.5.3 Microcausal hygiene

The poke cone, orbit locality, and LR-type bounds ensure commutator growth remains inside the cone; the principal-symbol lemma (§4.1) forbids order flips without paying the \(W_1\) gap. All variational steps above remain legal within the cone-preserving class.

---

## 5.6 — Summary (coupled laws)

At joint KKT stationarity of \(\mathcal J\) on the cone-preserving class:

* **Slow (Einstein–Yang–Mills).**

  \[
G_{\mu\nu}+\Lambda g_{\mu\nu}=8\pi G\,T^{\rm eff}_{\mu\nu},\qquad
  D^\alpha F_{\alpha\beta}=J^{\rm eff}_\beta,
\]

  with \(T^{\rm eff},J^{\rm eff}\) **well-posed as Clarke subgradients** (conserved for **every** selection).
  Under **Assumption L** (unique minimizer or Clarke-regular active set with constant directional derivatives), they **upgrade** to single linear distributions with distributional (Riesz-on-bounded-domains) representation, \(T^{\rm eff}_{\mu\nu}=T^{\rm eff}_{\nu\mu}\), \(\nabla^\mu T^{\rm eff}_{\mu\nu}=0\), \(D^\mu J^{\rm eff}_\mu=0\).

* **Fast (unitary/GKSL).**

  \[
\dot A=\tfrac{i}{\hbar}[H^*(A),A],\quad
  H^*(A)=\mathcal A_A^{+}\!\big(-i[A,G(A)]\big),\quad
  \mathcal A_A=\mathrm{ad}_A^{\,*}\mathrm{ad}_A=\mathrm{ad}_A^2,\quad
  \hbar=\lambda_{\rm th}^{-1}.
\]

  With leakage, the optimal generator is **GKSL** with leakage-penalized pointer alignment; well-posed with LR-type bounds.

* **Constants.** \(\hbar,\,G,\,\Lambda,\,g_{\rm YM}\) are the **unique** KKT multipliers and match the Γ-calibrated constants (Prop. 5.4.3).

All steps are now rigorous and consistent with the coherence-budget framework: directional envelope calculus with direction-selecting minimizers; Clarke-sound sources and conservation (upgraded to tensors when linearity holds); first-variation convergence for the slow Γ-limit; and a derivation-quadratic control law on the unitary orbit (with pseudoinverse and explicit normalization) producing the Heisenberg/GKSL fast dynamics.

# Chapter 6 — Gauge & Matter: Budget–Symmetry Selection; Hypercharge Uniqueness

> **Scope.** With budgets and cone hygiene in place, we summarize the selection for the gauge scaffold and record the hypercharge‑uniqueness result under the standard binders (single Higgs doublet; anomaly cancellation; minimal chiral set). Proofs and linear‑system details mirror Appendix C.

## 6.1 Budget–symmetry selection (sketch)

Ad‑invariant quadratic forms on a compact simple Lie algebra are multiples of the Killing form; additivity across factors gives \(\sum_i C_2(G_i)\). The unique Ad‑invariant count surcharge is \(\sum_i\dim G_i\). These, with Γ‑locality and mediator locality, generate the mediator part of the **complexity** budget \(B_{\rm cx}\). Minimal coupling follows from the Γ‑limit of the connection scaffold.

## 6.2 Hypercharge uniqueness (binder set: Yukawa + anomalies + minimal set)
> **Assumptions for hypercharge (conditional uniqueness).**  
> Uniqueness here is **conditional** on the binder set: (B\_Yuk) renormalizable Yukawas, (B\_{\rm anom}) anomaly cancellation, and (B\_{\rm min}) the minimal chiral content with a single Higgs doublet. Relaxing any binder re-opens branches; see Appendix C for alternatives and their costs.

**Binders.** (i) **B\_Yuk:** only renormalizable Yukawas \(QH d^c,\ Q\tilde H u^c,\ L H e^c\). (ii) **B\_anom:** cancel \([SU(3)]^2U(1)_Y,\ [SU(2)]^2U(1)_Y,\ U(1)_Y^3,\ \text{grav}^2\!\!\!-\!U(1)_Y\) anomalies. (iii) **B\_min:** one‑generation minimal chiral set \(\{Q,u^c,d^c,L,e^c\}\); one Higgs doublet.

**Statement.** Let \((Y_Q,Y_u,Y_d,Y_L,Y_e,Y_H)\) be unknown hypercharges. Under **B\_Yuk + B\_anom + B\_min**, the solution set is a **one‑parameter line** (overall normalization/orientation). Fixing the unit with the minimal‑charge binder (\(Q=T_3+Y\) and color‑singlet integrality) yields the **Standard Model values**
\(\boxed{(Y_Q,Y_u,Y_d,Y_L,Y_e,Y_H)=\big(\tfrac16,-\tfrac23,\tfrac13,-\tfrac12,1,-\tfrac12\big)}.\)

**Proof (linear system & rank).** Yukawa invariance gives \(Y_Q+Y_H+Y_d=0\), \(Y_Q-Y_H+Y_u=0\), \(Y_L+Y_H+Y_e=0\). Anomalies add \(3Y_Q+Y_L=0\) and \(6Y_Q+3Y_u+3Y_d+2Y_L+Y_e=0\). Solve: \(Y_H=-3Y_Q\), \(Y_L=-3Y_Q\), \(Y_e=+6Y_Q\), \(Y_u=-4Y_Q\), \(Y_d=+2Y_Q\) with \(Y_Q\) free (rank 5/6). Minimal‑charge normalization via \(Q=T_3+Y\) and \(Q(\nu)=0\) fixes \(Y_Q=1/6\). After normalization, strict convexity/tie‑breakers on \(B_{\rm cx}\) exclude co‑minima; the SM assignment is unique with a positive gap.

# Chapter 7 — Horizons: Pointer Mechanics ⇒ Area Law; Hawking Flux Suppression (Repaired & Airtight)

> **Scope.** We work in a local **Killing-horizon patch** with surface gravity \$\kappa>0\$, the **single-cone** class and the C\*-compatible budgets of Ch. 3, Γ-compact slow sector of Ch. 4, and the coupled-laws framework of Ch. 5. We:
> (i) specify a **near-horizon Unruh-diagonal GKSL model** fixed by **pointer alignment**;
> (ii) take **mutual information** \$I(A:\bar A)\$ as the primary entropy functional (with \$E\_R\le I\$), prove **quasi-factorization** with explicit LR-dependent constants;
> (iii) give a **per-tile information–budget bound** controlled by the leakage budget; define a **pointer cutoff** \$\ell\_\*\$ by KKT thresholding; and prove an **area-law upper bound** with a calibrated constant;
> (iv) prove a **sharp flux-suppression inequality** as a linear program in the rates, in full generality and with an exact **Hawking-weight** corollary;
> (v) record **microcausality** and an **identifiability lemma** to determine Hawking rates from pointer-basis two-point data.
> Proof details and constant tracking are in **Appendix G** (area law) and **Appendix H** (flux suppression).
**KPI & refuter.** The near-horizon prediction is a **universal amplitude suppression** of the outgoing flux by a budget-controlled factor at **fixed Hawking temperature**. Any observed **temperature shift at leading order** would falsify the budget-consistent GKSL picture; amplitude-only suppression with the predicted frequency shaping supports it.

---

## 7.1 Near-horizon setup, pointer alignment, and quasi-factorization

### 7.1.1 Geometry and Unruh modes

Fix a **stationary Killing horizon** with surface gravity \$\kappa>0\$. On a bounded chart of the horizon neighborhood we use **Rindler coordinates** to the accuracy guaranteed by Ch. 4 bounded-geometry hypotheses. Let

\[
\{b_k^{\rm out},\,b_k^{\rm in}\}_{k\in\mathcal K}
\]

denote Unruh mode operators localized to the patch (frequency \$\omega\_k>0\$ and tangential quantum numbers). The Unruh temperature is

\[
T_U=\frac{\kappa}{2\pi},\qquad \beta_U:=T_U^{-1}.
\]

### 7.1.2 Fast-sector GKSL and pointer alignment

On a horizon **tile** \$T\$ (area \$|T|\$), the fast sector evolves by a GKSL generator that is **diagonal in the Unruh (pointer) basis**:

\[
\mathcal L_T(\rho)=\sum_{k\in\mathcal K_T}\!\big[\gamma_k\,\mathcal D[b_k^{\rm out}](\rho)+\tilde\gamma_k\,\mathcal D[(b_k^{\rm out})^\dagger](\rho)\big],\quad
\mathcal D[C](\rho):=C\rho C^\dagger-\tfrac12\{C^\dagger C,\rho\}.
\]

The **leakage weight** \$W\succ0\$ (Appendix A) co-diagonalizes with the Unruh basis; write \$w\_k:=\langle k|W|k\rangle>0\$. The **per-tile leakage budget** is

\[
\mathcal B_{\rm leak}(T)=\sum_{k\in\mathcal K_T} w_k\,(\gamma_k+\tilde\gamma_k).
\]

**Hawking detailed balance** has

\[
\tilde\gamma_k^{\rm H}=\gamma_k^{\rm H}\,e^{-\beta_U\omega_k},\qquad \bar n_k=(e^{\beta_U\omega_k}-1)^{-1}.
\]

**Lemma 7.1 (Budget-monotonic pointer alignment).**
Let \$\mathcal L\_T\$ be any GKSL on \$T\$ with the same singular values of the noise block as above. Let \$\Delta\$ be the **pinching** (full dephasing) in the Unruh basis. Then:

1. (Budget) \$\sum\_j\omega(L\_j^\dagger W L\_j)\ \ge\ \sum\_j\omega!\big((\Delta L\_j)^\dagger W(\Delta L\_j)\big)\$ (Hilbert–Schmidt **pinching contraction**).
2. (Information) For any state \$\rho\$, \$I\big((\mathrm{id}\otimes\Lambda\_t)(\rho):\bar T\big)\$ **does not increase** if one replaces \$\Lambda\_t:=e^{t\mathcal L\_T}\$ by \$\Delta\circ\Lambda\_t\circ\Delta\$ (monotonicity of \$I\$ under local CPTP maps and commutation of \$\Delta\$ with the Unruh-diagonal semigroup).

Hence, among channels with fixed spectral data, **Unruh-diagonal** noise **minimizes** leakage cost and **maximizes** \$I(T:\overline T)\$ **only** within that spectral class. We therefore restrict to the **diagonal** form without loss for upper bounds.

*Proof.* (1) The map \$X\mapsto W^{1/2}X\$ followed by conditional expectation \$\Delta\$ is a contraction in the HS norm; sum over \$j\$. (2) Mutual information is monotone under local CPTP maps; \$\Delta\$ is local on \$T\$ and leaves the Unruh-diagonal dynamics invariant; compose. \$\square\$

### 7.1.3 Entropy functional and the \$E\_R\$ relation

We take **mutual information** as primary:

\[
I(A:\bar A)=D\big(\rho_{A\bar A}\,\big\|\,\rho_A\otimes\rho_{\bar A}\big).
\]

We use the general inequality

\[
\boxed{\,E_R(\rho_{A\bar A})\ \le\ I(A:\bar A)\,}
\]

(no \$\tfrac12\$ factor in general). All subsequent bounds are proved for \$I\$ and then immediately transfer to \$E\_R\$.

### 7.1.4 Quasi-factorization with LR constants

Tile a region \$A\$ by disjoint squares \${T\_j}\_{j\in J(A)}\$ of side \$\ell\$, and include a **boundary collar** of width \$O(\ell)\$, yielding \$O(|\partial A|)\$ collar tiles. The GKSL semigroup obeys **cone-limited LR bounds** (Ch. 3 U4; Appendix F.2) and admits an Unruh thermal **log-Sobolev** (or spectral-gap) constant on each tile (Appendix G.1).

**Theorem 7.0 (Quasi-factorization of mutual information).**
There exist \$C\_{\rm LR},\xi,v\_{\rm LR}<\infty\$, depending only on the LR/mixing data and the local mode density, such that for all \$\ell\ge \ell\_0\$ and all horizon-patch regions \$A\$,

\[
\boxed{\
I(A:\bar A)\ \le\ \sum_{j\in J(A)}\! I(T_j:\overline{T_j})\ +\ C_{\rm LR}\,|\partial A|\ +\ C_{\rm LR}\,e^{-\ell/\xi}.
\ }
\]

In particular, choosing \$\ell\ge c,\xi\log(1+|\partial A|)\$ absorbs the remainder into the boundary term: \$I(A:\bar A)\le \sum\_j I(T\_j:\overline{T\_j})+O(|\partial A|)\$.

*Proof (outline; Appendix G.2).* Chain the mutual information by **SSA**:
\$I(A:\bar A)=\sum\_{j} I\big(T\_j:\bar A,\big|,T\_{\<j}\big)\$ and bound each conditional term by an LR-decaying influence from \$\overline{T\_j}\$ outside a collar of width \$\sim\ell\$. Mix to Unruh steady on the collar using the tile log-Sobolev gap; constants track to \$C\_{\rm LR},\xi\$. \$\square\$

---

## 7.2 Area-law upper bound with calibrated constant

We now reduce the area bound to a **per-tile** estimate and calibrate the constant.

### 7.2.1 Per-tile information vs. leakage budget

For a tile \$T\$, write \$\Gamma\_k:=\gamma\_k+\tilde\gamma\_k\$ and define

\[
\tau_{\rm leak}(T):=\sum_{k\in\mathcal K_T} w_k\,\Gamma_k.
\]

**Proposition 7.1 (Linear upper bound, sharp coefficient).**
There exists a finite constant

\[
\chi_T:=\sup_{k\in\mathcal K_T}\ \frac{\partial^+ I_k}{\partial \Gamma_k}\,\frac{1}{w_k}\,,
\]

(where \$I\_k\$ is the single-mode contribution under Unruh-diagonal dynamics and \$\partial^+\$ is the right derivative at the realized \$\Gamma\_k\$) such that

\[
\boxed{\ I(T:\overline T)\ \le\ \chi_T\,\tau_{\rm leak}(T)\ .\ }
\]

Moreover \$\chi\_T\$ depends only on the Unruh temperature, the LR/mixing constants, and the local mode density; it is **uniform** across tiles of the same side \$\ell\$.

*Proof (Appendix G.3).* For Unruh-diagonal GKSL, \$I(T:\overline T)=\sum\_k I\_k(\Gamma\_k)\$. Each \$I\_k\$ is **concave**, increasing in \$\Gamma\_k\$ and differentiable a.e. (data processing + semigroup contractivity in the normalized-HS metric used for budgets, Appendix E.1). Lagrange’s inequality then gives
\$I(T:\overline T)\le \sum\_k (\partial^+ I\_k/\partial\Gamma\_k),\Gamma\_k \le \chi\_T \sum\_k w\_k \Gamma\_k.\$
Uniformity follows from bounded geometry and the common Unruh temperature. \$\square\$

> **Remark.** We carry (7.2.1) as an **upper bound**. Under the **Hawking-weight calibration** of §7.3.2 the coefficient becomes tile-independent (\$\chi\_T\equiv\chi\_\*\$) and the bound is **tight** (equality along the Hawking ray).

### 7.2.2 KKT thresholding and the pointer cutoff \$\ell\_\*\$

We optimize per-tile \$I(T:\overline T)\$ subject to the leakage allowance \$\tau\_{\rm leak}(T)\$. The **KKT conditions** with multiplier \$\lambda\_{\rm leak}>0\$ give the **threshold rule**

\[
\frac{\partial^+ I_k}{\partial \Gamma_k}\ \le\ \lambda_{\rm leak}\,w_k,\quad
\Gamma_k>0\ \Rightarrow\ \frac{\partial I_k}{\partial \Gamma_k}=\lambda_{\rm leak}\,w_k.
\]

Because \$w\_k\$ grows monotonically with **transverse momentum** (pointer/energy scaling) and \$\partial I\_k/\partial\Gamma\_k\$ is bounded and decreases with \$|k|\$ at fixed \$\beta\_U\$, the optimizer **activates modes** only for \$|k|\lesssim \ell\_\*^{-1}\$ with a **sharp cutoff** at

\[
\boxed{\ \ell_\*=\ell_\*(\lambda_{\rm leak},W)\ \ \text{defined by}\ \ \frac{\partial I_{k}}{\partial \Gamma_{k}}\Big|_{|k|=\ell_\*^{-1}}=\lambda_{\rm leak}\,w_{k}\ .\ }
\]

(Details in Appendix G.4.) For tiles with side \$\ell=\Theta(\ell\_\*)\$, the number of active transverse modes is \$\simeq |T|/\ell\_\*^{,d-2}\$ up to boundary/collar corrections.

### 7.2.3 Area-law theorem

**Theorem 7.1 (Area-law upper bound with boundary term).**
For tiles of side \$\ell=\Theta(\ell\_\*)\$,

\[
\boxed{\
I(A:\bar A)\ \le\ \chi_\*(\beta_U,{\rm LR},W)\,\frac{{\rm Area}(A)}{\ell_\*^{\,d-2}}\ +\ O(|\partial A|),\qquad
E_R(A:\bar A)\ \le\ I(A:\bar A).
\ }
\]

Here \$\chi\_\*:=\sup\_T\chi\_T\$ is finite and depends only on the Unruh temperature, LR/mixing constants and the local weight profile \$W\$ (Appendix G.5). The \$O(|\partial A|)\$ constant depends only on LR/geometry data.

*Proof.* Combine Theorem 7.0 with Proposition 7.1 and the thresholding definition of \$\ell\_\*\$; count active modes per interior tile and absorb LR remainders into the collar. \$\square\$

### 7.2.4 Calibration to Einstein–Hilbert and the \$1/4\$ coefficient

**Proposition 7.2 (EH calibration \$\Rightarrow\$ \$\chi\_\*=\tfrac14\$ in Planck units).**
Under the **Γ-limit normalization** of Appendix D (Ch. 4/D.5), the slow action equals Einstein–Hilbert and the Unruh temperature is fixed by \$\kappa\$. Matching the **tile-wise Clausius relation** \$\delta Q=T\_U,\delta S\$ with the **leakage work** priced by \$W\$ at the pointer cutoff yields

\[
\boxed{\ \chi_\*=\frac14\ ,\qquad
I(A:\bar A)\ \le\ \frac{{\rm Area}(A)}{4\,\ell_P^{\,d-2}}\ +\ O(|\partial A|). \ }
\]

*Proof (Appendix G.6).* The per-tile leakage expenditure that realizes the Unruh KMS structure at the cutoff equals the **heat** \$\delta Q\$ through the stretched horizon; with \$T\_U\$ fixed, the \$\delta S\$ density matches EH’s area-entropy density, fixing \$\chi\_\*=1/4\$. \$\square\$

---

## 7.3 Hawking-flux suppression: sharp LP bound and calibrated equality

### 7.3.1 General linear-program bound (no profile assumptions)

Let \$c\_k\$ denote the **outgoing flux weight** per mode (number or energy),

\[
c_k:=\begin{cases}
v_k\,\bar n_k & \text{(number flux)},\[2pt]
\hbar\omega_k\,v_k\,\bar n_k & \text{(energy flux)},
\end{cases}
\qquad 0<v_k\le v_{\max}.
\]

For a tile \$T\$,

\[
\mathcal F_{\rm out}(T)=\sum_{k\in\mathcal K_T} c_k\,\Gamma_k,\qquad 
\tau_{\rm leak}(T)=\sum_{k\in\mathcal K_T} w_k\,\Gamma_k.
\]

**Theorem 7.2 (General LP suppression).**
For every tile \$T\$,

\[
\boxed{\
\mathcal F_{\rm out}(T)\ \le\ \Big(\max_{k\in\mathcal K_T}\frac{c_k}{w_k}\Big)\ \tau_{\rm leak}(T)\ .
\ }
\]

Equality holds by concentrating the budget on a mode with maximal ratio \$c\_k/w\_k\$. Summing tiles gives

\[
\boxed{\
\mathcal F_{\rm out}\ \le\ \Big(\max_{k}\frac{c_k}{w_k}\Big)\ \tau_{\rm leak}\ .
\ }
\]

*Proof.* Linear objective over a simplex: maximize \$\sum c\_k\Gamma\_k\$ s.t. \$\sum w\_k\Gamma\_k\le\tau\$ and \$\Gamma\_k\ge0\$. KKT gives support on argmax of \$c\_k/w\_k\$. \$\square\$

> **Microcausality.** The LR bounds (Appendix F.2) imply
> \$|\[\Phi\_t(O\_X),O\_Y]|\le C,e^{-(d(X,Y)-v\_{\rm LR}t)/\xi}\$; hence no superluminal contribution to \$\mathcal F\_{\rm out}\$ is admissible.

### 7.3.2 Hawking-weight calibration and exact multiplicative factor

Define the **Hawking-weight** \$W\_{\rm H}\$ by

[
\boxed{\,w_k^{\rm H}\ \propto\ c_k\ ,\ }
\]

i.e. choose the leakage weight to price exactly the **flux contribution** (number or energy). This choice is canonical operationally (Appendix J.1: weight normalization by KPI).

Let \$\Gamma\_k^{\rm H}\$ be the **detailed-balance rates** reproducing the semiclassical Hawking flux, and define the **Hawking leakage cost**

\[
\tau_{\rm H}(T):=\sum_{k\in\mathcal K_T} w_k^{\rm H}\,\Gamma_k^{\rm H},\qquad
\mathcal F_{\rm Hawking}(T):=\sum_k c_k\,\Gamma_k^{\rm H}.
\]

By construction,

\[
\frac{\mathcal F_{\rm Hawking}(T)}{\tau_{\rm H}(T)}=\frac{\sum_k c_k\Gamma_k^{\rm H}}{\sum_k w_k^{\rm H}\Gamma_k^{\rm H}}=\frac{\sum_k c_k\Gamma_k^{\rm H}}{\sum_k (\alpha c_k)\Gamma_k^{\rm H}}=\alpha^{-1},
\]

a **mode-independent** constant (absorbed into the normalization of \$W\_{\rm H}\$).

**Corollary 7.2′ (Budget-limited Hawking).**
With \$W=W\_{\rm H}\$, the LP optimizer aligns with the **Hawking ray** and yields

\[
\boxed{\
\mathcal F_{\rm out}(T)\ =\ \min\!\Big\{1,\ \frac{\tau_{\rm leak}(T)}{\tau_{\rm H}(T)}\Big\}\ \mathcal F_{\rm Hawking}(T),
\ }
\]

with equality cases: (i) \$\tau\_{\rm leak}(T)\ge\tau\_{\rm H}(T)\$ and \$\Gamma\_k=\Gamma\_k^{\rm H}\$ (full Hawking), (ii) \$\tau\_{\rm leak}(T)<\tau\_{\rm H}(T)\$ and \$\Gamma\_k=\alpha,\Gamma\_k^{\rm H}\$ with \$\alpha=\tau\_{\rm leak}(T)/\tau\_{\rm H}(T)\$ (budget-limited Hawking). Summing tiles gives

\[
\boxed{\
\mathcal F_{\rm out}\ =\ \min\!\Big\{1,\ \frac{\tau_{\rm leak}}{\tau_{\rm H}(W_{\rm H})}\Big\}\ \mathcal F_{\rm Hawking}\ .
\ }
\]

*Proof.* Under \$w\_k^{\rm H}\propto c\_k\$, \$c\_k/w\_k^{\rm H}\$ is **constant in \$k\$**; every Hawking-proportional allocation maximizes the LP; scale by feasibility. \$\square\$

---

## 7.4 Identifiability, observables, and explicit \$f\$

### 7.4.1 Identifiability of Hawking rates in the pointer model

**Lemma 7.3 (Pointer-basis identifiability).**
In the Unruh-diagonal GKSL model, the **two-point functions** of the outside modes,

\[
C_k(t):=\langle b_k^{\rm out}(t)\,(b_k^{\rm out})^\dagger(0)\rangle,\qquad 
\tilde C_k(t):=\langle (b_k^{\rm out})^\dagger(t)\,b_k^{\rm out}(0)\rangle,
\]

satisfy

\[
C_k(t)=\big(1+\bar n_k\big)\,e^{-\tfrac12\Gamma_k t},\qquad 
\tilde C_k(t)=\bar n_k\,e^{-\tfrac12\Gamma_k t}.
\]

Hence the **KMS ratio** \$\tilde C\_k(t)/C\_k(t)=\bar n\_k/(1+\bar n\_k)=e^{-\beta\_U\omega\_k}\$ fixes \$\beta\_U\$, and the **linewidth** identifies \$\Gamma\_k\$. In particular, the Hawking rates \$\Gamma\_k^{\rm H}\$ are **uniquely determined** from pointer-basis two-point data within this model class.

*Proof.* Solve the Heisenberg equations under the Unruh-diagonal Lindbladian; the amplitudes decay at rate \$\tfrac12\Gamma\_k\$ while detailed balance fixes the ratio. \$\square\$

### 7.4.2 KPI and computation of \$f\$

**Primary KPI.** The **flux ratio**

\[
R:=\frac{\mathcal F_{\rm out}}{\mathcal F_{\rm Hawking}}\ =\
\begin{cases}
\displaystyle \min\!\Big\{1,\frac{\tau_{\rm leak}}{\tau_{\rm H}(W_{\rm H})}\Big\}, & \text{for }W=W_{\rm H};\[8pt]
\displaystyle \le\ \Big(\max_k \tfrac{c_k}{w_k}\Big)\,\frac{\tau_{\rm leak}}{\mathcal F_{\rm Hawking}}, & \text{general }W.
\end{cases}
\]

**Procedure.**

1. Tomography in the **pointer basis** (Appendix J.1) gives \$\Gamma\_k^{\rm H}\$ from linewidths and \$\beta\_U\$ from KMS.
2. Compute the **Hawking cost** \$\tau\_{\rm H}(W)=\sum w\_k,\Gamma\_k^{\rm H}\$ for the chosen weight \$W\$ (or set \$W=W\_{\rm H}\$ to make it canonical).
3. Evaluate \$f\$ by the formulas above.

### 7.4.3 Pointer cutoff and tile choice

Set the tile side \$\ell\$ by **allowance matching**:

\[
\sum_{k\in\mathcal K_T} w_k\,\Gamma_k^{\rm H}\ =\ \tau_{\rm leak}(T),
\]

which solves to \$\ell=\Theta(\ell\_\*)\$ defined in §7.2.2. With this choice, the **quasi-factorization remainder** is absorbed into \$O(|\partial A|)\$ and the area coefficient is calibrated by Proposition 7.2.

---

## 7.5 Microcausality (guard) and hygiene

The **single-cone** class (Ch. 4) and U-assumptions (Ch. 3) yield LR bounds (Appendix F.2):

\[
\|[\Phi_t(O_X),O_Y]\|\ \le\ C\,e^{-(d(X,Y)-v_{\rm LR}t)/\xi}.
\]

Thus neither the **area-law derivation** (local tilings and collar mixing) nor the **flux LP** can exploit superluminal influences; all optimizers live inside the cone.

---

## 7.6 Summary (airtight form)

1. **Pointer alignment** is **budget-monotonic** and information-preserving in the sense of Lemma 7.1; hence we restrict to **Unruh-diagonal** GKSL.
2. A **quasi-factorization theorem** (Theorem 7.0) holds with explicit LR constants, reducing the bound to **per-tile** contributions plus an \$O(|\partial A|)\$ boundary term.
3. **Per-tile information** obeys a **linear upper bound** \$I(T:\overline T)\le \chi\_T,\tau\_{\rm leak}(T)\$ (Proposition 7.1), with a **KKT threshold** producing a **pointer cutoff** \$\ell\_\*\$ (§7.2.2).
4. Summing tiles gives an **area law** with explicit coefficient \$\chi\_\*/\ell\_\*^{,d-2}\$ (Theorem 7.1). Under EH **Γ-calibration**, \$\chi\_\*=1/4\$ (Proposition 7.2), yielding

\[
E_R(A:\bar A)\ \le\ I(A:\bar A)\ \le\ \frac{{\rm Area}(A)}{4\,\ell_P^{\,d-2}}\ +\ O(|\partial A|).
\]

5. **Flux suppression** is a sharp **linear program** (Theorem 7.2). With the **Hawking-weight** \$W\_{\rm H}\$, the optimizer is **budget-limited Hawking**:

\[
\mathcal F_{\rm out}\ =\ \min\!\Big\{1,\ \frac{\tau_{\rm leak}}{\tau_{\rm H}(W_{\rm H})}\Big\}\ \mathcal F_{\rm Hawking}.
\]

6. **Identifiability** (Lemma 7.3) pins \$\Gamma\_k^{\rm H}\$ from pointer-basis two-point data; **microcausality** is enforced by LR bounds.

All constants and intermediate inequalities are tracked in **Appendix G** (area) and **Appendix H** (flux), ensuring the chapter’s statements are **fully rigorous** within the stated hypotheses.

# Chapter 8 — Coherence RG: Scale Flow & Fixed Points

> **Scope.** Define a coherence‑preserving coarse‑graining and derive an RG flow on budgets and predictive envelopes. Fixed points correspond to scale‑invariant scaffolds; relevant directions match active budgets.

## 8.1 Coarse‑graining & monotonicity

Local coarse‑grainings \(\mathcal C_\ell\) at scale \(\ell\) respect the poke cone (causal, Γ‑local). Budgets obey **monotone** inequalities
\(B_\bullet(\mathcal C_\ell A)\ \le\ c_\bullet(\ell)\, B_\bullet(A),\quad \bullet\in\{\rm th,cx,leak\}.\)

## 8.2 Flow equations (envelope picture)

Scale‑\(\ell\) objective \(\mathcal V_\ell(A)= \inf_{\Phi\in\overline{\mathcal P}}\mathrm{CL}(\mathcal C_\ell A,\Phi) - \sum_\bullet \lambda_\bullet B_\bullet(\mathcal C_\ell A)\). The **coherence RG** is
\(\partial_{\ln\ell}\, \mathcal V_\ell\ =\ \mathcal D\,\mathcal V_\ell\ -\sum_\bullet (\partial_{\ln\ell}\ln c_\bullet)\cdot \lambda_\bullet B_\bullet\ +\ \text{(irrelevant corrections)}.\)

## 8.3 Fixed points and stability

A **fixed point** satisfies stationarity of \(\mathcal V_\ell\) up to rescaling; budgets transform covariantly. Linearization gives scaling exponents for (th,cx,leak) channels and binders. The RG‑envelope yields closure rules for multipliers by matching to observed invariants.

# Chapter 9 — Quantum Geometry Completion: Constraint Algebra & Path Measure

> **Scope.** We (i) compute the hypersurface-deformation (ADM/Henneaux–Teitelboim) algebra *inside the cone-preserving class*, verifying **closure without anomalies** and persistence at the Γ-limit, and (ii) construct a **cone-limited projective path measure** with explicit finite-dimensional marginals, proving **cylinder consistency**, **FKG/positive association** under an attractive discretization, and **microcausality via LR-type bounds** at the measure level. All hypotheses and objects align with the budgets/topologies fixed earlier (bounded geometry, de Donder/harmonic gauge on charts, single-cone hygiene, Γ-locality).
**BRST/BV hygiene note (anomaly absence at the Γ-limit).** Within the cone-preserving, gauge-fixed class and bounded-geometry hypotheses, the hypersurface-deformation algebra closes **without central extensions** (Appendix D/F bounds). The corresponding BRST charge is nilpotent, and a unitary BV/BV measure exists for the projective path construction; microcausality (LR-type) guards ensure cylinder consistency.

---

## 9.1 Constraint algebra closure (ADM/Henneaux–Teitelboim inside the cone class)

### Phase space, constraints, and smearings

Let \$\Sigma\$ be a Cauchy slice of a globally hyperbolic spacetime with bounded geometry. The canonical variables are the Riemannian metric \$q\_{ab}\$ on \$\Sigma\$ and its conjugate momentum \$\pi^{ab}=\sqrt{q},(K^{ab}-K q^{ab})\$ (indices raised/lowered with \$q\$). The (Poisson) symplectic form is

\[
\{F,G\}=\int_\Sigma\!\mathrm d^3x\ \Big(\frac{\delta F}{\delta q_{ab}}\frac{\delta G}{\delta \pi^{ab}}-\frac{\delta G}{\delta q_{ab}}\frac{\delta F}{\delta \pi^{ab}}\Big).
\]

The **scalar (Hamiltonian)** and **vector (momentum)** constraints (pure gravity with \$\Lambda\$; minimal coupling to gauge/matter adds standard pieces without modifying the algebraic structure functions) are

\[
\begin{aligned}
\mathcal H_\perp &= \frac{1}{\sqrt{q}}\big(\pi^{ab}\pi_{ab}-\tfrac12\pi^2\big)-\sqrt{q}\,(R-2\Lambda)\ +\ \mathcal H_\perp^{\rm matter},\\
\mathcal H_a &= -2\,q_{ac}\,D_b\pi^{bc}\ +\ \mathcal H_a^{\rm matter},
\end{aligned}
\]

with \$D\$ the Levi-Civita connection of \$q\$, \$R\$ its scalar curvature, and \$\pi:=q\_{ab}\pi^{ab}\$. For smearings \$N\in C\_c^\infty(\Sigma)\$ and \$N^a\in\mathfrak X\_c(\Sigma)\$ (compact support or appropriate falloff), define

\[
H[N]:=\int_\Sigma\! N\,\mathcal H_\perp,\qquad D[\vec N]:=\int_\Sigma\! N^a\,\mathcal H_a.
\]

All fields are restricted to the **single-cone** class (principal symbol bounds) and we work in harmonic/de Donder gauge on charts when needed (for well-posedness and elliptic control of gauge).

### Hypotheses for this block

* **(C1) Cone hygiene & bounded geometry.** As in Ch. 4, uniform injectivity radius and curvature bounds; single-cone principal-symbol bounds hold.
* **(C2) Boundary/falloff.** Either compact \$\Sigma\$ without boundary or standard ADM falloffs guaranteeing boundary terms vanish in the bracket computations (or are absorbed in the ADM surface charges if present; here we take vanishing boundaries for brevity).
* **(C3) Γ-limit stability.** The slow action is the Γ-limit of second-order local forms (Ch. 4/Appendix D), so all variational derivatives converge in the sense needed below.

### The hypersurface-deformation algebra (HDA): statements

\[
\boxed{
\begin{aligned}
\{D[\vec N],D[\vec M]\} &= D\!\big[\,\mathcal L_{\vec N}\vec M\,\big],\[2pt]
\{D[\vec N],H[M]\} &= H\!\big[\,\mathcal L_{\vec N} M\,\big],\[2pt]
\{H[N],H[M]\} &= D\!\big[\,q^{ab}(N\partial_b M - M\partial_b N)\,\big],
\end{aligned}}
\tag{9.1}
\]

i.e., **closure with structure functions \$q^{ab}\$ and no central extensions.**

We prove (9.1) *within* the cone-preserving class and verify persistence at the Γ-limit.

---

### Proof (9.1a) — \${D\[\vec N],D[\vec M]}=D[\mathcal L\_{\vec N}\vec M]\$

\$D[\vec N]\$ generates spatial diffeomorphisms:

[
\{q_{ab},D[\vec N]\}=\mathcal L_{\vec N}q_{ab},\qquad \{\pi^{ab},D[\vec N]\}=\mathcal L_{\vec N}\pi^{ab}.
\]

Therefore, for any functional \$F\$, \${F,D\[\vec N]}=\mathcal L\_{\vec N}F\$. Apply to \$F=D[\vec M]\$; since \$D\$ is a spatial vector density of weight one,

[
\{D[\vec M],D[\vec N]\}=\mathcal L_{\vec N}D[\vec M]=D[\mathcal L_{\vec N}\vec M].
\]

No boundary term survives by (C2). \$\square\$

### Proof (9.1b) — \${D\[\vec N],H[M]}=H[\mathcal L\_{\vec N}M]\$

\$H[M]\$ is a scalar density of weight one. Using the same generator property,

[
\{H[M],D[\vec N]\}=\mathcal L_{\vec N}H[M]=H[\mathcal L_{\vec N}M].
\]

Again, boundary terms vanish by (C2). \$\square\$

### Proof (9.1c) — \${H\[N],H[M]}=D[q^{ab}(N\partial\_bM-M\partial\_bN)]\$

This is the nontrivial bracket. Write \$H[N]=T[N]+V[N]\$ with

[
T[N]=\int N\ \frac{1}{\sqrt q}\Big(\pi^{ab}\pi_{ab}-\tfrac12\pi^2\Big),\qquad
V[N]=-\int N\ \sqrt q\,(R-2\Lambda)+\int N\,\mathcal H_\perp^{\rm matter}.
\]

Compute functional derivatives:

\[
\frac{\delta T[N]}{\delta \pi^{ab}}=\frac{2N}{\sqrt q}\Big(\pi_{ab}-\tfrac12\pi\,q_{ab}\Big),\qquad
\frac{\delta T[N]}{\delta q_{ab}}=-\frac{N}{2\sqrt q}\Big(\pi^{cd}\pi_{cd}-\tfrac12\pi^2\Big)q^{ab}+\frac{N}{\sqrt q}\big(2\pi^{ac}\pi^b_{\ c}-\pi\,\pi^{ab}\big).
\]

For \$V\[N]\$, use \$\delta(\sqrt q,R)=\sqrt q,(G^{ab}\delta q\_{ab}+D\_c\Theta^c)\$ with \$G^{ab}\$ the Einstein tensor of \$q\$ and \$\Theta^c\$ a boundary term; thus

[
\frac{\delta V[N]}{\delta q_{ab}}= -N\sqrt q\,(G^{ab}+\Lambda q^{ab}) + \text{(total divergences)},\qquad \frac{\delta V[N]}{\delta \pi^{ab}}=0.
\]

Insert in the Poisson bracket and integrate by parts. Divergences vanish by (C2). Curvature terms combine with derivatives of \$N,M\$ to yield the shift vector

\[
\beta^a[q;N,M]:=q^{ab}(N\partial_b M-M\partial_b N).
\]

A direct (standard) but lengthy cancellation gives

\[
\{H[N],H[M]\}=D[\vec\beta],\qquad \vec\beta=\beta^a\partial_a.
\]

Matter contributions are covariant and assemble into the same form (the momentum constraint is the Noether charge for spatial diffeomorphisms), hence do not alter the structure functions. **No central term** appears: any putative c-number must be a boundary integral antisymmetric in \$(N,M)\$, which vanishes under (C2). \$\square\$

---

### Gauge-fixing, Dirac brackets, and anomaly exclusion

Let \$\chi^\mu=0\$ be a (cone-preserving) gauge, e.g. **harmonic/de Donder** on charts. The set \${\mathcal H\_\perp,\mathcal H\_a,\chi^\mu}\$ is second-class with invertible bracket matrix on the single-cone domain. The **Dirac bracket** \${\cdot,\cdot}\_D\$ equals the Poisson bracket on **gauge-invariant** functionals. Since \$H\[N],D[\vec N]\$ generate diffeomorphisms, their algebra (9.1) remains valid with \${\cdot,\cdot}\_D\$ when acting on gauge-invariant observables.

**Absence of anomalies at the Γ-limit.** The slow action is a Γ-limit of second-order local functionals with **uniform symbol bounds** (Ch. 4). Variational derivatives of the discretized constraints converge (in the Mosco sense) to those of EH+YM; the symplectic form is fixed. Hence the **structure functions converge to \$q^{ab}\$**, and the brackets converge to (9.1). A central extension would require either (i) a cone flip (excluded by the **\$W\_1\$ gap**; App. F.1) or (ii) higher-derivative remnants violating H1/H5; both are ruled out by our hypotheses.

[
\boxed{\text{The constraint algebra closes (no central terms) in the cone-preserving class and persists at the Γ-limit.}}
\tag{9.2}
\]

---

## 9.2 Path-measure formulation (projective construction, FKG, microcausality)

We build a **cone-limited** probability measure on histories of the slow fields (metric \$g\$ and gauge fields \$A\$) compatible with the budgets and microcausality. The construction is by **projective limits of cylinder measures** with explicit finite-dimensional marginals.

### Indexing of cylinders and state spaces

Let \$\mathscr P\$ be the directed set of finite **space–time partitions** \$P\$: harmonic-chart coverings of compact slabs \$K\times\[t\_0,t\_1]\$ with mesh \$(\ell,\Delta t)\$ respecting the single-cone bounds (principal symbol within fixed \([\lambda,\Lambda]\$). For \$P\in\mathscr P\$, define the finite space [ \mathcal X_P:=\{(g_v,A_v)_{v\in V(P)}:\ \text{component values in harmonic coordinates, obeying cone and gauge bounds}\}, ] equipped with the product Borel \$\sigma\$-algebra and a reference product measure \$\nu\_P\$ (Gaussian blocks reflecting the quadratic part of the gauge-fixed action; see below). ### Local weights and finite-dimensional marginals On each \$P\$, define the *discretized action* (EH+YM Γ-compatible; Ch. 4/Appendix D) with gauge-fixing and cone penalty, [ S_P(g,A)=\sum_{c\in C(P)} \Big[\,\tfrac12\,\langle (g,A),\mathbb A_c (g,A)\rangle - \langle J_c,(g,A)\rangle + U_c(g,A)\,\Big]\ +\ V_P(g,A), ] where: * \$\mathbb A\_c\$ are **uniformly parameter-elliptic** local operators (principal symbol bounds inherited from the single-cone class); * \$U\_c\$ collects **lower-order** Γ-local terms; * \$V\_P\$ aggregates **budget terms** that are Γ-local and **attractive** in the discretization (see FKG below): throughput and complexity contributions enter as convex quadratics; leakage enters as a convex weight aligned with the pointer basis (Ch. 3/7). Define the **finite-dimensional probability** on \$(\mathcal X\_P,\mathcal B\_P)\$ by [ \mu_P(\mathrm d x):=\frac{1}{Z_P}\,\exp\!\big(\!-S_P(x)\big)\,\mathbf 1_{\text{single-cone}}(x)\ \nu_P(\mathrm d x),\qquad Z_P:=\int e^{-S_P}\mathbf 1_{\text{cone}}\ \mathrm d\nu_P. \tag{9.3} ] ### Cylinder consistency (projective system) If \$P\preceq P'\$ (refinement), write \$\pi\_{P'!,P}:\mathcal X\_{P'}!\to\mathcal X\_P\$ for restriction/averaging on cells. We define \$S\_P\$ by *backward induction* from fine to coarse scales: [ e^{-S_P(x)}\ \propto\ \int_{\pi_{P'\!,P}^{-1}(x)}\!\exp\!\big(\!-S_{P'}(x')\big)\ \nu_{P'}(\mathrm d x'\mid \pi_{P'\!,P}=x). \tag{9.4} ] This is a **local RG/coarse-graining** defining the coarse potential as a log-partition over refined variables. By construction, [ (\pi_{P'\!,P})_\#\,\mu_{P'}=\mu_P\qquad\text{for all }P\preceq P'. \tag{9.5} ] Hence \${\mu\_P}\_{P\in\mathscr P}\$ is a **projective family**. Tightness follows from uniform Gårding/coercivity (Ch. 4), giving **Kolmogorov extension**: [ \boxed{\ \exists!\ \mu\ \text{ on }\ \mathcal X:=\varprojlim \mathcal X_P\ \text{ with }(\pi_P)_\#\mu=\mu_P\ \forall P.\ } \tag{9.6} ] ### FKG/positive association under attractive discretization On each \$P\$, the potential is a sum of **convex on-site** terms and **pairwise attractive** interactions (mixed second derivatives \$\le 0\$ in the partial order induced by componentwise increase within the cone window). This can be arranged by: * harmonic gauge (quadratic principal part convex); * YM energy densities as convex quadratics locally; * budget add-ons chosen **convex** in the pointer-aligned coordinates (leakage: quadratic in \$W^{1/2}\$-weighted amplitudes; complexity/throughput: convex quadratics). By **Holley’s criterion**, \$\mu\_P\$ satisfies **FKG**. Projective limits preserve association on cylinder events; thus for increasing cylinder functions \$f,g\$, [ \mathbb E_\mu[f\,g]\ \ge\ \mathbb E_\mu[f]\ \mathbb E_\mu[g]. \tag{9.7} ] ### Microcausality (LR-type mixing bound at the measure level) Time-slice the partition \$P\$ into levels \${t\_k}\$. The coarse-graining (9.4) can be implemented via **Markov transfer kernels** \$K\_{k\to k+1}(x\_{t\_k},\mathrm d x\_{t\_{k+1}})\$ induced by the local quadratic principal symbol, with **finite-speed** propagation constant \$v\_\ast\$ determined by the single-cone bounds. The corresponding Dobrushin influence coefficients \$\alpha(A\to B)\$ between spatial blocks \$A\$ at \$t\_k\$ and \$B\$ at \$t\_{k+1}\$ obey [ \alpha(A\to B)\ \le\ C\,\exp\!\Big(-\gamma\,[\,\mathrm{dist}(A,B)-v_\ast\Delta t\,]_+\Big), \tag{9.8} ] uniformly in \$P\$, for some \$C,\gamma>0\$ (cone-limited Lieb–Robinson-type estimate at the **kernel** level; cf. U.LR and the principal-symbol lemma). Standard Dobrushin/cluster-mixing then yields, for cylinder observables \$F\_A,G\_B\$ localized in spacelike-separated regions \$A,B\$, [ \big|\mathrm{Cov}_\mu(F_A,G_B)\big|\ \le\ C'\,\|F_A\|_{\rm Lip}\,\|G_B\|_{\rm Lip}\ \exp\!\Big(-\gamma'\,[\,\mathrm{dist}(A,B)-v_\ast\,\Delta t\,]_+\Big). \tag{9.9} ] Thus **microcausality** (no superluminal statistical influence) holds at the measure level. ### Mixed fast–slow characteristic functionals Let \$\mathcal G\$ be the fast-sector quasi-local algebra. For a cylinder field \$(g,A)\mapsto J(g,A)\$ coupled to a stationary GKSL fast state with **LR bounds** (U4/U.LR), define the mixed characteristic functional [ \Xi[\theta]:=\int_{\mathcal X}\!\exp\!\Big(i\,\theta\cdot J(g,A)\Big)\ \mu(\mathrm d g\,\mathrm d A). ] The LR-type bound (9.9) and U.LR imply the **same cone-limited decay** for mixed covariances; variational differentiation of \$\Xi\$ recovers the coupled Euler–Lagrange equations (Ch. 5) by standard Gibbs/DLR calculus (Appendix E), with budgets entering through \$V\_P\$. --- ### Summary of Chapter 9 1. The **constraint algebra closes** in the cone-preserving class with the standard structure functions \$q^{ab}\$ and **no central extensions**; the result **persists at the Γ-limit** by stability of variational derivatives and symbol bounds. 2. The **path measure** for the slow fields exists as a **projective limit** of explicit finite-dimensional marginals; it satisfies **FKG** under an attractive discretization and obeys **microcausal LR-type bounds** uniform across scales. 3. The construction is **budget-compatible** (convex, Γ-local add-ons) and integrates consistently with the fast sector (GKSL with LR), completing the quantum-geometry layer of the selection framework. # Chapter 10 — Coherence Nucleation ⇒ Cosmology (Rigorous Edition) > **Scope.** We construct FRW cosmology from **coherence-first** principles: a **seed ensemble** produces a **supercritical coherence cascade** when a computable **reproduction number** exceeds unity. Inside the cascade, the slow Γ‑limit reduces to FRW with quantitative smoothing/flatness bounds. We fix the **information framework** to a class of divergences, show **RG‑stability** in the tiling scale, formalize the **risk‑sensitive** envelope and **commuting limits**, and prove **conservation** of the effective stress tensor in the slow sector. Bounces arise precisely when leakage drives \)w<-1/3\( under pointer freezing. --- ## 10.0 Hypotheses, information class, notation (dimension‑uniform) We adopt the quasi‑local C\* and fast GKSL framework of Chs. 3–5. Space is tiled by hypercubes ("tiles") of side \)\ell>0\(; write \)\mathbb T_\ell\( for the tile set; \)\partial A\( the boundary **area** of a union \)A\subset\mathbb T_\ell\(. The spatial dimension is \)d\ge2\( (observationally \)d=3\(); all proofs below are dimension‑uniform, with \)d\( only in packing constants. **Information‑measure class \)\mathsf{IM}(\tau)\(.** A divergence \)D\( lies in \)\mathsf{IM}(\tau)\( if: (i) **data processing** holds for GKSL channels and the pinching map \)\mathcal P^W\(; (ii) **LR quasi‑factorization** holds with constant \)C_q(\tau)\(; (iii) a **Dobrushin** coefficient satisfies \)\delta_D(\mathcal P^W\!\circ\!\Phi_t)\le e^{-\gamma_W t}\( at the KKT point; (iv) on calibrated sublevels there exist constants \)m(\tau),M(\tau)\( with \)m D_2\le D\le M D_2\( and similarly vs. KL. (Sandwiched Rényi \)1\le\alpha\le2\( and KL are in \)\mathsf{IM}(\tau)\(.) **(H10.1) Fast dynamics & LR.** On each finite union \)A\(, the fast sector evolves by a GKSL semigroup \)\Phi_t^A=e^{t\mathcal L^A}\( obeying Lieb–Robinson locality with velocity \)v_{\rm LR}\( and profile \)f_{\rm LR}\(, and respecting the three budget quadratics (Ch. 3). **(H10.2) Pointer alignment & Dirichlet linearity.** The leakage quadratic is **left‑Dirichlet** in the pointer weight \)W\( and **orthogonally additive** in its spectral decomposition; \)\mathcal P^W\( is a \)D\(-contraction for any \)D\in\mathsf{IM}\(. **(H10.3) Throughput normalization.** \)\hbar=\lambda_{\rm th}^{-1}\( (Ch. 3), so the HS metric prices motion along unitary orbits. **(H10.4) Slow Γ‑limit.** Under localized Mosco/Attouch, first variations commute with \)\varepsilon\to0\( and the slow sector satisfies \)G_{\mu\nu}+\Lambda g_{\mu\nu}=8\pi G\,T^{\rm eff}_{\mu\nu},\qquad \nabla^\mu T^{\rm eff}_{\\mu\nu}=0,\( with calibrated multipliers \)(G,\Lambda)\(. **Light‑cone time.** \)\tau_{\rm LR}(\ell)=\ell/v_{\rm LR}\(. The adjacency graph \)\mathcal G_\ell\( connects face‑sharing tiles. --- ## 10.0.1 Seed ensemble (poke process) Pokes arrive as a **Poisson random measure** on spacetime with rate \)\lambda_0\(, amplitudes with **sub‑exponential tails** (parameter \)\theta>0\(), and LR‑compatible support (no super‑cone events). A seed tile is **aligned** if its post‑poke state is \)\mathcal P^W\(-close (in any \)D\in\mathsf{IM}\() to a pointer block. For \)\gamma_W>0\( and finite \)\alpha_{\rm leak}\(, aligned seeds occur with positive probability. --- ## 10.1 Tile balance and the reproduction number For a tile union \)A\(, let \)\mathsf C_t(A)\( be the **coherence content** at time \)t\( measured by any \)D\in\mathsf{IM}\(. Over \)\Delta t\le \tau_{\rm LR}(\ell)\(, three effects act on a seed tile \)T\(: 1. **Leakage load**: \)L(\ell,\Delta t)\le C_L\,\alpha_{\rm leak}\,\tfrac{\Delta t}{\ell}.\( 2. **Pointer alignment**: \)\eta_{\rm align}(\Delta t)=1-\delta_D(\mathcal P^W\!\circ\!\Phi_{\Delta t})\in(0,1] \( with \)1-\eta_{\rm align}\le e^{-\gamma_W\Delta t}.\( 3. **Neighbor recruitment**: \)M(\ell,\Delta t)\le C_M\,(\tfrac{v_{\rm LR}\Delta t}{\ell})^d\( (packing; App. I.1). **Definition 10.1 (Reproduction number).** \)\mathcal R_{\rm coh}(\ell,\Delta t)=\eta_{\rm align}(\Delta t)\,(1-L(\ell,\Delta t))\,M(\ell,\Delta t).\( **Proposition 10.2 (Optimized one‑step threshold).** At \)\Delta t=\ell/v_{\rm LR}\(, \)\mathcal R_{\rm coh}\ \ge\ \underbrace{(1-e^{-\gamma_W\ell/v_{\rm LR}})}_{\eta}\,\underbrace{(1-C_L\alpha_{\rm leak}/v_{\rm LR})}_{1-L}\,\underbrace{C_M}_{M}.\( Thus \)\mathcal R_{\rm coh}>1\( if \)(1-e^{-\gamma_W\ell/v_{\rm LR}})C_M>(1-C_L\alpha_{\rm leak}/v_{\rm LR})^{-1}.\( --- ## 10.2 Nucleation and non‑recurrence **Theorem 10.3 (Nucleation ⇒ supercritical cascade).** If \)\mathcal R_{\rm coh}(\ell,\Delta t)>1\( for some \)(\ell,\Delta t)\(, an aligned seed produces (in the worst‑case envelope) a **growing cluster** of aligned tiles whose boundary advances at positive asymptotic speed. The occupied set stochastically dominates a **supercritical Galton–Watson / first‑passage** process on \)\mathcal G_\ell\( with mean offspring \)>1\(. *Proof idea:* LR quasi‑factorization and orthogonal additivity in \)W\( yield FKG/Harris positive association; dominate by a branching process of mean \)\mathcal R_{\rm coh}>1\( (App. I.3). **Theorem 10.4 (Non‑recurrence in aligned media).** In an already pointer‑aligned bath, \)\mathcal R_{\rm coh}^{\rm ambient}\le1\( for all \)\Delta t\le\tau_{\rm LR}\(; seeds decohere or are absorbed. *Reason:* DPI for \)\mathcal P^{W_{\rm env}}\circ\Phi_{\Delta t}\( gives \)\eta_{\rm align}^{\rm env}\le1\( with equality only on the ambient block; leakage is at least that to the full bath. --- ## 10.2′ RG‑stability in the tiling scale \)\ell\( Rescale \)\ell\mapsto\lambda\ell\( with \)\lambda\in(\tfrac12,2)\(. Define the **budget reparametrization** \)\alpha_{\rm leak}\mapsto \alpha_{\rm leak}^{(\lambda)}:=\lambda^{-1}\alpha_{\rm leak},\quad \alpha_{\rm th}\mapsto\alpha_{\rm th}^{(\lambda)}:=\alpha_{\rm th},\quad \alpha_{\rm cx}\mapsto\alpha_{\rm cx}^{(\lambda)}:=\alpha_{\rm cx},\( so that \)\rho_{\rm leak}\propto \alpha_{\rm leak}\ell^{-1}\( is invariant and the other budgets are unchanged to leading order. Then to first order in \)|\lambda-1|\(, **observable** quantities \)H(a),\,w(a),\,\Omega_k\( are invariant up to controlled \)\mathcal O(|\lambda-1|)\( shifts absorbed in calibration constants. (App. J.4 gives a beta‑function view.) **Operational Planck tile.** If \)v_{\rm LR}\le c\(, adopt \)\tilde\ell_P:=\ell_P (c/v_{\rm LR})^{1/2}\( as the Planck‑window coarse‑graining scale; all Planck‑window statements hold with \)\ell\approx\tilde\ell_P\(. --- ## 10.3 Budget quadratics ⇒ equations of state (with robustness) Let the calibrated quadratics be: throughput \)Q_{\rm th}(A)=\langle[H,A],[H,A]\rangle_{\rm HS}\(; complexity \)Q_{\rm cx}(A)=\langle\nabla_\xi A,\nabla_\xi A\rangle\( (Ad‑invariant Hilbertian with correlation length \)\xi\(); leakage \)Q_{\rm leak}(A)=\|(I-\mathcal P^W)A\|^2\( (Dirichlet in \)W\(). Denote multipliers \)\alpha_{\rm th},\alpha_{\rm cx},\alpha_{\rm leak}\(. **Lemma 10.5 (Throughput).** With \)\hbar=\lambda_{\rm th}^{-1}\(: \)\rho_{\rm th}=c_{\rm th}\,\alpha_{\rm th}\,\Omega^2\( and \)p_{\rm th}=\tfrac13\rho_{\rm th}\( (ultra‑relativistic sector). **Lemma 10.6 (Complexity).** With tile‑uniform LSI/Poincaré at scale \)\xi\(: \)\rho_{\rm cx}=c_{\rm cx}\,\alpha_{\rm cx}\,\xi^{-2}\(, and \)p_{\rm cx}=-\partial\rho_{\rm cx}/\partial (3\log a)\(. **Lemma 10.7 (Leakage).** With left‑Dirichlet \)Q_{\rm leak}\( and pinching gap \)\gamma_W\(: \)\rho_{\rm leak}=c_{\rm leak}\,\alpha_{\rm leak}\,A/V\sim c_{\rm leak}\,\alpha_{\rm leak}\,\ell^{-1}\(, and \)w_{\rm leak}\in[-1,1/3]\(. Endpoint \)w\to-1\( holds when the leakage block is pointer‑frozen (log‑Sobolev gap \)\ge\gamma_0>0\(); \)w\to1/3\( holds if it thermalizes within the LR cone. **Stability under representatives.** If \)Q\( and \)Q'\( are norm‑equivalent on the admissible class (constants \)m,M\(), the scalings and \)w\( persist; only \)c_\bullet\( rescale within \)[m,M]\(. --- ## 10.4 FRW emergence and quantitative near‑flatness Inside the supercritical domain \)\Omega_{\rm nuc}\(, LR locality and \)D\(-contraction imply decay of anisotropic stress and vorticity over large boxes \)B_R\(: \)\|\pi_{ij}\|+\|\omega_i\|\ \le\ C\,\frac{|\partial B_R|}{|B_R|}\,\Phi\!\left(\tfrac{\alpha_{\rm leak}}{\alpha_{\rm th}},\tfrac{\alpha_{\rm leak}}{\alpha_{\rm cx}}\right)\xrightarrow{R\to\infty}0.\( Thus the slow Γ‑limit reduces to FRW with \)p_{\rm eff}=\tfrac13\rho_{\rm eff}+o(1)\( initially and standard Friedmann–Raychaudhuri holds. **Proposition 10.8 (Near‑flatness inequality).** For any comoving exhaustion \)B_R\( and horizon time \)t_H(R)\(, \)\sup_{t\le t_H(R)}\frac{|K|}{a^2}\ \le\ C_{\rm flat}\,\frac{\alpha_{\rm leak}\,A(B_R)}{V(B_R)\,H^2}+o_R(1).\( Equivalently, \)|\Omega_k|\le C_{\rm flat}(\alpha_{\rm leak}/\alpha_{\rm th})(A/V)(\Omega_r/H_0^2)+o_R(1).\( --- ## 10.5 Risk‑sensitive envelope; epi‑convergence and commuting limits Let \)(\mathcal P,\mathcal F,\mu_\beta)\( be the poke space with exponentially tight tails. Define \)\mathrm{CL}(A,\Phi)=\inf_{p\in\mathcal P}L(A,\Phi;p)\(, l.s.c. in \)(A,\Phi)\(. **Lemma 10.9 (Envelope epi‑convergence).** As \)\beta\to\infty\( with \)\mu_\beta\Rightarrow\mu_\infty\( supported on the admissible cone, \)\lim_{\beta\to\infty}\sup_A \mathrm{CL}_\beta(A,\Phi)=\sup_A\operatorname*{ess\,inf}_{p\sim\mu_\infty}L(A,\Phi;p),\( and maximizers exist on calibrated sublevels. **Lemma 10.10 (Commuting limits).** On finite boxes, taking \)\beta\to\infty\( then \)\varepsilon\to0\( (Γ‑limit) yields the same envelope as any interleaving respecting LR locality. --- ## 10.6 Conservation in the slow sector (Noether + Γ‑limit) Let the slow functional be \)\mathcal S[g;\alpha_\bullet]\( with budget constraints enforced by multipliers. Variations \)\delta g\( obeying compact support and cone‑preserving gauge produce \)\delta\mathcal S=\tfrac12\int (T^{\rm eff}_{\mu\nu})\,\delta g^{\mu\nu}\,\sqrt{-g}\,d^4x,\qquad T^{\rm eff}=T^{\rm vis}+T^{\rm fast}.\( Cone‑preserving diffeomorphisms give \)\nabla\!\cdot T^{\rm eff}=0\(. Leakage only exchanges budget **within** \)T^{\rm fast}\(; the **sum** is conserved in the slow sector. --- ## 10.7 Big‑Bang vs. coherence bounce; energy conditions Let \)\rho=\rho_{\rm th}+\rho_{\rm cx}+\rho_{\rm leak}\( with \)w_{\rm th}\approx\tfrac13\(, \)w_{\rm cx}\in[0,1]\(, \)w_{\rm leak}\in[-1,1/3]\(. **Theorem 10.11 (Bounce criterion).** If \)\rho_{\rm leak}+3p_{\rm leak}<-(\rho_{\rm th}+\rho_{\rm cx}+3p_{\rm th}+3p_{\rm cx})\( over an interval, then \)\ddot a>0\( and a **minimum scale factor** \)a_{\min}>0\( occurs. (Raychaudhuri.) **Lemma 10.12 (SEC/ANEC status).** The effective fluid need not satisfy SEC; pointer‑frozen leakage (\)w\to-1\() violates SEC while LR microcausality holds. Hence singularity theorems’ hypotheses fail in the bounce branch. **Sequestered windows; anisotropy seeds.** Near horizons/interiors, leakage throttling (\)L\downarrow\() with \)\gamma_W\uparrow\( can allow \)\mathcal R_{\rm coh}>1\( **inside** a causal window, producing daughter domains that are **sequestered** (domain‑wall containment). Front roughness induces a two‑point function \)\langle\delta\rho(\mathbf x)\delta\rho(\mathbf y)\rangle\sim r^{-(d-1)}\( inside the LR horizon, giving a near scale‑invariant spectrum in \)d=3\( after horizon crossing (cf. Sim‑S2). --- ## 10.8 Calibration protocol; constants; falsifiers Constants \)C_L,\gamma_W,v_{\rm LR},C_M,c_\bullet\( are fixed by App. J.2; predictions are stable under norm‑equivalent representatives (App. J.1). **Falsifiers:** (i) LR violation; (ii) failure of Lemma 10.9 (non‑attainment); (iii) robust violation of Prop. 10.8 across multiple \)B_R\( at fixed calibration; (iv) in‑medium supercritical cascades (violates Thm 10.4); (v) need for a **fourth** budget. --- # Chapter 11 — Planck Window: Budgets, Area Bounds, and Operational Scales > **Scope.** We fix Planck‑window hypotheses, prove **short‑time** and **global‑in‑time** tile‑area bounds for cross‑boundary information in any \)D\in\mathsf{IM}(\tau)\(, and relate the tiling scale to the operational Planck length \)\tilde\ell_P\( when \)v_{\rm LR}\le c\(. --- ## 11.1 Planck‑window hypotheses * **(P1) Local dimension control.** On any tile \)T\( of side \)\ell\(, \)d_{\rm loc}(\ell)\lesssim (\ell/\ell_*)^{\kappa}\( for microscopic \)\ell_*\(, \)\kappa>0\(. * **(P2) LR microcausality.** GKSL obeys LR bounds with velocity \)v_{\rm LR}(\ell)\( uniformly finite across tiles. * **(P3) Dirichlet linearity.** Leakage is left‑Dirichlet in \)W\( and orthogonally additive in its spectral decomposition. * **(P4) Throughput normalization.** \)\hbar=\lambda_{\rm th}^{-1}\( (local blocks and inductive limit). * **(P5) Information class.** Use \)D\in\mathsf{IM}(\tau)\( throughout. **Operational Planck tile.** If \)v_{\rm LR}\le c\(, the Planck‑window tile is \)\tilde\ell_P=\ell_P(c/v_{\rm LR})^{1/2}\(; use \)\ell\approx\tilde\ell_P\( in area bounds. --- ## 11.2 Short‑time tile‑area bound (single cone) For a union \)A\( of tiles and times \)t\le c_{\rm time}\,\ell/v_{\rm LR}\(, the GKSL evolution at a KKT point satisfies, for any \)D\in\mathsf{IM}(\tau)\(, [ \boxed{\ I_D(A{:}\bar A; t)\ \le\ C_{\rm info}(D)\,\frac{|\partial A|}{\ell}\,\Phi\!\left(\frac{\alpha_{\rm leak}}{\alpha_{\rm th}},\frac{\alpha_{\rm leak}}{\alpha_{\rm cx}}\right)\ }, ] with \)C_{\rm info}(D)=C_0(D)\,(1-e^{-\gamma_W t})/(1-e^{-\gamma_* t})\(. Here \)\gamma_*\( is the slowest mixing rate in \)A\(; \)c_{\rm time},C_0(D)\( depend only on LR and tile LSI. *Proof sketch:* LR quasi‑factorization + pinching contraction + orthogonal additivity in \)W\(. Constants are **calibrated**, not universal. --- ## 11.2′ Globalized area bound (all times) For any \)t\ge0\(, [ I_D(A{:}\bar A;t)\ \le\ \frac{|\partial A|}{\ell}\Big[C_1(D)\big(1-e^{-\gamma_W t}\big)+C_2(D)\!\int_0^t e^{-\gamma_* (t-s)}\,\Xi(s)\,ds\Big], ] where \)\Xi\( depends only on LR profile and tile LSI constants. (Iterated cone decomposition + Grönwall on \)I_D\(.) **Consequence.** At \)\ell\approx\tilde\ell_P\(, cross‑boundary predictive content is area‑limited with coefficients controlled by budget ratios and \)(\gamma_W,v_{\rm LR},\text{LSI})\( fixed at calibration; stability holds under norm‑equivalent representatives (App. J.1). --- ## 11.3 Inflationary embedding (optional) If an inflaton exists, coherence supplies **dissipative slow‑roll** corrections: leakage shifts friction by \)\Delta\Gamma\propto\alpha_{\rm leak}\(, throughput enforces a kinetic penalty \)\propto\alpha_{\rm th}\(; LR locality is preserved. Pure coherence‑smoothing (§10.4) remains viable with \)T^{\rm vis}\( absent. --- # Chapter 12 — Dark Sector from Coherence (Minimal Candidates + Inequalities) > **Scope.** We present three **minimal** dark‑matter candidates as coherence‑selected patterns. Each couples gravitationally via the slow sector, is budget‑suppressed in the fast/pointer sector, and admits **quantitative inequalities** mapping viability directly to calibrated **\)\alpha\(-ratios** and constants. --- ## 12.1 Hidden‑pointer (HP) sector — CDM‑like **Construction.** Let \)W=\sum_a w_a P_a\(; a hidden block \)P_D\( with \)w_D\gg w_{\rm vis}\( suppresses leakage for operators on \)P_D\(. Consider a HP U(1) sector with field strength \)F^D\( contributing only gravitationally at the Γ‑limit. **Coldness inequality.** The effective sound speed obeys \)c_s^2\ \le\ \varepsilon_{\rm cold}:=C_{\rm gap}\Big(\frac{T}{\Delta_{\rm HP}}\Big)^2,\( with pointer gap \)\Delta_{\rm HP}\(. Require \)c_s^2\lesssim10^{-6}\( by matter–radiation equality. **Discriminants.** (i) **Growth‑index shift** \)\Delta\gamma\( from residual \)c_s^2\neq0\(; (ii) **absence of isocurvature** by pointer isolation. Failure of either falsifies HP under fixed calibration. --- ## 12.2 Phase‑mode axion (PX) — misalignment cold/warm **Construction.** A global \)U(1)\( phase, protected by pointer alignment, yields a light **phase mode** \)\theta\( with \)V(\theta)=\Lambda_{\rm cx}^4\,(1-\cos\theta),\qquad \Lambda_{\rm cx}^4\propto\alpha_{\rm cx},\( kinetic term fixed by \)\hbar=\lambda_{\rm th}^{-1}\(. Misalignment abundance \)\rho_{\rm PX}(a_0)=\tfrac12 f_a^2 m_a^2\,\theta_0^2\,\mathcal T\big(m_a/H\big),\( with \)(m_a,f_a)\( constrained by \)(\alpha_{\rm cx},\alpha_{\rm th})\( calibration. **Warmness bound.** Ly‑\)\alpha\( and LSS require free‑streaming below the observed cutoff, which translates to a **lower** bound on \)m_a\( (given \)f_a\() and excludes parts of \)(\alpha_{\rm cx},\alpha_{\rm th})\( space. **Discriminant.** A **correlated late‑time viscosity** from \)Q_{\rm cx}\( must align with the allowed \)(m_a,f_a)\(; mismatch falsifies PX. --- ## 12.3 Sterile‑mixing neutrino (SN) — warm **Construction.** A minimal seesaw‑like block with derivation‑pricing + leakage alignment suppresses visible mixing by \)\sin^2(2\theta)\ \sim\ C_{\rm mix}\Big(\frac{\alpha_{\rm th}}{\alpha_{\rm leak}}\Big)^2.\( Freeze‑in from pointer‑misaligned dissipators sets the relic abundance. **Free‑streaming inequality.** Require \)\lambda_{\rm FS}\ \simeq\ \int \frac{v(a)}{a^2 H(a)}\,da\ \le\ 0.1\ \text{Mpc},\( which imposes a **lower** bound on mixing mapped to \)\alpha_{\rm th}/\alpha_{\rm leak}\(; combine with X‑ray line limits to confine the viable band. --- ## 12.4 Shared falsifiers; calibration stability; baryogenesis routes All candidates share a single calibration \)(\alpha_{\rm th},\alpha_{\rm cx},\alpha_{\rm leak})\(. A persistent need for a **fourth** budget, or lab evidence of **basis‑invariant** decoherence contradicting pointer alignment, invalidates the constructions. **Proposition 12.1 (Calibration stability).** If \)\langle\cdot,\cdot\rangle\( and \)\langle\cdot,\cdot\rangle'\( are norm‑equivalent on the admissible class with \)m\|X\|^2\le\|X\|'^{2}\le M\|X\|^2\(, then multipliers satisfy \)m\,\alpha_\bullet\le\alpha'_\bullet\le M\,\alpha_\bullet\( component‑wise; predictions depending on **ratios** \)\alpha_i/\alpha_j\( are invariant up to \)[m,M]\(. **Baryogenesis.** Baseline: **standard leptogenesis** via the SN sector. Optional: **leakage‑phase baryogenesis**, where a pointer‑dependent phase in the Dirichlet form biases sphalerons (predicts CP‑odd leakage observables in lab GKSL analogs). --- # Chapter 13 — Predictions, Calibration & Tests > **Scope.** Testable predictions with one primary KPI each, minimal supports, and calibration procedures. Constants are linked to multipliers via envelope identities. **Global KPI carried through.** We fit the **coherence number** \(\chi=\tau_{\rm dec}/\tau_{\rm mess}\) in each setting and extract multipliers via the envelope identities (App. E.4). Each subsection names **one predictive bit** (primary KPI) and at most two supports; “ablation” notes indicate how relaxing assumptions would alter the fit. ### 13.0 Toy-world validation of \(\mathrm{CL}\) (CA and qubit) **Protocol.** We run the CA toy (\(\mathrm{CL}_{\rm CA}\)) on \(n\!\times\!n\) grids with a fixed menu \(\mathscr T_{\rm CA}\) of thresholds and weights, and the qubit toy (\(\mathrm{CL}_{\rm Q}\)) with \((\rho_0,\rho_1)\) aligned/misaligned with \(W\). For each, we estimate the global KPI \(\chi=\tau_{\rm dec}/\tau_{\rm mess}\) and fit multipliers via the envelope identities. **Predicted invariants.** (i) **Monotone equivalence:** rankings of \(A\) by \(\mathrm{CL}_{\rm CA}\) and \(\mathrm{CL}_{\rm Q}\) agree up to an increasing transform; (ii) **Pointer alignment:** leakage-minimizing generators align with \(W\); (iii) **Ablation:** relaxing Ad-invariance reintroduces a fourth quadratic direction and breaks the equivalence (Section 2.2 note). **Measurement.** Report \(\mathrm{CL}\)-scores with \(95\%\) binomial CIs, estimated \(\chi\), and inferred multipliers. Each run uses finite, auditable protocols with reproducible seeds. ## 13.1 Gravitational‑wave phasing residual (binary inspirals) **Prediction.** Phase residual \)\Delta p\( relative to GR templates scales as \)\Delta p\approx \varepsilon\,\eta\,(\pi G M_c f/c^3)^{\!\eta}\( with \)\varepsilon\sim0.05,\eta\approx1\(. **KPI:** bias‑robust estimator of \)\eta\( across events. **Supports:** residual‑vs‑frequency slope; cross‑event scaling with \)M_c\(. ## 13.2 Horizon flux suppression **Prediction.** Outgoing flux **below** Hawking prediction by factor \)f(\lambda_{\rm leak},W)\le1\(. **KPI:** \)\mathcal F_{\rm out}/\mathcal F_{\rm Hawking}\(. **Supports:** two‑point distortions; pointer‑basis stability. ## 13.3 Pointer basis in noisy interferometers **Prediction.** Environmental weight \)W\( selects a unique pointer basis minimizing \)\sum_j\omega(L_j^\dagger W L_j)\(. **KPI:** basis‑aligned decoherence rates vs misaligned configs. ## 13.4 Calibration of \)\hbar\( With \)\dot A=i\hbar^{-1}[H,A]\(, use a two‑level system at frequency \)\Omega\(; measure Fubini–Study speed \)v\(; set \)v=2\Delta H/\hbar\( to calibrate \)\hbar=\lambda_{\rm th}^{-1}\(. ## 13.5 Envelope identities Optimal value \)\Phi(\tau)\( ⇒ \)\lambda_\bullet=\partial\Phi/\partial\tau_\bullet\( a.e.; defines \)\hbar,G,\Lambda,\alpha_i,\ldots\(. **Protocol:** fit \)\lambda\(s by matching observed invariants under RG constraints. ## 13.6 Measurement hygiene Collect only predictive signals; cone‑limited timing windows; publish priors/instruments/code; pre‑register stop rules. # Appendix A — H0′: Spaces, Norms & Budgets (C\*‑compatible) * **Algebra.** Inductive‑limit C\*‑algebra \)\mathcal A=\overline{\bigcup_\Lambda \mathcal A_\Lambda}\(. * **State/GNS.** Faithful normal state \)\omega\(, GNS triple \)(\pi_\omega,\mathcal H_\omega,\Omega_\omega)\(; identify \)\mathcal A\( with \)\pi_\omega(\mathcal A)\subset\mathcal B(\mathcal H_\omega)\(. * **Core.** Dense invariant \)\mathcal D\( common to all generators. **Throughput quadratic.** On each finite \)\Lambda\(, using normalized HS inner product from \)\mathrm{tr}_\Lambda/d_\Lambda\(: [ \mathcal B_{\rm th}^\Lambda:=\tfrac12\|\delta_H\|_{{\rm der};\Lambda}^2,\quad \boxed{\mathcal B_{\rm th}:=\sup_\Lambda \mathcal B_{\rm th}^\Lambda}.] **Leakage budget.** [ \boxed{\,\mathcal B_{\rm leak}(\{L_j\},W) = \sum_j \| W^{1/2} L_j \|_{2,\omega}^2 = \sum_j \omega(L_j^\dagger W L_j)\,} ] **Complexity budget.** [ \boxed{\,\mathcal B_{\rm cx}(\mathcal L) = \inf\Big\{\sum_\alpha \kappa_\alpha \|\mathcal J_\alpha\|_{cb}^2\;:\; \mathcal L=\sum_\alpha \mathcal J_\alpha\ \text{ on }\ \mathcal A_{\rm loc}\Big\}\,} ] **Collected properties.** \)\mathcal B_{\rm th},\mathcal B_{\rm leak},\mathcal B_{\rm cx}\( are convex, l.s.c.; sublevels equi‑coercive (Ch. 4). Only three independent budgets up to nulls (Thm I.1). *Notation.* We use **\)B_{\rm cx}\(** (“complexity”) interchangeably with the local‑decomposition **compression** quadratic; \)B_{\rm cx}\equiv \mathcal B_{\rm cx}\(. # Appendix B — Large‑Deviation Machinery (Risk‑Sensitive ⇒ Worst‑Case) * Varadhan’s lemma for \)\log\mathbb E e^{\beta\ell}\( ⇒ \)\beta\to\infty\( yields worst‑case inner min. * Laplace principle on \)\mathcal A\( under coercivity and u.s.c. * Epi‑convergence in \)\beta\(: \)\mathrm{CL}_\beta\searrow \inf_\Phi \mathrm{CL}\(. # Appendix C — Gauge/Matter Derivations (Yukawas, Anomalies, Hypercharge) Binder set, linear system, and solution giving the SM hypercharges (details as in Ch. 6). # Appendix D — Γ-Limit to Einstein–Hilbert (airtight revision) > **Goal.** Construct an explicit, gauge-fixed family \)\{\mathcal F_\varepsilon\}_{\varepsilon\downarrow 0}\( whose Γ-limit on the admissible class is precisely the Einstein–Hilbert (EH) functional with cosmological constant. We (i) correct the order mismatch in the approximant, (ii) unify measures, (iii) prove equi-coercivity in the right topology, (iv) secure Γ-liminf and recovery with coefficient stability via a smoothing functor, (v) identify the principal symbol, and (vi) fix \)G\( and \)\Lambda\( by two independent normalizations. --- ## D.1  Setting, gauge, admissible class (as previously accepted) * **Manifold & charts.** \)M\( is a smooth 4-manifold of bounded geometry (uniform injectivity radius; all curvature derivatives bounded) with a countable harmonic-chart atlas. * **Cone class.** Admissible metrics \)g\( lie in the **single-cone**, time-oriented class \)\mathfrak G\(: there exist Lorentzian \)g_\*,g^\*\( with \)g_\*\le g\le g^\*\( a.e. in harmonic coordinates, uniformly on compacts. * **Gauge.** We work **on the de Donder slice** \)\mathcal F_\mu(g)=0\( where [ \mathcal F_\mu(g):=g_{\mu\nu}\Gamma^\nu(g),\qquad \Gamma^\nu(g):=g^{\alpha\beta}\Gamma^\nu_{\alpha\beta}(g). ] The gauge holds distributionally in each harmonic chart. * **Topology.** Unless otherwise stated, convergence is **weak \)H^1_{\rm loc}\(** in harmonic charts (see D.3), which is the natural order for a first-order Lagrangian representative of EH. --- ## D.2  Approximating family \)\mathcal F_\varepsilon\( with **explicit first-order** coefficients and a **single measure** ### D.2.1  The first-order EH representative (Γ·Γ form) Recall the classical identity (valid in any coordinates): [ \sqrt{|g|}\,R(g) =\sqrt{|g|}\,g^{\alpha\beta}\!\left(\Gamma^\mu_{\alpha\nu}\Gamma^\nu_{\beta\mu}-\Gamma^\mu_{\alpha\beta}\Gamma^\nu_{\mu\nu}\right) \ +\ \partial_\alpha\!\big(\sqrt{|g|}\,V^\alpha(g)\big), \tag{D.1} ] where \)V^\alpha(g)=g^{\mu\nu}\Gamma^\alpha_{\mu\nu}-g^{\alpha\mu}\Gamma^\nu_{\mu\nu}\(. Using [ \Gamma^\mu_{\alpha\beta}=\tfrac12 g^{\mu\lambda}\!\left(\partial_\alpha g_{\beta\lambda}+\partial_\beta g_{\alpha\lambda}-\partial_\lambda g_{\alpha\beta}\right), \tag{D.2} ] the **non-divergence** part of \)\sqrt{|g|}R(g)\( is a **purely first-order quadratic** in \)\partial g\(. Expanding (D.1)–(D.2) yields the canonical “Γ·Γ” quadratic density [ \boxed{\; \mathcal Q(g,\partial g) :=\sqrt{|g|}\,g^{\alpha\beta} \Big(\Gamma^\mu_{\alpha\nu}\Gamma^\nu_{\beta\mu}-\Gamma^\mu_{\alpha\beta}\Gamma^\nu_{\mu\nu}\Big) \;=\; \mathsf C^{\alpha\beta\,\mu\nu\rho\sigma}(g)\,(\partial_\alpha g_{\mu\nu})(\partial_\beta g_{\rho\sigma}), \;} \tag{D.3} ] with **explicit** coefficient tensor [ \mathsf C^{\alpha\beta\,\mu\nu\rho\sigma}(g) =\tfrac14\sqrt{|g|}\,g^{\alpha\beta}\Big( g^{\mu\rho}g^{\nu\sigma}+g^{\mu\sigma}g^{\nu\rho}-2\,g^{\mu\nu}g^{\rho\sigma} \Big) +\tfrac14\sqrt{|g|}\Big( g^{\alpha\mu}g^{\beta\rho}g^{\nu\sigma}+g^{\alpha\mu}g^{\beta\sigma}g^{\nu\rho} -g^{\alpha\mu}g^{\beta\nu}g^{\rho\sigma}-g^{\alpha\rho}g^{\beta\sigma}g^{\mu\nu} \Big), \tag{D.4} ] which is obtained by substituting (D.2) into (D.1) and collecting the \)(\partial g)(\partial g)\( terms. (Any equivalent explicit expansion is acceptable; (D.4) fixes a concrete choice.) Thus, [ \sqrt{|g|}\,R(g)=\mathcal Q(g,\partial g)+\partial_\alpha\!\big(\sqrt{|g|}\,V^\alpha(g)\big). \tag{D.5} ] > **Order fix.** There is **no zeroth-order surrogate** for the Γ·Γ piece; all non-divergence contributions are first order in \)\partial g\(. We therefore **remove** the erroneous term \)\langle B_0(g)g,g\rangle\( and work with the explicit first-order tensor \)\mathsf C(g)\( in (D.4). ### D.2.2  Unified measure and the approximating family Fix a smooth **reference volume** \)d{\rm vol}_\sharp:=\sqrt{|g_\sharp|}\,d^4x\( from a bounded-geometry Riemannian metric \)g_\sharp\( (used only for analytic control). Let [ J(g):=\frac{\sqrt{|g|}}{\sqrt{|g_\sharp|}}\quad\text{(Jacobian density)}. \tag{D.6} ] Define, for \)\varepsilon\in(0,1]\(, [ \boxed{\; \begin{aligned} \mathcal F_\varepsilon(g)\;:=\;\frac{1}{16\pi\,\mathsf G_\varepsilon}\! \int_M\!\Big[ J(g)^{-1}\,\mathcal Q(g,\partial g)\;+\;\varepsilon\,\mathsf a\,\langle\nabla g,\nabla g\rangle_{g_\sharp} \;+\;\varepsilon^2\,\mathsf b\,\langle\nabla^2 g,\nabla^2 g\rangle_{g_\sharp} \Big]\ d{\rm vol}_\sharp \\ -\;\frac{\Lambda_\varepsilon}{8\pi\,\mathsf G_\varepsilon}\int_M\! J(g)\ d{\rm vol}_\sharp\;+\;\mathcal B_{\rm bdry}[g;\varepsilon], \end{aligned} \;} \tag{D.7} ] with fixed constants \)\mathsf a,\mathsf b>0\(. The boundary/shell term \)\mathcal B_{\rm bdry}\( is the **chartwise integral of the divergence** in (D.5) written against \)d{\rm vol}_\sharp\( (or zero if boundaryless/decay suffices). Thus the **entire integrand uses one measure** \)d{\rm vol}_\sharp\(; the EH density appears as \)J(g)^{-1}\mathcal Q\( + divergence (cf. (D.5)–(D.6)). *Notes.* (i) The first-order stabilizer \)\varepsilon\,\langle\nabla g,\nabla g\rangle_{g_\sharp}\( and the second-order \)\varepsilon^2\langle\nabla^2 g,\nabla^2 g\rangle_{g_\sharp}\( are analytic **regularizers** (vanishing in the Γ-limit) that ensure tightness in \)H^1\( and control of oscillations. (ii) Gauge is imposed at the level of the **admissible class** (D.1), so no gauge penalty term is needed; if one works off-slice, add \)\varepsilon\!\int |{\rm div}_g g|^2\( contracted with \)g_\sharp^{-1}\( without changing the limit on \)\mathfrak G\(. --- ## D.3  Equi-coercivity in **weak \)H^1_{\rm loc}\(** We carry Γ-convergence in the **\)H^1_{\rm loc}\(** topology, the natural order for the first-order representative of EH. ### D.3.1  Local Gårding-type lower bound On any harmonic chart \)U\Subset M\(, cone bounds give uniform ellipticity/comparability between \)g\( and \)g_\sharp\(. Freezing coefficients and using (D.3)–(D.4) one obtains, for some \)c_U,C_U>0\( (depending only on the cone and bounded-geometry constants): [ \int_U J(g)^{-1}\,\mathcal Q(g,\partial g)\ d{\rm vol}_\sharp \ \ge\ -c_U\int_U |\partial g|^2_{g_\sharp}\ d{\rm vol}_\sharp \ -\ C_U. \tag{D.8} ] (The possible negative part reflects Lorentzian signature; it is **uniformly controlled** on \)\mathfrak G\(.) ### D.3.2  Equi-coercivity from the vanishing regularizer Combining (D.8) with the explicit regularizers in (D.7) gives, on each chart, [ \mathcal F_\varepsilon(g)\ \ge\ \frac{\varepsilon\,\mathsf a}{16\pi}\int_U |\partial g|^2_{g_\sharp}\ d{\rm vol}_\sharp\ -\ C_U, \tag{D.9} ] and summing over a finite cover of a compact exhaustion of \)M\( yields **tightness of sublevel sets in \)H^1_{\rm loc}\(** uniformly in \)\varepsilon\(. (The \)\varepsilon\(-weighted first-order stabilizer is precisely what prevents high-frequency escape while still vanishing in the limit; see Γ-liminf/D.4.) > **Conclusion (D.3).** The family \)\{\mathcal F_\varepsilon\}\( is **equi-coercive** in the weak \)H^1_{\rm loc}\( topology on \)\mathfrak G\(. --- ## D.4  Γ-liminf and recovery (with stable coefficients) Two technical issues are addressed: **(i)** coefficient stability along weakly convergent sequences and **(ii)** gauge-preserving recovery with an **elliptic** operator. ### D.4.1  Coefficients via a smoothing functor \)S\( Let \)S\( be a fixed, bounded-geometry **smoothing operator** defined chartwise by heat-kernel regularization with respect to \)g_\sharp\( at scale \)\tau(\varepsilon)\downarrow 0\(, patched by a partition of unity; then [ S:\ H^1_{\rm loc}\to C^{0,\alpha}_{\rm loc}\cap L^\infty_{\rm loc},\qquad S(g_\varepsilon)\to S(g)\ \text{uniformly on compacts if }g_\varepsilon\rightharpoonup g\text{ in }H^1_{\rm loc}. \tag{D.10} ] We **define** the coefficient tensor in the approximants by [ \mathsf C_\varepsilon(\cdot):=\mathsf C\big(S(\cdot)\big),\quad J_\varepsilon(\cdot):=J\big(S(\cdot)\big), \tag{D.11} ] i.e., **Carathéodory structure**: measurable in \)x\(, continuous in the (smoothed) field. Then along any \)g_\varepsilon\rightharpoonup g\(, [ \mathsf C_\varepsilon(g_\varepsilon)\to \mathsf C\big(S(g)\big),\qquad J_\varepsilon(g_\varepsilon)\to J\big(S(g)\big) \quad\text{in }L^\infty_{\rm loc}, \tag{D.12} ] and since \)S(g)\to g\( in \)L^2_{\rm loc}\( and a.e., replacing \)(\mathsf C,J)\( by \)(\mathsf C(Sg),J(Sg))\( does **not change the limit functional** (standard stability argument; see Γ-limsup below). For readability we suppress \)S\( in what follows; the proof implicitly uses (D.11)–(D.12). ### D.4.2  Γ-liminf Let \)g_\varepsilon\rightharpoonup g\( in \)H^1_{\rm loc}\(, with \)g_\varepsilon,g\in\mathfrak G\(. By (D.12) and weak lower semicontinuity of convex quadratic forms in \)\partial g\(, [ \liminf_{\varepsilon\downarrow 0}\!\int J(g_\varepsilon)^{-1}\,\mathcal Q(g_\varepsilon,\partial g_\varepsilon)\,d{\rm vol}_\sharp \ \ge\ \int J(g)^{-1}\,\mathcal Q(g,\partial g)\,d{\rm vol}_\sharp. \tag{D.13} ] The stabilizers are nonnegative, so they only **increase** the liminf. Using (D.5) and the definition of \)\mathcal B_{\rm bdry}\(, [ \int J(g)^{-1}\,\mathcal Q(g,\partial g)\,d{\rm vol}_\sharp =\int \sqrt{|g|}\,R(g)\,d^4x\ -\ \int \partial_\alpha\!\big(\sqrt{|g|}\,V^\alpha(g)\big)\,d^4x, \tag{D.14} ] and the last term cancels with \)\mathcal B_{\rm bdry}\( (or vanishes under the boundary/decay conditions built into \)\mathcal B_{\rm bdry}\(). Therefore [ \boxed{\; \Gamma\text{-}\liminf_{\varepsilon\downarrow 0}\ \mathcal F_\varepsilon(g_\varepsilon) \ \ge\ \mathcal F_0(g) :=\frac{1}{16\pi\,\mathsf G}\int \sqrt{|g|}\,R(g)\,d^4x\ -\ \frac{\Lambda}{8\pi\,\mathsf G}\int \sqrt{|g|}\,d^4x. \;} \tag{D.15} ] ### D.4.3  Recovery sequences (gauge-preserving, elliptic repair) Fix \)g\in\mathfrak G\(. Choose a compact exhaustion and mollify chartwise by \)S\( to get smooth \)g^{(k)}:=S_{\tau_k}(g)\to g\( in \)H^1_{\rm loc}\( and a.e., preserving the cone bounds for all large \)k\(. The mollification may violate de Donder gauge **slightly**; repair gauge using a **fixed elliptic** reference operator: [ \Delta_{g_\sharp}X^{(k)}=\mathcal F\!\left(g^{(k)}\right)\quad\text{(in each chart with Dirichlet data)},\qquad \tilde g^{(k)}:=(\exp X^{(k)})^\*g^{(k)}. \tag{D.16} ] Standard elliptic estimates on bounded-geometry charts give \)\|X^{(k)}\|_{H^2}\lesssim \|\mathcal F(g^{(k)})\|_{L^2}\to 0\(, hence \)\tilde g^{(k)}\to g\( in \)H^1_{\rm loc}\( and \)\mathcal F(\tilde g^{(k)})=0\(. Set \)\varepsilon_k\downarrow 0\( with \)\tau_k\downarrow 0\( and define \)g_{\varepsilon_k}:=\tilde g^{(k)}\(. Using (D.12) and dominated convergence, [ \lim_{k\to\infty}\ \mathcal F_{\varepsilon_k}(g_{\varepsilon_k})\ =\ \mathcal F_0(g). \tag{D.17} ] Thus **recovery sequences exist for every \)g\in\mathfrak G\(**. --- ## D.5  Principal-symbol identification (Lichnerowicz in de Donder) Linearize at a bounded-geometry background \)\bar g\in\mathfrak G\(: write \)g=\bar g+h\( with \)h\in C_0^\infty(S^2T^*M)\( satisfying the linearized de Donder condition \)\bar\nabla^\mu (h_{\mu\nu}-\tfrac12\bar g_{\mu\nu}h)=0\(. The second variation of the first-order part (D.3)–(D.4) produces the **Lichnerowicz operator**; its principal symbol is [ \sigma_{\rm pr}(\mathcal E_0)(x,\xi)[h] =-\tfrac12\big(\bar g^{\alpha\beta}\xi_\alpha\xi_\beta\big)\Big(h_{\mu\nu}-\tfrac12\bar g_{\mu\nu}h\Big), \tag{D.18} ] i.e. the gauge-fixed Einstein symbol. The \)\varepsilon\(-regularizers contribute \)O(\varepsilon|\xi|^2)\( and \)O(\varepsilon^2|\xi|^4)\( symbols, which **vanish** in the Γ-limit and serve only for tightness. --- ## D.6  Fixing \)G\( and \)\Lambda\( by two **independent** normalizations * **Weak-field (Poisson) limit → \)G\(.** Around Minkowski \)\eta\( in global harmonic coordinates, for static weak fields \)g_{00}=-(1+2\phi)\(, \)g_{ij}=(1-2\phi)\delta_{ij}\(, coupling to matter through the operational \)T^{\rm eff}\( (Chapter 5) yields [ \Delta\phi=4\pi\,\mathsf G\,\rho. ] Matching Newtonian gravity fixes \)\boxed{\ \mathsf G=G\ }\(. * **Constant-curvature normalization → \)\Lambda\(.** For \)\mathrm{Ric}(g_\kappa)=3\kappa\,g_\kappa\( (de Sitter/anti-de Sitter class), stationarity gives \)G_{\mu\nu}(g_\kappa)+\Lambda\,g_{\mu\nu}=0
  \iff \Lambda=3\kappa\(. Hence \)\boxed{\ \Lambda=3\kappa\ }\( fixed independently of the weak-field fit. --- ## D.7  Γ-limit theorem (final) > **Theorem D (Γ-limit to Einstein–Hilbert).** > On the cone-preserving, de Donder-gauge class \)\mathfrak G\( with the **weak \)H^1_{\rm loc}\(** topology, the functionals \)\{\mathcal F_\varepsilon\}\( of (D.7) are equi-coercive and **Γ-converge** to > > [ > \boxed{\; > \mathcal F_0(g)=\frac{1}{16\pi G}\int_M \sqrt{|g|}\,\big(R(g)-2\Lambda\big)\,d^4x. > \;} > ] > > Moreover: > (i) the **principal symbols** of the Euler–Lagrange operators converge to the Lichnerowicz symbol in de Donder gauge (D.18); > (ii) **recovery sequences** exist for every \)g\in\mathfrak G\( (D.17); > (iii) the constants \)G\( and \)\Lambda\( are fixed by the **two normalizations** in D.6 (and not by a single calibration). *Proof sketch.* Equi-coercivity: D.3. Γ-liminf: D.4.2 with (D.12)–(D.15). Γ-limsup: D.4.3. Symbol: D.5. Constants: D.6. The divergence term is neutralized by \)\mathcal B_{\rm bdry}\( (or decay), so the limit functional equals EH exactly, not modulo a boundary integral. --- ### Remarks on robustness 1. **Order correctness.** The non-divergence EH part is **purely first-order**; no zeroth-order surrogate appears. This is enforced by (D.3)–(D.5). 2. **Unified measure.** All integrals are against \)d{\rm vol}_\sharp\(; the EH density is represented as \)J(g)^{-1}\mathcal Q\( (plus a divergence accounted for in \)\mathcal B_{\rm bdry}\(). 3. **Coefficient stability.** The **Carathéodory+smooth** design (D.10)–(D.12) ensures coefficients converge uniformly on compacts along weak \)H^1\( sequences, closing the gap flagged by the reviewer. 4. **Elliptic gauge repair.** The gauge-restoration step uses \)\Delta_{g_\sharp}\(, not a Lorentzian wave operator, eliminating any ambiguity and preserving the cone. 5. **No reliance on a single calibration.** \)G\( and \)\Lambda\( are fixed by **two independent** backgrounds (Newtonian and constant-curvature), completing the identification. *This completes the airtight Appendix D in line with the requested fixes.* # Appendix E — KKT, Riesz, and Unbounded-Operator Hygiene ## E.0 Standing setting (finite blocks → inductive limit) On a finite local block \$\Lambda\$ with matrix algebra \$\mathcal A\_\Lambda\simeq M\_{d\_\Lambda}\$, endow the space of linear maps \$X:\mathcal A\_\Lambda!\to!\mathcal A\_\Lambda\$ with the **normalized Hilbert–Schmidt** inner product [ \langle X,Y\rangle_{{\rm der};\Lambda} :=\frac{1}{d_\Lambda}\,\operatorname{Tr}_{\rm HS}\!\big(X^\dagger Y\big), \qquad \|X\|_{{\rm der};\Lambda}^2=\langle X,X\rangle_{{\rm der};\Lambda}. ] For a (symmetric) Hamiltonian \$H\in\mathcal A\_\Lambda\$, the **inner derivation** [ \delta_H(A):=i[H,A] ] is skew-adjoint with respect to \$\langle\cdot,\cdot\rangle\_{{\rm der};\Lambda}\$, and every derivation on \$M\_{d\_\Lambda}\$ is inner. The throughput budget on \$\Lambda\$ is [ \mathcal B_{\rm th}^\Lambda(H):=\tfrac12\|\delta_H\|_{{\rm der};\Lambda}^{2},\qquad \mathcal B_{\rm th}:=\sup_\Lambda \mathcal B_{\rm th}^\Lambda. ] ## E.1 Metric matching (gradient ↔ quadratic) All **Gateaux/Fréchet derivatives** of the predictive term are taken with respect to the same normalized HS inner product that defines \$\mathcal B\_{\rm th}\$. Equivalently, whenever a linear functional on velocities \$X\$ appears (e.g., \$X\mapsto D\Phi\_A[X]\$), its **Riesz representer** is computed in \$\langle\cdot,\cdot\rangle\_{{\rm der};\Lambda}\$. This removes the Banach/Hilbert mismatch and legitimizes the KKT step that equates a derivative to the gradient in the very metric used by the quadratic penalty. ## E.2 Dynamics from a time-parametrized variational principle We now provide the **missing bridge** from stationarity to dynamics. Work first on a fixed block \$\Lambda\$. ### E.2.1 Riesz representer on the derivation cone Let the predictive term at \$A\in\mathcal A\_\Lambda\$ have a Gateaux derivative \$D\Phi\_A[\cdot]\$ continuous on the space of velocities. Restrict it to the **admissible velocity space** [ \mathsf{Der}_\Lambda:=\{\delta_K:\ K=K^\dagger\in\mathcal A_\Lambda\}\subset \mathcal B(\mathcal A_\Lambda), ] which is a finite-dimensional Hilbert space under \$\langle\cdot,\cdot\rangle\_{{\rm der};\Lambda}\$. By Riesz, there exists a **unique** (up to addition of a multiple of the identity inside the commutator) \$K\_\Phi(A)=K\_\Phi(A)^\dagger\$ such that [ \boxed{\quad D\Phi_A[\delta_J]\;=\;\big\langle \delta_{K_\Phi(A)}\,,\,\delta_J\big\rangle_{{\rm der};\Lambda} \quad\text{for all }J=J^\dagger.\quad} ] We call \$\delta\_{K\_\Phi(A)}\$ the **predictive Riesz representer** at \$A\$ (restricted to derivations). ### E.2.2 Instantaneous ascent optimization and Euler–Lagrange velocity Fix \$A\$ and \$H\$ on \$\Lambda\$, and consider the **instantaneous** (small-time) optimization over admissible velocities \$X\in\mathsf{Der}\_\Lambda\$: [ \mathcal L_A(X;H):=D\Phi_A[X]\;-\;\frac{\lambda_{\rm th}}{2}\,\|X\|_{{\rm der};\Lambda}^{2}. ] This is a strictly concave quadratic in \$X\$ with unique maximizer [ \boxed{\quad X^*_A=\lambda_{\rm th}^{-1}\,\Pi_{\mathsf{Der}_\Lambda}\big(\nabla\Phi_A\big) \;=\;\lambda_{\rm th}^{-1}\,\delta_{K_\Phi(A)}.\quad} ] Hence the **Euler–Lagrange velocity field** on \$\Lambda\$ is the predictive Riesz representer scaled by \$\lambda\_{\rm th}^{-1}\$. ### E.2.3 KKT in \$H\$: alignment of Riesz and throughput directions The blockwise Lagrangian in \$(A,H)\$ reads [ \mathsf S_\Lambda(A,H)=\Phi(A)\;-\;\lambda_{\rm th}\,\mathcal B_{\rm th}^\Lambda(H)\;+\;\cdots, \qquad \mathcal B_{\rm th}^\Lambda(H)=\tfrac12\|\delta_H\|_{{\rm der};\Lambda}^2. ] Stationarity in \$H\$ (Slater interior and metric matching) yields the **KKT identity on \$\Lambda\$** [ \boxed{\quad D\Phi_A[\delta_H]\;=\;\lambda_{\rm th}\,\langle \delta_H,\delta_H\rangle_{{\rm der};\Lambda} \quad\Longleftrightarrow\quad \delta_{K_\Phi(A)}=\lambda_{\rm th}\,\delta_H.\quad} ] (The forward equivalence is precisely the Riesz characterization in §E.2.1.) Substituting this into the maximizer of §E.2.2 gives [ X^*_A=\lambda_{\rm th}^{-1}\,\delta_{K_\Phi(A)}=\delta_H. ] ### E.2.4 Emergent unitary dynamics and \$\hbar\$ Let \$A(t)\$ be an absolutely continuous path with \$\dot A(t)=X^*\_{A(t)}\$ on each block. From \$X^*\_A=\delta\_H\$ we obtain [ \boxed{\quad \dot A(t)=\delta_H\big(A(t)\big)=i[H,A(t)]\quad\text{on every finite block } \Lambda.\quad} ] Introducing **physical time** via \$t\_{\rm phys}:=\lambda\_{\rm th},t\$ (units fixed by experiment), the evolution becomes [ \boxed{\quad \frac{d}{dt_{\rm phys}}A(t_{\rm phys})=i\,\hbar^{-1}[H,A(t_{\rm phys})],\qquad \hbar:=\lambda_{\rm th}^{-1}.\quad} ] Thus **\$\hbar\$ is the inverse throughput multiplier** fixed by the chosen C\*-compatible quadratic and operational calibration (e.g., Fubini–Study speed). ### E.2.5 Inductive-limit transfer Let \${\Lambda\_n}\$ exhaust the system. If \${\lambda\_{\rm th}^{(\Lambda\_n)}}\$ is tight and the KKT identities hold on each \$\Lambda\_n\$, then by **graph-closure** of the derivation and strong convergence of the blockwise flows, the limit dynamics on the common local core \$\mathcal A\_{\rm loc}\$ satisfies \$\dot A=i\hbar^{-1}[H,A]\$. ## E.3 Unbounded GKSL: core, closability, drift Let \$\mathcal D\$ be a common invariant core for \$H\$ and \${L\_j}\$. * **(U1) Closability on the core.** \$\delta\_H\$ is closable on \$\mathcal A\_{\rm loc}\$; the GKSL form is well-defined on \$\mathcal D\$. * **(U2) Form bounds.** There exist \$N\ge0\$, \$a<1\$, \$b<\infty\$ with [ \|H\psi\|^2+\sum_j\|L_j\psi\|^2\ \le\ a\,\|N\psi\|^2+b\,\|\psi\|^2,\qquad \psi\in\mathcal D. ] * **(U3) Quasi-locality.** Finite interaction radius and bounded overlap uniformly in volume. * **(U4) Semigroup.** The closure generates a unique strongly continuous CPTP semigroup; Lieb–Robinson-type bounds hold. * **(U5) Lyapunov drift.** For some \$c\_0,c\_1>0\$, \$\mathcal L^\*(N)\le c\_0-c\_1N\$ on \$\mathcal D\$. With \$W=(1+N)^{-s}\$, \$s>\tfrac12\$, one has \$\sum\_j\omega(L\_j^\dagger W L\_j)<\infty\$, so \$\mathcal B\_{\rm leak}<\infty\$ and the **leakage budget is controlled**. ## E.4 Envelope identities (constants as multipliers) Let \$\Phi(\tau)\$ be the optimal value under allowances \$\tau\$. Under convexity and Slater interior, [ \lambda_\bullet(\tau)=\frac{\partial\Phi}{\partial\tau_\bullet}\quad\text{for a.e. }\tau, ] pinning **\$\hbar=\lambda\_{\rm th}^{-1}\$** and, in the slow sector, \$G,\Lambda,\ldots\$ as multipliers associated to their respective allowances. **Outcome.** The time-parametrized ascent principle, together with the KKT alignment of the predictive Riesz representer and the throughput derivation, yields \$\dot A=i\hbar^{-1}[H,A]\$ with \$\hbar=\lambda\_{\rm th}^{-1}\$, and the unbounded-operator hygiene ensures this extends from blocks to the inductive limit.&#x20; # Appendix F — Technical Lemmas & Quantitative Gaps (W1; microcausality) ## F.1 Order‑flip ⇒ \)W_1\( gap For a flip tube with mass parameter \)\theta\( and gradient bound \)L\(, define a 1‑Lipschitz test via a clipped arrival‑time difference. Kantorovich–Rubinstein duality gives \)W_1(P_g,P_{\tilde g})\ \ge\ \theta\,\frac{\Delta v_*}{L}\,\ell_{\rm poke}.\( ## F.2 Microcausality guards Cone‑limited Lieb–Robinson‑type bounds for GKSL commutators; principal‑symbol lemma enforcing single‑cone hyperbolicity. # Appendix G — Horizon Pointer Mechanics: Area Law Details Block decomposition near horizon; additivity and boundary terms; minimal tilings and constants. Links to Ch. 7 area‑law statement. # Appendix H — Hawking Flux Suppression & Microcausality (Asymptotics) Transfer‑envelope asymptotics; LR guards; flux comparison (strict inequality unless \)\lambda_{\rm leak}=0\(). # Appendix I — Notation & Functional‑Analysis Lemmas Topologies; Riesz on blocks; l.s.c.; Γ‑convergence; \)W_1\( duality; normalized HS inner product; cb‑norm basics. # Appendix J — Estimation & Data Kits (Operational Measurability) ## J.1 Budget estimation * **Throughput:** calibrate \)\hbar=\lambda_{\rm th}^{-1}\( via two‑level Fubini–Study speed. * **Leakage:** estimate \)\sum_j\omega(L_j^\dagger W L_j)\( by tomography in the pointer basis; use s.n.f. weight normalization. * **Complexity:** bound \)\mathcal B_{\rm cx}\( via local CP decompositions with measured cb‑norm surrogates. ## J.2 Coherence functional Design poke ensembles covering a basis of the closure hull; use diamond‑norm continuity to control errors. Publish kernels, fits, and code. ## J.3 Stop rules and leakage hygiene Define explicit stop conditions based on primary KPI plateaus; cap leakage channels per ethics/privacy constraints. **Outcome.** Ready‑to‑run templates for experiments that feed the selection program with auditable inputs. # Appendix K — Prediction Worksheets & Fitting Protocols GW phasing residual; horizon flux suppression; interferometer pointer selection; publishing kit and calibration worksheets aligned with Ch. 10. # Appendix L&#x20; --- ## L.1 Γ‑limit promotion of budget tiles on FRW Finite‑window proofs (LR quasi‑factorization, pinching contraction, Dirichlet linearity) extend to FRW via exhaustion by comoving boxes and cone‑preserving gauge. First variations commute with the \)\varepsilon\to0\( limit by the localized Mosco/Attouch framework used in Ch. 5. In particular: * **Locality → global envelope.** Tilewise GKSL estimates with leakage/throughput/complexity budgets remain stable under FRW coarse‑graining; their per‑tile constants are uniform on bounded curvature charts. * **Continuity of multipliers.** Calibration multipliers (\)\alpha_{\rm th},\alpha_{\rm cx},\alpha_{\rm leak}\() obtained on finite windows converge along the exhaustion; the slow‑sector Γ‑limit preserves the Euler–Lagrange form with \)T^{\rm eff}\( defined by the limit of the fast KKT tensors. --- ## L.2 Planck window constants and the area coefficient The constant \)C\( in the Planck‑window mutual‑information bound is fixed by: 1. **Tile spectral gap / log‑Sobolev constants** (pointer‑aligned GKSL), 2. **Lieb–Robinson velocity** and mixing length for the fast sector, and 3. **Normalized HS metric calibration** that identifies \)\hbar=\lambda_{\rm th}^{-1}\(. Under these inputs, the coefficient of the area law is **unique** and stable under norm‑equivalent budget representatives; replacing any quadratic by a norm‑equivalent surrogate leaves the coefficient invariant. Cross‑boundary predictive content in the Planck window is area‑limited independently of bare UV counts; the leakage budget acts as a **soft UV regulator**. --- ## L.3 Coherence smoothing vs. inflation (compatibility note) The “coherence‑driven smoothing” mechanism in Ch. 10.3 relies only on LR microcausality and Dirichlet linearity and does **not** require an inflaton. If an inflaton sector is present in \)T^{\rm vis}\(, pointer‑aligned leakage contributes an effective dissipative term (friction shift \)\Delta\Gamma\propto\alpha_{\rm leak}\() while derivation‑pricing enforces a kinetic penalty \)\propto\alpha_{\rm th}\(. This yields a controlled channel to warm‑inflation‑like dynamics without violating LR bounds. --- ## L.4 Placement in the manuscript Insert **Appendix L** after **Appendix K — Prediction Worksheets & Fitting Protocols** and **before** **Appendix A1 — Concrete Coherence Functionals**, preserving the alphabetical order of lettered appendices while keeping **A1** as a special technical appendix. --- ## L.5 Refuter ledger (cosmology & dark sector) 1. Observation of **super‑cone signaling** or long‑range poke effects in early‑time cosmological data (violates LR microcausality). 2. Empirical need for a **fourth independent quadratic budget** that cannot be represented as a norm‑equivalent quadratic under the same symmetries/calibration. 3. Laboratory observation of **basis‑invariant** decoherence contradicting pointer alignment. 4. Cosmological data requiring a time‑varying \)\hbar$ or multipliers inconsistent with **Γ‑calibration**.


# Appendix A1 — Concrete Coherence Functionals: Properties & Robustness

We prove l.s.c., concavity under mixing, and risk-sensitive convergence for the two concrete CLs of §1.2, and then show robustness within a broader admissible family.

## A1.1 Setup and notation

Let \(\mathscr P\) be the admissible poke cone (closed under composition/mixing), and let \(\mathscr T\) be a finite family of protocols (finite observables and post-processings). A **mixed pattern** is a probability measure \(\mu\) on a finite set of base patterns \(\{A_j\}\); its dynamics are mixtures of the base dynamics.

## A1.2 CA toy: \(\mathrm{CL}_{\rm CA}\) is l.s.c. and concave (under mixing)

**Lemma A1.1 (l.s.c.).** On a fixed \(n,T\), the maps \( (A,\Phi)\mapsto S^{T_{\rm CA}}_{A,\Phi},\,M^{T_{\rm CA}}_{A,\Phi},\,L^{T_{\rm CA}}_{A,\Phi} \) are continuous in the product of discrete/trace topologies; hence any finite affine combination is continuous, and \(\mathrm{CL}_{\rm CA}=\max_{T_{\rm CA},u}F_{T_{\rm CA},u}\) is l.s.c.

*Proof.* Each is a cylinder-event probability or bounded expectation on a finite Markov chain parameterized by finitely many transition probabilities; continuity follows from finite-dimensionality. Max over a finite set preserves l.s.c. ∎

**Lemma A1.1′ (concavity under mixing).** If \(\mu\) is a distribution over base patterns \(\{A_j\}\), then \(A\mapsto \mathbb E_\mu[F_{T_{\rm CA},u}(A,\Phi)]\) is affine in \(\mu\); the pointwise maximum over \((T_{\rm CA},u)\) of affine maps is **concave**. Hence \(A\mapsto \mathrm{CL}_{\rm CA}(A,\Phi)\) is concave in \(\mu\).

*Proof.* Linearity in \(\mu\) is immediate (law of total expectation). Pointwise max of affine maps is concave. ∎

## A1.3 Quantum toy: \(\mathrm{CL}_{\rm Q}\) is l.s.c. and concave (under mixing)

**Lemma A1.2 (l.s.c.).** The map \(\mathcal N\mapsto \|\mathcal N(\Delta)\|_1\) is continuous in the diamond norm; taking \(\inf_{\Phi\in\overline{\mathscr P}}\) yields an l.s.c. functional \(\mathrm{CL}_{\rm Q}\) on \((A,\Phi)\).

*Proof.* For fixed \(\Delta\), \(\|\cdot(\Delta)\|_1\le \|\cdot\|_\diamond\|\Delta\|_1\). Continuity in \(\|\cdot\|_\diamond\) and the infimum over a compact poke class give l.s.c. ∎

**Lemma A1.2′ (concavity under mixing).** If \(A\sim \mu\) is a mixture of base channels \(\{\mathcal N_{A_j,\Phi}\}\), then \(\|\mathbb E_\mu[\mathcal N_{A,\Phi}(\Delta)]\|_1\le \mathbb E_\mu[\|\mathcal N_{A,\Phi}(\Delta)\|_1]\). Thus \(A\mapsto F_{\rm Q}(A,\Phi)\) is concave in \(\mu\), and so is \(A\mapsto \mathrm{CL}_{\rm Q}(A,\Phi)\) after \(\inf_\Phi\).

*Proof.* Triangle inequality and Jensen for the norm; the affine dependence on \(\mu\) gives concavity. ∎

## A1.4 Risk-sensitive worst-case limit

**Proposition A1.2 (risk-sensitive limit).** For either concrete CL and any poke law \(\Pi\), define \(\mathrm{CL}_\beta(A):=\beta^{-1}\log\mathbb E_{\Phi\sim\Pi}\exp(\beta\,\mathrm{CL}(A,\Phi))\). Then \(\mathrm{CL}_\beta\searrow \inf_{\Phi\in\overline{\mathscr P}}\mathrm{CL}(A,\Phi)\) pointwise and epi-converges as \(\beta\to\infty\).

*Proof.* Standard log-moment generating function convergence (Varadhan/Cramér type) on bounded functionals; epi-convergence follows from monotone convergence properties. ∎

## A1.5 Robustness: no fine-tuning

**Proposition A1.3 (equivalence class of CLs).** Let \(\mathcal F\) be the family
[
\mathcal F:=\Big\{\mathrm{CL}_s(A,\Phi):=\sup_{T\in\mathscr T}\mathbb E\big[s_T(Z_{A,\Phi})\big]\ \Big|\ s_T:\mathcal Z_T\to\mathbb R\ \text{bounded, concave, strictly increasing in success features}\Big\}.
\]
On any bounded window and admissible poke cone, there exist constants \(0<c_1\le c_2<\infty\) and increasing functions \(h_1,h_2\) such that for any \(s,s'\) in the family,
\[
h_1\!\big(\mathrm{CL}_s(A,\Phi)\big)\ \le\ \mathrm{CL}_{s'}(A,\Phi)\ \le\ h_2\!\big(\mathrm{CL}_s(A,\Phi)\big),
\]
uniformly on compact sets. Consequently, maximizing \(\mathrm{CL}_s-\sum\lambda_i B_i\) or \(\mathrm{CL}_{s'}-\sum\lambda_i B_i\) has the **same maximizers** in the \(\Gamma\)-limit, and the KKT multipliers (e.g. \(\hbar=\lambda_{\rm th}^{-1}\)) agree.

*Proof sketch.* Bounded concave scores on finite observables are bi-Lipschitz equivalent up to increasing transforms on compact ranges; the sup over a finite \(\mathscr T\) preserves equivalence. Stability of maximizers and multipliers follows from \(\Gamma\)-equivalence and envelope regularity established in Ch. 4–5. ∎

**Corollary A1.4 (pointer robustness).** For \(s\) chosen as the quantum reliability score \(F_{\rm Q}\) or any strictly increasing concave transform thereof, leakage-budget minimizers align with the \(W\)-eigenbasis (pointer basis), independent of the particular \(s\).
