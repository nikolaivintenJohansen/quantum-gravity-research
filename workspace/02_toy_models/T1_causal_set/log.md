# T1 log — causal-set manifoldlikeness

Status: **passed its limited kinematic claim; not a GR or dynamics test**.

## Hypothesis

A uniform sprinkling conditioned on (N) elements in a 1+1D Minkowski Alexandrov interval should have ordering fraction

\[
r(d)=\frac{\Gamma(d+1)\Gamma(d/2)}{2\Gamma(3d/2)},
\]

so (r(2)=1/2), and numerical inversion should recover (d=2) as (N) grows. The ordering-fraction definition and Myrheim–Meyer interpretation are documented in [Surya (2019)](https://link.springer.com/article/10.1007/s41114-019-0023-1).

## Parameters and command

- Null coordinates (u,v\in[-1,1]); the half-extent is the dimensionless unit.
- Sizes: (N=64,128,256,512,1024).
- Repeats: 100 independently generated conditioned sprinklings per size.
- NumPy generator: PCG64 via `default_rng`.
- Seed: 20260802.
- No physical identification with the Planck scale is made.

```bash
MPLCONFIGDIR=python-code/.mplconfig python-code/.venv/bin/python python-code/toy_models/t1_causal_set.py
```

## Results

| N | Mean ordering fraction | Mean inferred dimension | Mean longest chain |
|---:|---:|---:|---:|
| 64 | 0.491379 | 2.028330 | 13.02 |
| 128 | 0.500231 | 2.001287 | 19.27 |
| 256 | 0.496950 | 2.009133 | 27.94 |
| 512 | 0.500127 | 2.000044 | 40.73 |
| 1024 | 0.500756 | 1.998224 | 59.52 |

The plotted error bars are 95% normal-approximation intervals for the mean across repeats. They are descriptive Monte Carlo errors, not uncertainty in the underlying theory.

## Required checks

- **Dimensional analysis:** coordinates are dimensionless in units of the diamond half-extent; the ordering fraction and inferred dimension are dimensionless.
- **Covariance replacement:** the finite causal relation is exactly unchanged under the tested null-coordinate boost (u\mapsto e^{\eta}u, v\mapsto e^{-\eta}v) with (eta=1.7). This is a kinematic check, not proof of a quantum measure's covariance.
- **Causality:** irreflexivity and transitivity passed exactly for the validation sample.
- **Stability/sensitivity:** the mean ordering fraction stays within 0.02 of 0.5 at every tested size; the mean inferred dimension is within 0.2 of 2 for (N\ge128). Finite-size scatter decreases with (N).
- **Conservation:** not applicable because T1 has no matter or dynamics.
- **Unitarity:** not applicable because T1 has no quantum amplitudes or evolution.
- **Newtonian/weak-field GR:** not tested. Passing T1 cannot support a claim of GR recovery.
- **Semiclassical behavior:** only manifoldlike kinematics are tested.
- **Horizon entropy:** not applicable.
- **Wolfram/Python cross-check:** Wolfram 15 independently gives (r(2)=1/2), (r(4)=1/10), a monotone integer grid from (d=1) through 10, and inverse (d=2) at (r=1/2).

## Failure conditions and conclusion

The limited hypothesis would fail if causal order were not boost invariant, if the partial-order axioms failed, or if ordering statistics did not converge to the analytic target. None occurred. The broader causal-set bridge still lacks dynamics, matter backreaction, conservation, unitarity, and Einstein/Newtonian recovery here. T1 therefore licenses only a later discrete-field/dynamics test, not a hybrid claim.

Canonical outputs: `results/t1_causal_set/`.
