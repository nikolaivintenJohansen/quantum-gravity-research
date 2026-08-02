# Executive summary

## Outcome

This project did not derive a complete bridge from a discrete quantum microstructure to classical general relativity. It did produce a reproducible comparison, three independently checked toy calculations, and a concrete hybrid-model rejection criterion. The strongest defensible conclusion is therefore negative but useful: several candidate programs supply complementary ingredients, yet joining them requires more than placing a quantum field on a causal substrate.

The first hybrid tested here combines a causal-set path sum with a retarded scalar operator. It fails at the first structural gate. The retarded operator is not the kernel obtained by varying an ordinary real quadratic action; symmetrizing it restores an action principle but introduces advanced support. Consequently, this ansatz does not simultaneously establish microscopic causality, conservative real-action dynamics, and a controlled general-relativistic limit.

## What was completed

- A documented environment preflight covering Python, package versions, the connected Wolfram Language kernel, and network access.
- A source-based comparison of causal sets, loop quantum gravity and spin foams, causal dynamical triangulations, tensor networks, asymptotic safety, string theory and holography, emergent or entropic gravity, and gravitational effective field theory.
- A transparent weighted ranking with a second weighting scheme that exposes sensitivity to research priorities.
- Three reproducible toy models:
  - T1: Poisson-sprinkled causal orders and an ordering-fraction dimension estimator.
  - T2: a six-leg perfect tensor built from the five-qubit code, with exact erasure checks and controlled perturbations.
  - T3: the weak-field Newtonian limit, including dimensional, Bianchi-identity, and domain-of-validity checks.
- H1: a formally stated causal-set-regulated scalar hybrid, followed by an explicit failure audit.
- Independent Wolfram Language cross-checks for every model, plus Python tests and saved metadata.

## Framework comparison and ranking

The ranking separates a controlled low-energy benchmark from proposed ultraviolet completions. Gravitational effective field theory scores highest overall because it is mathematically controlled and empirically anchored, but it is not itself a microscopic completion.

Under the baseline weights, the ultraviolet shortlist begins with string theory and holography, causal dynamical triangulations, and asymptotic safety. Under weights favoring near-term testability and computation, the ordering changes to causal dynamical triangulations, asymptotic safety, and causal sets. That instability is substantive: the evidence does not justify declaring one ultraviolet framework the winner.

The ranking is a decision aid, not a measurement. Scores encode documented judgments, while the alternative weighting shows how those judgments affect the result.

![Framework ranking sensitivity](../../results/framework_ranking_sensitivity.png)

## Model-level findings

### T1: causal order

A Lorentz-compatible Poisson sprinkling in a two-dimensional causal diamond reproduces the expected ordering fraction. At 1,024 sprinkled points and 100 deterministic-seed repetitions, the mean ordering fraction is 0.500756 and the inferred dimension is 1.998224. Relabeling invariance, transitivity, irreflexivity, and an exact boost-invariance check pass.

This establishes only a kinematic consistency check. It does not supply quantum dynamics, an Einstein limit, matter, or phenomenology.

### T2: perfect tensor

The five-qubit code purification gives a six-qubit perfect tensor. Exact checks confirm the expected isometry and correctability properties for the relevant partitions. A controlled unitary perturbation preserves the global isometry exactly while degrading local erasure recovery and flat entanglement structure.

This shows that tensor-network geometry can be precise but fragile under deformations. It does not derive bulk dynamics or Einstein equations.

### T3: weak-field recovery target

Symbolic calculations reproduce the Poisson equation, the point-mass potential, inverse-square acceleration, Gauss flux, and the linearized Bianchi identity. The approximation parameter is the compactness ratio r_s/r, so the weak-field expansion is explicitly controlled only when r is much larger than the Schwarzschild radius r_s.

This model is an infrared benchmark that a microscopic proposal must recover. It is not a microscopic account of gravity.

### H1: causal scalar hybrid

For finite causal sets, the tested retarded d'Alembertian is strictly lower triangular apart from its diagonal. Varying a real quadratic action built from that operator produces its symmetric part, which necessarily contains advanced support. Directly using the nonsymmetric operator as an equation of motion does not by itself provide a conservative or unitary theory.

H1 is therefore rejected before phenomenological fitting. No second hybrid was introduced, because doing so without a justified microscopic rule would add parameters rather than knowledge.

![Retarded and action-derived kernels](../../results/h1_causal_scalar/retarded_vs_action_kernel.png)

## Candid conclusion

The calculations support a modular research strategy:

1. Treat gravitational effective field theory and the weak-field limit as non-negotiable infrared targets.
2. Use discrete causal structure as a candidate kinematic regulator, not as evidence of completed dynamics.
3. Use quantum-code and tensor-network ideas to study encoding and emergence, while testing robustness rather than assuming it.
4. Require any hybrid to pass structural gates for covariance, causality, conservation or unitarity, and continuum recovery before discussing observational signatures.

The next justified calculation is to derive, rather than posit, a conservative causal propagator prescription on an ensemble of causal sets or to prove that no ordinary real single-field action can provide one. A closed-time-path or doubled-field construction is a plausible comparison target, but it must be introduced with its additional degrees of freedom and boundary conditions made explicit.

## Where to continue

- [Full report](full_report.md)
- [Framework comparison](../01_framework_comparison/framework_comparison.md)
- [Ranking rationale](../01_framework_comparison/scoring_rationale.md)
- [Append-only research log](../research_log.md)
- [Bibliography](../references/references.bib)
- [Environment report](../00_environment_report.md)
- [Reproducibility audit](../../results/reproducibility_audit.json)

Key primary sources include the causal-set reviews and nonlocal operators of [Surya](https://arxiv.org/abs/1903.11544), [Benincasa and Dowker](https://arxiv.org/abs/1001.2725), and [Dowker and Glaser](https://arxiv.org/abs/1305.2588); the loop and spin-foam reviews of [Ashtekar and Lewandowski](https://arxiv.org/abs/gr-qc/0404018) and [Perez](https://arxiv.org/abs/1205.2019); the CDT reviews of [Loll](https://arxiv.org/abs/1905.08669) and [Benedetti](https://arxiv.org/abs/2212.11043); the holographic and tensor-network constructions of [Maldacena](https://arxiv.org/abs/hep-th/9711200), [Swingle](https://arxiv.org/abs/0905.1317), and [Pastawski et al.](https://arxiv.org/abs/1503.06237); and the effective-field-theory treatment of [Donoghue](https://arxiv.org/abs/gr-qc/9405057) and [Burgess](https://arxiv.org/abs/gr-qc/0311082).
