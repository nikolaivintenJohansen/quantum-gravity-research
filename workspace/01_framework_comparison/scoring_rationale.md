# Ranking rubric and score rationale

## Ordinal rubric

- 0: absent or contradicted.
- 1: conceptual proposal with severe unresolved gaps.
- 2: partial or special-case result, with an essential bridge missing.
- 3: substantive programmatic evidence, still materially incomplete.
- 4: strong controlled evidence in a delimited domain.
- 5: established and technically controlled throughout the criterion's stated domain.

The numbers summarize the retrieved evidence; they are not probabilities, Bayes factors, or measurements. Differences below roughly 0.25 should not be treated as decisive. Input scores live in `data/framework_scores.csv` and weights in `data/ranking_weights.csv`.

## Fixed baseline weights

| Criterion | Weight | Rationale |
|---|---:|---|
| Consistency with quantum theory | 0.20 | A bridge must retain superposition, probabilities, and controlled quantum dynamics. |
| Recovery of GR at large scales | 0.25 | This is the central non-negotiable macroscopic limit. |
| Conservation laws and causality | 0.15 | Universal stress–energy coupling and causal stability are essential. |
| Mathematical clarity | 0.15 | Precise variables, dynamics, and domains are prerequisites for checks. |
| Testability | 0.10 | Direct Planck-scale access is difficult, but discriminatory consequences still matter. |
| Feasibility of concrete computation | 0.15 | The program must produce reproducible, falsifiable intermediate results. |

The weights sum exactly to 1 and remain fixed across every framework.

## Alternative weights

The `test_and_compute` scenario sets weights to 0.15, 0.15, 0.10, 0.10, 0.25, and 0.25 in the same order. It asks how the ranking changes when near-term discrimination and tractable computation are emphasized. It also sums exactly to 1 and is applied uniformly.

## Per-framework rationale

- **Causal sets (3, 2, 4, 4, 2, 4).** Clear discrete causal kinematics and continuum operator limits support clarity, causality, and computation. Full dynamics, matter backreaction, and GR recovery remain incomplete.
- **LQG/spin foams (4, 2, 3, 4, 1, 3).** Quantum kinematics are mathematically mature and background independent; full dynamics and controlled infrared QFT/GR recovery remain the main penalties. Proposed observational signatures are not yet robust discriminants.
- **CDT (3, 3, 4, 4, 2, 4).** The causal lattice path integral and transfer-matrix/Monte Carlo machinery are concrete, with nontrivial macroscopic phases. A controlled 4D continuum limit and Lorentzian observable reconstruction remain open.
- **Tensor-network geometry (4, 2, 2, 4, 1, 5).** Finite quantum systems, entropies, and recovery maps are exceptionally explicit. The low scores reflect missing time-dependent, causal, universal gravitational dynamics and limited non-AdS phenomenology.
- **Asymptotic safety (4, 3, 3, 3, 2, 4).** Functional RG supplies a direct continuum computational program and candidate fixed points. Truncation/regulator dependence and Lorentzian unitarity prevent stronger claims.
- **String/gauge–gravity duality (5, 4, 4, 3, 1, 2).** Special-background quantum consistency, low-energy gravity, dualities, and black-hole microstate results are unusually strong. Vacuum realism, background generality, direct tests, and lightweight computation score lower.
- **Emergent family (2, 2, 2, 2, 2, 3).** Several mechanisms reproduce Einstein/Newton equations under assumptions, but the family lacks a shared microtheory and must meet universal-coupling, nonlocality, unitarity, and falsifiability requirements.
- **Gravitational EFT (4, 5, 5, 5, 2, 5).** It is the controlled infrared standard, with transparent power counting, conservation, and GR recovery. Its quantum-consistency score is 4 rather than 5 because control is explicitly cutoff-limited. `is_uv_candidate=false` prevents category error.

## Required interpretation rule

Report both the overall ranking and the UV-candidate-only ranking. EFT may lead overall, but it cannot be selected as the microscopic answer. A change in the UV leader between scenarios is evidence of weight sensitivity, not a reason to tune weights after seeing the outcome.
