# Critical framework comparison

Evidence retrieval date: 2026-08-02. The source list below is deliberately bounded to 2–4 load-bearing primary papers or standard reviews per framework. All linked arXiv records were actually retrieved during this phase. Scores are deferred to `ranking.md` so descriptive evidence is not silently converted into numerical judgment.

## Scope and epistemic labels

- **Established here** means a result stated in a retrieved source or a standard mathematical consequence checked against it. It does not mean experimentally confirmed quantum gravity.
- **Programmatic evidence** means a nontrivial result inside a candidate framework, not confirmation that the framework describes nature.
- **Open** means a missing derivation, limit, or validation essential to the present bridge objective.
- **Speculative** means a proposed interpretation or extrapolation, even when mathematically suggestive.

General relativity already couples ordinary matter through (G_{\mu\nu}+\Lambda g_{\mu\nu}=8\pi G T_{\mu\nu}). The shared unresolved issue is the quantum treatment of dynamical geometry and its matter backreaction, not an absence of matter from GR. The Planck length is used as a motivated scale, never as an experimentally established minimum distance.

## Comparison at a glance

| Framework | Fundamental degrees of freedom | Route to geometry/curvature | GR recovery status | Best transparent computation | Central unresolved issue |
|---|---|---|---|---|---|
| Causal sets | Locally finite partially ordered set | Order encodes causal structure; counting encodes volume; discrete d'Alembertian/action estimates curvature | Operators/actions have continuum limits on manifoldlike sprinklings; full dynamical selection of 4D manifoldlike causal sets is open | Poisson sprinkling and causal-matrix observables in 1+1D | Dynamics, manifoldlikeness, matter backreaction, continuum phenomenology |
| Loop/spin foams | SU(2) holonomies, fluxes, spin networks; labeled two-complex histories | Quantum area/volume spectra; spinfoam amplitudes encode histories | Semiclassical and asymptotic evidence exists; controlled full low-energy GR/QFT limit remains open | Small spin networks or 2+1D spin-foam amplitudes | Dynamics, coarse graining, continuum limit, low-energy correlators |
| Causal dynamical triangulations (CDT) | Causally glued Lorentzian simplices | Curvature through Regge action; macroscopic geometry from an ensemble | Extended 4D phases and effective geometries are numerical evidence; continuum critical limit and full GR recovery remain open | 2D transfer matrix or finite triangulation Monte Carlo | Continuum limit, universality, Lorentzian reconstruction/unitarity |
| Tensor-network / entanglement geometry | Tensors, qudits, isometries, boundary many-body states | Network connectivity/minimal cuts encode entanglement and spatial geometry | Exact toy realizations of Ryu–Takayanagi and bulk reconstruction; not a derivation of general 4D dynamical GR | Small holographic code or MERA-like network | Time, dynamics, non-AdS settings, universal matter coupling |
| Asymptotic safety | Metric and matter fields with scale-dependent effective action | Geometry remains metric; couplings run toward a proposed UV fixed point | GR is the intended infrared trajectory; evidence is mainly truncation-dependent functional RG | Einstein–Hilbert truncation beta-flow and sensitivity scan | Fixed-point robustness, Lorentzian unitarity, regulator/truncation control |
| String theory / gauge–gravity duality | Strings, branes, worldsheet CFT; dual gauge-theory degrees of freedom | Closed-string spin-2 mode and dual emergent bulk geometry | Low-energy supergravity contains Einstein gravity; strong results in special supersymmetric/AdS settings | Protected spectra, low-dimensional CFTs, matrix or code-inspired models | Realistic vacuum selection, nonperturbative definition in general backgrounds, direct tests |
| Emergent / induced / thermodynamic gravity | Framework-dependent quantum fields or microscopic information variables | Effective action or thermodynamic constitutive relation yields metric dynamics | Einstein equations can follow under strong entropy/local-equilibrium assumptions; microscopic derivation is generally incomplete | Induced Einstein–Hilbert term or entropic Newton-law algebra | Universal coupling, microscopic degrees, locality no-go constraints, falsifiability |
| Gravitational effective field theory | Low-energy metric perturbations plus ordinary quantum fields | The metric is already the geometric field; higher-curvature operators encode short-distance ignorance | Exact by construction at leading order below the cutoff | Weak-field quantum correction and power counting | Not a UV/microscopic completion |

## 1. Causal sets

