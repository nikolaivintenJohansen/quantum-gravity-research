# H1 — Causal-set-regulated scalar EFT

Status: **speculative finite hybrid, rejected at the first causality/action audit**.

## Ingredients and new postulate

H1 combines:

1. causal-set geometry \((C,\prec)\), local finiteness, density \(\rho=\ell_*^{-d}\), and a Benincasa–Dowker-type geometric action;
2. a real scalar EFT on each fixed causal set, using the retarded causal-set d'Alembertian \(B_R[C]\);
3. the T3 requirement that any continuum limit reproduce conserved weak-field GR/EFT.

The **new postulate** is that geometry and matter are weighted by a single finite joint path sum, so integrating out the scalar changes the relative amplitudes of causal sets rather than treating matter as a test field.

For a finite causal set, the proposed schematic Lorentzian amplitude is

\[
Z_{H1}=\sum_C \mu(C)\int d^N\phi\;
\exp\!\left\{\frac{i}{\hbar}\left[S_{BD}[C]+\frac{v_*}{2}\phi^T
(K_C+m^2I)\phi\right]\right\},
\qquad K_C=\frac{B_R+B_R^T}{2},
\]

with an \(i\epsilon\) prescription required for the oscillatory Gaussian integral. The symmetrized \(K_C\) is not an arbitrary choice: varying a real quadratic form containing \(B_R\) produces only its symmetric part.

## Variables, units, symmetries, and domain

- \(C\): finite locally finite poset; \(N=|C|\).
- \(\ell_*\): discreteness length; \(v_*=\ell_*^d\); \(\rho=\ell_*^{-d}\).
- \(\phi_x\in\mathbb R\): scalar at event \(x\); in \(d=2\), \([\phi]=L^0\) in \(\hbar=c=1\).
- \(B_R\): retarded layer operator, with \([B_R]=L^{-2}\); \(m^2\) has the same dimension.
- In the implemented 2D audit, \(\rho^{-1}B_R\) has diagonal coefficient \(-2\) and past-layer coefficients \((4,-8,4)\), sourced to the generalized causal-set d'Alembertian literature and [Dowker & Glaser (2013), arXiv:1305.2588](https://arxiv.org/abs/1305.2588).
- Exact symmetry: invariance under order relabeling. Statistical Lorentz invariance is inherited only for a Poisson-sprinkled ensemble.
- Implemented domain: finite chains in 1+1D, used solely to audit action versus retarded support. It is not a gravitational phenomenology model.

## Required limits

- **Classical/GR limit required:** in \(d=4\), ensemble averages of the geometric and matter variations must converge to \(G_{\mu\nu}+\Lambda g_{\mu\nu}=8\pi G T_{\mu\nu}\), including the T3 Bianchi/Newtonian checks. Not demonstrated.
- **Quantum/QFT limit required:** conditional on a manifoldlike causal set, scalar correlation and commutator functions must converge to unitary curved-spacetime QFT with causal propagation. Not demonstrated.
- **Backreaction required:** the geometry-dependent scalar determinant must produce a conserved discrete stress response under allowed order variations. No satisfactory discrete Ward identity is supplied.

## Audit result

On the three-element chain, in units \(\rho=1\),

\[
B_R=\begin{pmatrix}-2&0&0\\4&-2&0\\-8&4&-2\end{pmatrix}.
\]

It is strictly retarded and nonsymmetric. For a real field,

\[
\frac{\partial}{\partial\phi}\left(\frac12\phi^TB_R\phi\right)
=\frac{B_R+B_R^T}{2}\phi.
\]

The resulting action kernel has nonzero advanced support. Keeping \(B_R\) as a non-Hermitian quadratic generator instead would not provide ordinary conservative/unitary evolution. Python verifies this across chain sizes 3–10 and exact order relabelings; Wolfram independently verifies the three-chain variation.

## Physics guardrail audit

- Dimensional analysis: **pass** in the 2D diagnostic.
- Order covariance/relabeling: **pass** exactly.
- Causality: \(B_R\) **passes**, but the real action kernel **fails** by acquiring advanced support.
- Conservation: **fail/not defined**; no discrete Ward identity for backreaction.
- Stability: **not tested**; literature already warns that operator stability depends on dimension/operator family.
- Unitarity: **fail/not established** for a strictly retarded non-Hermitian kernel.
- Newtonian/weak-field GR: **fail/not derived**.
- Standard semiclassical QFT: **fail/not derived**.
- \(S=A/4\): **not applicable**; no horizon sector.
- Parameter sensitivity: chain-size dependence recorded, but it does not cure the structural obstruction.

## Failure conditions and decision

H1 is rejected if no formulation simultaneously supplies a causal kernel, a conservative/unitary quantum theory, a discrete conservation identity, and the T3 continuum limit. The naive single-real-field action fails the first pair already, so escalation stops.

The most productive repair is not parameter tuning. It is to formulate a doubled Schwinger–Keldysh/influence-functional causal-set theory or another explicitly unitary construction, then derive a discrete Ward identity before reattempting geometry backreaction. That is a future research direction, not a result established here.
