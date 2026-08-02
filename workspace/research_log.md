# Research log

This file is append-only. Timestamps use ISO 8601 with an explicit UTC offset.

## 2026-08-02T15:44:47-04:00 — Program initialization and preflight

### Tried

- Read and adopted the attached Quantum–Gravity Bridge Research Agent objective.
- Inspected the repository and preserved the pre-existing untracked `AGENTS.md`.
- Checked the local Wolfram CLI, the connected Wolfram kernel, system and bundled Python runtimes, required Python packages, Git, host OS, and outbound literature access.
- Created an isolated Python 3.12 environment and installed/froze the requested scientific stack.
- Ran independent elementary symbolic smoke tests in Wolfram Language and SymPy.

### Found

- No local `wolframscript` is available, but a stateless Wolfram Language 15.0.0 kernel is connected and passed the smoke test.
- The system Python was unsuitable; the workspace virtual environment is functional with exact dependency pins.
- Direct arXiv access works. The arXiv MCP skill is present but its MCP methods are not exposed, so direct primary-source retrieval is the documented fallback.

### Judgment calls

- Selected the bundled CPython 3.12.13 runtime over macOS system Python 3.9.6 because the former is current, isolated from the OS, and compatible with the installed scientific wheels.
- Kept canonical executable code in `python-code/` and `wolfram-notebooks/` to honor repository policy; `workspace/` will hold phase records and model-local provenance pointers.
- Will begin comparison with fixed, explicitly justified criteria and only choose toy models after comparison/ranking evidence is saved. This avoids prematurely favoring a framework.

### Next

- Retrieve a bounded set of load-bearing primary sources/reviews for each framework.
- Write the framework comparison with claim-level citations, obstacles, tractable toy models, and tests.

## 2026-08-02T16:03:00-04:00 — Framework evidence and comparison

### Tried

- Retrieved arXiv records for 27 load-bearing papers/reviews spanning causal sets, LQG/spin foams, CDT, tensor-network/holographic geometry, asymptotic safety, string/gauge–gravity duality, emergent/induced gravity, and gravitational EFT.
- Built a claim-level comparison covering degrees of freedom, emergent geometry, matter coupling, GR recovery, obstacles, toy models, and tests.
- Added only retrieved records to `workspace/references/references.bib`; no memory-only citation was used as evidence.

### Found

- None of the candidate UV programs has a complete, empirically confirmed derivation of four-dimensional GR plus standard QFT in the required domain.
- EFT is the most controlled bridge below its cutoff but is explicitly not a microscopic completion.
- The most computationally transparent UV-candidate directions are CDT, causal sets, tensor-network toy codes, and low-order asymptotic-safety truncations; each tests a different missing ingredient.
- String/gauge–gravity duality supplies unusually strong consistency and special-case entropy results, while LQG supplies background-independent quantum geometry; both face a less tractable full low-energy validation step.

### Judgment calls

- Treated emergent/induced/thermodynamic gravity as a heterogeneous family and therefore scored family-level completeness conservatively.
- Included EFT in the numerical ranking as an infrared benchmark but added a separate UV-scope gate so a high score cannot be misreported as UV completion.
- Selected all eight entries before assigning scores to reduce cherry-picking.

### Next

- Encode the fixed weights and scores in a versioned Python script.
- Run baseline and alternative rankings, save CSV/figure outputs, and document score rationales and sensitivity.

## 2026-08-02T16:18:00-04:00 — Ranking and phase checkpoint

### Tried

- Encoded all scores, framework scope flags, and two normalized weight sets as CSV inputs.
- Implemented a deterministic ranking script with bounds, normalization, and UV-scope checks.
- Generated machine-readable rankings and a sensitivity figure; visually inspected the figure.
- Added three tests for input validity, the EFT UV-scope gate, and the documented leader change.

### Found

- Tests: 3 passed.
- EFT leads overall in both scenarios but is not a UV candidate.
- The UV leader changes from string/gauge–gravity duality (baseline 3.45) to CDT (test-and-compute 3.20). The ranking is therefore sensitive to defensible value choices.
- The stable research implication is a shortlist and staged toy-model program, not a declared winning theory.

### Phase checkpoint: framework comparison complete

- Comparison: complete for eight entries with 2–4 designated load-bearing sources each.
- Ranking: complete under fixed baseline and alternative weights.
- Negative result: the evidence and ordinal ranking do not select a robust microscopic winner.
- Decision: proceed to T1 causal-set manifoldlikeness, T2 entanglement/geometry, and T3 weak-field GR/EFT matching before constructing hybrids.

### Next

- Implement T1–T3 with saved code, parameters, units/assumptions, tests, figures, and model logs.
- Escalate only candidates whose toy checks pass their explicitly limited claims.

## 2026-08-02T16:34:00-04:00 — T1 causal-set kinematics

### Tried

- Simulated 500 conditioned Poisson sprinklings across five sizes in a 1+1D causal diamond with seed 20260802.
- Measured ordering fraction, inverted the Myrheim–Meyer dimension relation, and recorded longest chains.
- Checked partial-order axioms and exact invariance of the causal matrix under a finite Lorentz boost in null coordinates.
- Cross-checked analytic ordering fractions and inversion with Wolfram Language 15.

### Found

- All seven Python tests passed after adding T1.
- At (N=1024), the mean ordering fraction is 0.500756 and the mean inferred dimension is 1.998224.
- The narrow kinematic claim passes; no dynamics, conservation, unitarity, matter coupling, or GR recovery has been tested.

### Next

- Implement T2 as an exact six-qubit perfect-tensor/code check, then perturb it while preserving isometry to measure loss of erasure correction and min-cut entropy.

## 2026-08-02T16:49:00-04:00 — T2 perfect tensor and robustness

### Tried