1. **Objects.** A causal set is a locally finite partially ordered set ((C,\prec)). The order is interpreted as proto-causality and local finiteness as spacetime discreteness. This definition and its Lorentzian motivation are reviewed by [Surya (2019), arXiv:1903.11544](https://arxiv.org/abs/1903.11544).
2. **Emergent geometry.** A causal set is *manifoldlike* only if it admits a faithful approximation by a Lorentzian manifold, commonly modeled by Poisson sprinkling. Causal order supplies conformal geometry and counting supplies volume. Benincasa and Dowker construct retarded scalar operators approaching (\Box-\tfrac12R) on slowly varying fields, thereby defining a discrete curvature/action surrogate [Benincasa & Dowker (2010), arXiv:1001.2725](https://arxiv.org/abs/1001.2725).
3. **Matter–geometry interaction.** Scalar propagation on a fixed causal set is concrete. A mutually backreacting quantum matter–causal-set dynamics is much less developed; fixed-background propagation must not be mistaken for completion of the coupling problem.
4. **Large-scale GR.** **Programmatic evidence:** the cited discrete operator recovers a continuum curvature term on suitable manifoldlike causal sets. **Open:** showing that the quantum dynamics overwhelmingly selects four-dimensional manifoldlike histories with Einstein dynamics.
5. **Obstacles.** Manifold reconstruction, suppression of non-manifoldlike orders, nonlocality forced by Lorentz-compatible discreteness, dynamical measure definition, and controlled matter backreaction.
6. **Toy models.** Poisson sprinkling into a 1+1D causal diamond; ordering fraction, link matrix, longest chains, interval abundance, and a discrete scalar operator. All are finite, visualizable, and test continuum/statistical limits.
7. **Tests.** Lorentz-frame independence in sprinkling statistics; convergence of dimension and d'Alembertian estimators; causal propagation; finite-size sensitivity; and eventual constraints on nonlocal dispersion. These are theoretical validation targets, not current empirical confirmation.

Load-bearing sources: [Surya 2019](https://arxiv.org/abs/1903.11544); [Benincasa & Dowker 2010](https://arxiv.org/abs/1001.2725); [Wallden 2010](https://arxiv.org/abs/1001.4041).

## 2. Loop quantum gravity and spin foams

1. **Objects.** Canonical LQG quantizes holonomies of an SU(2) connection and conjugate fluxes. Spin-network graphs label quantum geometry; spin foams are histories of such data. The mathematical construction and conventional matter couplings are reviewed by [Ashtekar & Lewandowski (2004), arXiv:gr-qc/0404018](https://arxiv.org/abs/gr-qc/0404018), while [Perez (2012), arXiv:1205.2019](https://arxiv.org/abs/1205.2019) reviews the covariant simplicial path-integral formulation.
2. **Emergent geometry.** Area and volume are operators on spin-network states. Curvature/dynamics enter through constraints or spin-foam amplitudes rather than through a fixed background metric.
3. **Matter–geometry interaction.** Gauge fields and fermions can be coupled at the kinematical level. A controlled interacting continuum limit reproducing ordinary curved-spacetime QFT remains part of the open low-energy problem.
4. **Large-scale GR.** **Established within the program:** well-defined background-independent kinematics and semiclassical/asymptotic constructions. **Open:** a unique, controlled full dynamics whose coarse-grained correlation functions reproduce Einstein gravity and QFT across relevant regimes.
5. **Obstacles.** Hamiltonian-constraint and amplitude choices, anomaly control, coarse graining, continuum limit, recovery of local Lorentzian dynamics, and robust phenomenology. The older overview by [Rovelli (1997), arXiv:gr-qc/9710008](https://arxiv.org/abs/gr-qc/9710008) already identifies dynamics as the weak point; later models improve the situation but do not close the full recovery problem.
6. **Toy models.** A single spin-network vertex, area-spectrum calculations, 2+1D Ponzano–Regge-type amplitudes, or small spinfoam asymptotics. The 2+1D sector is especially useful because it separates quantization machinery from propagating-graviton complications.
7. **Tests.** Constraint closure, triangulation/coarse-graining dependence, semiclassical graviton correlators, black-hole entropy, and cosmological effective dynamics. [Bianchi (2012), arXiv:1204.5122](https://arxiv.org/abs/1204.5122) obtains (S=A/4) for a specific non-extremal horizon treatment; this is a framework-specific benchmark, not a universal empirical validation.

Load-bearing sources: [Ashtekar & Lewandowski 2004](https://arxiv.org/abs/gr-qc/0404018); [Perez 2012](https://arxiv.org/abs/1205.2019); [Bianchi 2012](https://arxiv.org/abs/1204.5122); [Ashtekar & Bianchi 2021](https://arxiv.org/abs/2104.04394).

## 3. Causal dynamical triangulations

1. **Objects.** CDT sums over causally glued Lorentzian simplicial manifolds with fixed edge-length assignments and a preferred global foliation in its standard formulation.
2. **Emergent geometry.** Each triangulation carries a Regge discretization of curvature; an ensemble weighted by the discretized Einstein–Hilbert action is sampled. The construction, Wick rotation, transfer matrix, and Monte Carlo moves are set out by [Ambjørn, Jurkiewicz & Loll (2001), arXiv:hep-th/0105267](https://arxiv.org/abs/hep-th/0105267).
3. **Matter–geometry interaction.** Matter fields can live on the triangulations and backreact through the joint path integral. Four-dimensional universality with realistic matter is not established.
4. **Large-scale GR.** **Programmatic evidence:** extended phases with macroscopic effective geometry and computable invariant observables. [Loll (2019), arXiv:1905.08669](https://arxiv.org/abs/1905.08669) reviews the 4D phase structure and geometric observables. **Open:** demonstrate a second-order critical continuum limit and show the resulting effective action is full Lorentzian GR rather than only a minisuperspace-like sector.
5. **Obstacles.** Finite-size scaling, universality, topology/foliation restrictions, locating and controlling a continuum critical surface, analytic continuation, and reconstructing unitary Lorentzian observables.
6. **Toy models.** Exactly soluble 2D CDT transfer matrices; small-volume triangulation enumeration; or a reproducible minisuperspace volume-profile model before attempting Monte Carlo triangulations.
7. **Tests.** Transfer-matrix positivity, phase-transition order, spectral/Hausdorff dimensions, finite-size scaling, effective action fits, and stability after adding matter. [Benedetti (2022), arXiv:2212.11043](https://arxiv.org/abs/2212.11043) emphasizes that reaching GR may require parameter tuning and discusses continuum-limit difficulty.

Load-bearing sources: [Ambjørn, Jurkiewicz & Loll 2001](https://arxiv.org/abs/hep-th/0105267); [Loll 2019](https://arxiv.org/abs/1905.08669); [Benedetti 2022](https://arxiv.org/abs/2212.11043).

## 4. Tensor networks and entanglement-based geometry

1. **Objects.** Finite-dimensional tensors, isometries, qudits, and boundary many-body states; MERA-like layers organize correlations by scale, while holographic codes encode logical bulk degrees into boundary degrees.
2. **Emergent geometry.** Network connectivity and minimal cuts encode spatial distance and entropy. [Ryu & Takayanagi (2006), arXiv:hep-th/0603001](https://arxiv.org/abs/hep-th/0603001) relates boundary entanglement entropy to bulk minimal area in AdS/CFT; [Swingle (2009), arXiv:0905.1317](https://arxiv.org/abs/0905.1317) interprets entanglement renormalization geometrically.
3. **Matter–geometry interaction.** Bulk logical indices can represent matter-like excitations, and their encoding responds to network structure. This is a precise information-theoretic analogue, not yet universal gravitational backreaction.
4. **Large-scale GR.** [Pastawski et al. (2015), arXiv:1503.06237](https://arxiv.org/abs/1503.06237) gives exact toy realizations of Ryu–Takayanagi behavior and redundant bulk reconstruction. **Open:** derive a dynamical Lorentzian metric satisfying Einstein equations for general states, especially outside asymptotically AdS settings.
5. **Obstacles.** Time and causal dynamics, continuum limits, state/network non-uniqueness, realistic dimension and cosmology, universal stress–energy coupling, and separating holographic toy-code features from full gravity.
6. **Toy models.** A small perfect-tensor/HaPPY-like code, a binary MERA graph, minimal-cut entropy, erasure recovery, and perturbations of bond dimensions.
7. **Tests.** Ryu–Takayanagi/min-cut equality where claimed, quantum error-correction recovery, entropy inequalities, locality of reconstructed operators, and stability under tensor perturbations. [Van Raamsdonk (2010), arXiv:1005.3035](https://arxiv.org/abs/1005.3035) motivates connected geometry from entanglement, but its geometric extrapolation is an argument rather than an experimentally verified mechanism.

Load-bearing sources: [Ryu & Takayanagi 2006](https://arxiv.org/abs/hep-th/0603001); [Swingle 2009](https://arxiv.org/abs/0905.1317); [Van Raamsdonk 2010](https://arxiv.org/abs/1005.3035); [Pastawski et al. 2015](https://arxiv.org/abs/1503.06237).

## 5. Asymptotic safety

1. **Objects.** The metric and matter fields remain fundamental continuum variables. Their scale-dependent effective average action (\Gamma_k) evolves under a functional renormalization-group equation.
2. **Emergent geometry.** Geometry is not emergent in the same ontological sense as in causal sets or tensor networks; rather, its couplings and effective dimensional behavior change with scale.
3. **Matter–geometry interaction.** Matter operators and gravitational couplings enter the same theory space, allowing joint fixed-point studies. [Eichhorn (2018), arXiv:1810.07615](https://arxiv.org/abs/1810.07615) reviews gravity–matter results and their open questions.
4. **Large-scale GR.** A UV-safe trajectory must flow into the observed low-energy Einstein–Hilbert regime plus suppressed higher-curvature terms. This is built into candidate trajectories, but a unique realistic trajectory is not established.
5. **Obstacles.** Fixed-point evidence is primarily obtained in truncations; regulator, gauge, and field-parametrization dependence must converge. Lorentzian continuation, reflection positivity/unitarity, and full matter content remain demanding checks.
6. **Toy models.** Einstein–Hilbert truncation with dimensionless (g(k)=k^2G(k)) and (\lambda(k)=\Lambda(k)/k^2); polynomial (f(R)) truncations; stability of fixed points under added operators.
7. **Tests.** Critical-exponent convergence across truncations, regulator sensitivity, compatibility with Standard Model matter, Lorentzian spectral properties, and infrared recovery. [Reuter (1996), arXiv:hep-th/9605030](https://arxiv.org/abs/hep-th/9605030) introduced the nonperturbative flow; [Reuter & Saueressig (2012), arXiv:1202.2274](https://arxiv.org/abs/1202.2274) reviews fixed-point evidence and dimensional flow.

Load-bearing sources: [Reuter 1996](https://arxiv.org/abs/hep-th/9605030); [Reuter & Saueressig 2012](https://arxiv.org/abs/1202.2274); [Eichhorn 2018](https://arxiv.org/abs/1810.07615); [Eichhorn 2022](https://arxiv.org/abs/2201.11543).

## 6. String theory and gauge–gravity duality

1. **Objects.** Fundamental strings, branes, worldsheet conformal fields, and—in dual descriptions—large-(N) gauge-theory degrees of freedom.
2. **Emergent geometry.** The massless closed-string spectrum contains a spin-2 mode interpreted as the graviton; target-space consistency yields gravitational field equations at low energy. Gauge–gravity duality makes a higher-dimensional bulk emergent from nongravitational boundary data in special backgrounds.
3. **Matter–geometry interaction.** Open/closed strings and branes provide matter/gauge sectors coupled consistently to the graviton, although realistic compactification and vacuum selection are model-dependent. [Polchinski (1996), arXiv:hep-th/9611050](https://arxiv.org/abs/hep-th/9611050) reviews D-branes and nonperturbative objects.
4. **Large-scale GR.** Low-energy string effective actions contain supergravity/Einstein terms plus controlled corrections. [Maldacena (1997), arXiv:hep-th/9711200](https://arxiv.org/abs/hep-th/9711200) proposes exact AdS/CFT dualities in particular large-(N) systems. Extrapolation to our cosmology is open.
5. **Obstacles.** Vacuum/compactification selection, moduli and supersymmetry breaking, controlled de Sitter cosmology, background-independent nonperturbative formulation in general spacetimes, and sparse direct empirical discriminants.
6. **Toy models.** Worldsheet beta functions, matrix models, protected supersymmetric observables, low-dimensional CFT dualities, and black-hole microstate counts. These are mathematically rich but usually less lightweight than graph or truncation models.
7. **Tests.** Anomaly cancellation, modular/unitary consistency, duality matching, correct low-energy spectra, black-hole entropy, and controlled corrections. [Strominger & Vafa (1996), arXiv:hep-th/9601029](https://arxiv.org/abs/hep-th/9601029) derives (S=A/4) for a special five-dimensional extremal BPS class; the domain restriction is essential.

Load-bearing sources: [Polchinski 1996](https://arxiv.org/abs/hep-th/9611050); [Maldacena 1997](https://arxiv.org/abs/hep-th/9711200); [Strominger & Vafa 1996](https://arxiv.org/abs/hep-th/9601029).

## 7. Emergent, induced, and thermodynamic gravity

This is a family of mechanisms, not one theory. Scores and conclusions must therefore be interpreted as applying to the family-level evidence, not every member.

1. **Objects.** Depending on the model: ordinary quantum fields whose fluctuations induce a gravitational action, microscopic information variables, or thermodynamic state variables.
2. **Emergent geometry.** [Visser (2002), arXiv:gr-qc/0204062](https://arxiv.org/abs/gr-qc/0204062) reviews Sakharov-style induction of gravitational terms from quantum fields. [Jacobson (1995), arXiv:gr-qc/9504004](https://arxiv.org/abs/gr-qc/9504004) derives Einstein's equation as an equation of state from local horizon entropy and (\delta Q=T\,dS).
3. **Matter–geometry interaction.** Matter energy flux or quantum effective action sources the emergent equation. The hard requirement is universal coupling to the full conserved stress tensor, not merely a Newton-like force for selected matter.
4. **Large-scale GR.** Einstein or Newton equations can be reproduced under stated assumptions; [Verlinde (2010), arXiv:1001.0785](https://arxiv.org/abs/1001.0785) is an influential entropic proposal. Deriving the assumptions and all relativistic dynamics from a concrete unitary microtheory remains open.
5. **Obstacles.** Undefined or nonunique microphysics, universal coupling/equivalence principle, causal and unitary dynamics, entropy accounting, radiative stability, and empirical distinguishability. [Marolf (2014), arXiv:1409.2509](https://arxiv.org/abs/1409.2509) shows that emergent nonlinear gravity with universal energy coupling requires kinematic nonlocality under broad assumptions; any local microscopic hybrid must confront this failure condition.
6. **Toy models.** Heat-kernel induction of an Einstein–Hilbert term, Jacobson's local Rindler algebra, or the entropic derivation of Newton's inverse-square law with every assumption exposed.
7. **Tests.** Exact conservation and equivalence principle, gravitational-wave speed/polarizations, entropy normalization, causal response, positivity/unitarity, and whether the proposal produces deviations rather than only redescribing GR.

Load-bearing sources: [Jacobson 1995](https://arxiv.org/abs/gr-qc/9504004); [Visser 2002](https://arxiv.org/abs/gr-qc/0204062); [Verlinde 2010](https://arxiv.org/abs/1001.0785); [Marolf 2014](https://arxiv.org/abs/1409.2509).

## 8. Gravitational effective field theory

1. **Objects.** A low-energy metric field and ordinary quantum matter, organized by a local derivative expansion constrained by diffeomorphism symmetry.
2. **Emergent geometry.** Geometry is not emergent; the Einstein–Hilbert term is the leading operator, followed by higher-curvature terms suppressed by a cutoff.
3. **Matter–geometry interaction.** Standard stress–energy coupling is retained and loop corrections are computed consistently below the cutoff.
4. **Large-scale GR.** This is the strongest entry precisely because GR is the leading low-energy term. [Donoghue (1994), arXiv:gr-qc/9405057](https://arxiv.org/abs/gr-qc/9405057) isolates parameter-free long-distance quantum corrections from unknown short-distance coefficients.
5. **Obstacles.** It does not specify the ultraviolet microscopic degrees of freedom and loses predictivity when the derivative expansion ceases to be controlled. Therefore it cannot by itself satisfy the goal's microscopic-completion requirement.
6. **Toy models.** Dimensional power counting, the weak-field propagator, leading nonanalytic corrections to the Newtonian potential, and curvature-squared perturbations.
7. **Tests.** Ward identities, order-by-order unitarity below cutoff, decoupling, conservation, weak-field/Newtonian recovery, and matching from any proposed UV candidate. [Burgess (2003), arXiv:gr-qc/0311082](https://arxiv.org/abs/gr-qc/0311082) provides a pedagogical treatment.

Load-bearing sources: [Donoghue 1994](https://arxiv.org/abs/gr-qc/9405057); [Burgess 2003](https://arxiv.org/abs/gr-qc/0311082).

## Phase conclusion before ranking

No retrieved source establishes a complete, empirically confirmed microscopic quantum theory of four-dimensional spacetime. The comparison instead identifies complementary strengths:

- gravitational EFT is the non-negotiable infrared benchmark but not a UV completion;
- string/gauge–gravity duality has the deepest examples of quantum consistency and special-case black-hole microphysics, but limited direct testability and background generality;
- asymptotic safety and CDT offer comparatively direct scale/continuum computations, with truncation or continuum-limit gaps;
- causal sets and LQG make background independence and quantum geometry explicit, while full low-energy recovery remains open;
- tensor networks provide exceptionally transparent entanglement/geometry and error-correction toy models but presently encode only part of gravitational dynamics;
- emergent-gravity claims are too heterogeneous to treat as a single completed framework and face a sharp universal-coupling/nonlocality hurdle.

The ranking will use these distinctions and will apply an explicit **UV-scope gate** so EFT's benchmark strength does not answer a question it was never designed to answer.
