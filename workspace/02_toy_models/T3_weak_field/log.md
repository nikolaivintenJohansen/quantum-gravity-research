# T3 log — weak-field GR/EFT benchmark

Status: **passed inside its explicit weak-field domain; not a UV completion**.

## Hypothesis

For metric signature \((-+++)\), \(g_{00}=-(1+2\Phi/c^2)\), nonrelativistic \(T_{00}\simeq\rho c^2\), and a static weak field, the \(00\) Einstein equation reduces to

\[
\nabla^2\Phi=4\pi G\rho.
\]

The generic linearized Einstein tensor must also satisfy \(k^\mu G^{L}_{\mu\nu}=0\), the Fourier-space linearized contracted Bianchi identity. This is the conservation benchmark that later discrete or hybrid sources must match. The interpretation of GR as a controlled low-energy quantum EFT is sourced to [Donoghue (1994), arXiv:gr-qc/9405057](https://arxiv.org/abs/gr-qc/9405057) and [Burgess (2003), arXiv:gr-qc/0311082](https://arxiv.org/abs/gr-qc/0311082).

## Variables, units, assumptions, and command

- \(G\): dimensions \(L^3M^{-1}T^{-2}\); \(\rho\): \(ML^{-3}\); \(\Phi\): \(L^2T^{-2}\).
- Weak-field parameter: \(\epsilon=|2\Phi/c^2|=r_s/r\), with \(r_s=2GM/c^2\).
- Sweep: \(r/r_s=10,30,100,300,10^3,10^4,10^6,10^8\).
- Nominal omitted second-order scale: \(\epsilon^2\). This is a power-counting indicator, not an exact error bound for every observable.
- Static source for Newtonian matching; generic Fourier metric perturbation for the Bianchi identity.
- No randomness.

Command: MPLCONFIGDIR=python-code/.mplconfig python-code/.venv/bin/python python-code/toy_models/t3_weak_field.py

## Results

- Exact symbolic Poisson coefficient: \(4\pi G\rho\).
- Point-mass potential: \(-GM/r\).
- Radial acceleration: \(-GM/r^2\).
- Gauss flux: \(4\pi GM\).
- Generic linearized Bianchi residuals: \((0,0,0,0)\).
- Dimensional checks: both sides of Poisson's equation have \(T^{-2}\); both sides of Einstein's equation have \(L^{-2}\).
- Domain sensitivity: at \(10r_s\), \(\epsilon=0.1\) and the nominal second-order scale is \(10^{-2}\); at \(10^3r_s\), they are \(10^{-3}\) and \(10^{-6}\), respectively.

## Required checks

- **Dimensional analysis:** passed exactly using mass–length–time exponent arithmetic.
- **Covariance:** full covariance is inherited by the Einstein equation but was not rederived. The explicit linearized Bianchi identity is gauge-independent and passed for a generic symmetric perturbation.
- **Local energy–momentum conservation:** \(k^\mu G^L_{\mu\nu}=0\) passed symbolically, so a consistent linear source must obey \(k^\mu T_{\mu\nu}=0\).
- **Causality/stability:** the static Poisson limit does not test hyperbolic propagation or stability; these remain outside T3.
- **Unitarity:** not tested by a classical linearized field equation. EFT unitarity below cutoff remains a literature-backed requirement, not a result of this script.
- **Newtonian and weak-field GR recovery:** passed exactly.
- **Semiclassical behavior:** T3 defines the classical part of the target; quantum matter expectation values and fluctuations are not included.
- **Horizon entropy:** not applicable because \(r\gg r_s\) is required; the model is invalid near a horizon.
- **Parameter sensitivity:** explicit and monotone in \(r_s/r\).
- **Wolfram/Python cross-check:** both systems independently yield the Poisson coefficient, point-source flux, and four zero Bianchi residuals.

## Failure conditions and conclusion

The benchmark would fail under a wrong Einstein-equation normalization, dimensional mismatch, nonzero Bianchi residual, or loss of weak-field control. None occurred. T3 is the mandatory infrared target for later models; it supplies no microscopic degrees of freedom and cannot be ranked as a UV solution.

Canonical outputs: results/t3_weak_field/.