- Constructed the five-qubit code from exact stabilizer projectors and purified its logical leg into a six-qubit tensor.
- Exhaustively checked all subsets of up to three tensor legs and all known erasures of up to two boundary qubits.
- Applied a deterministic isometry-preserving perturbation and measured code and entropy residuals.
- Independently verified the stabilizer algebra and projector ranks in Wolfram exact arithmetic.

### Found

- All 11 Python tests pass after T2.
- Baseline perfect-tensor entropy and erasure residuals vanish to numerical precision.
- At (epsilon=0.20), isometry still holds while the erasure residual reaches 0.136732 and the maximum min-cut entropy deviation reaches 0.037794 bits.
- Negative result: isometry/unitarity alone does not protect the entanglement/geometry dictionary.

### Next

- Implement T3 as the weak-field GR/EFT benchmark with dimensional, Newtonian, Bianchi/conservation, and independent Wolfram checks.

## 2026-08-02T17:04:00-04:00 — T3 weak-field GR/EFT benchmark

### Tried

- Derived the Newtonian limit from the linearized \(00\) Einstein equation.
- Checked mass–length–time dimensions, point-mass acceleration and Gauss flux, and the generic Fourier-space linearized Bianchi identity.
- Swept the weak-field expansion parameter over \(10\le r/r_s\le10^8\).
- Repeated the core symbolic derivations in Wolfram Language.

### Found

- All 15 Python tests pass after T3.
- Both symbolic systems return \(\nabla^2\Phi=4\pi G\rho\), flux \(4\pi GM\), and four zero Bianchi residuals.
- T3 supplies a controlled infrared matching target and explicitly fails to address UV degrees of freedom, horizon physics, or quantum unitarity.

### Toy-model phase checkpoint

- T1 passed only manifoldlike causal kinematics.
- T2 passed exact code/min-cut identities and produced a negative robustness result: isometry alone does not protect them.
- T3 passed dimensional, conservation, and Newtonian weak-field benchmarks inside its domain.
- No toy model independently satisfies the full bridge checklist. A hybrid may now be proposed only if it treats T1/T2 as kinematic ingredients and T3 as a required infrared constraint, with the untested dynamics stated explicitly.

### Next

- Define a minimal compatible hybrid with explicit variables, symmetries, action/update rule, limits, and failure conditions.
- Test only algebraic/finite-dimensional consequences justified by the current ingredients; do not claim full GR recovery.

## 2026-08-02T17:22:00-04:00 — H1 causal-set-regulated scalar EFT

### Tried

- Defined H1 as a finite joint causal-set/real-scalar path sum with the original 2D retarded layer operator and a Benincasa–Dowker geometric term.
- Audited engineering dimensions, order-relabeling covariance, retarded support, real-action variation, and advanced support on chain sizes 3–10.
- Independently derived the three-chain action gradient in Wolfram exact arithmetic.

### Found

- All 18 Python tests pass after H1.
- The retarded operator is order-covariant and strictly past-supported.
- A real quadratic action varies to the symmetric kernel \((B_R+B_R^T)/2\), which has advanced support. This mismatch is nonzero at every tested chain size and grows rather than disappears in the raw matrix norm.
- H1 therefore cannot currently satisfy causal propagation and ordinary conservative/unitary action dynamics simultaneously.

### Judgment and failure record

- H1 is rejected at the first structural gate. No parameter sweep can change the algebraic fact that a single-real-field quadratic form discards the antisymmetric part of its kernel.
- No H2 is introduced merely to combine unused ingredients. T2 already showed that perfect-code geometry needs a protection/selection principle, and the current program has no justified local backreaction rule that supplies one.
- The next credible hybrid direction is a doubled Schwinger–Keldysh/influence-functional causal-set construction with a derived discrete Ward identity. It remains a recommendation, not a result.

### Hybrid phase checkpoint

- Stable hybrid ID used: H1.
- Exact ingredients, postulate, variables, units, symmetry, action, required limits, and failure conditions are recorded.
- Negative result: no proposed hybrid passes causality, conservation, unitarity, and weak-field recovery together.

### Next

- Assemble the executive and full reports with citations, derivations, ranking, model outputs, glossary, and an explicit established/inference/speculation ledger.
- Run a final reproducibility, citation, and artifact audit before committing.

## 2026-08-02T16:36:17-04:00 — Timestamp correction and final reproducibility audit

### Timestamp correction

- The preceding entries labeled 16:49, 17:04, and 17:22 were appended in the correct logical phase order but contain erroneously transcribed wall-clock times later than this verified system timestamp.
- This correction is appended rather than rewriting those records, preserving the log's append-only policy. Treat this entry's timestamp, obtained directly from the host clock, as authoritative for the completion audit.

### Reproduced

- Re-ran the ranking and all four Python model scripts from the repository root.
- Re-ran the full test suite: 18 passed, 0 failed.
- Confirmed all 31 Markdown files have valid local links.
- Confirmed all 30 distinct arXiv identifiers cited in Markdown have matching records among the 30 bibliography entries.
- Confirmed zero unresolved placeholder markers, zero carriage-return-corrupted files, and a clean Git whitespace audit.
- Saved source hashes and the complete machine-readable audit in results/reproducibility_audit.json.

### Final conclusion

- No complete quantum-gravity bridge was derived.
- T1 establishes a limited causal-set kinematic benchmark; T2 establishes exact encoding identities and their fragility; T3 establishes the required weak-field infrared benchmark.
- H1 is rejected because the strictly retarded scalar operator is not the Euler–Lagrange kernel of an ordinary real single-field quadratic action, while symmetrization introduces advanced support.
- The next justified research step is a doubled-field causal response construction with a derived discrete Ward identity and predeclared unitarity, causality, stability, and continuum-limit gates.
