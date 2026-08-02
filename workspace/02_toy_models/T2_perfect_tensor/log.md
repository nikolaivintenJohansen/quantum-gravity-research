# T2 log — perfect tensor and erasure code

Status: **exact benchmark passed; robustness test failed as intended; no spacetime dynamics**.

## Hypothesis

The purification of the ([[5,1,3]]) perfect quantum code defines a six-qubit perfect tensor: every subset of at most three tensor legs is maximally mixed, so its entropy equals the corresponding unweighted min-cut count in bits. The boundary encoding should satisfy the erasure Knill–Laflamme condition for every known erasure of at most two of the five boundary qubits. A generic perturbation can preserve (V^\dagger V=I) while breaking both special properties.

The five-qubit code is sourced to [Laflamme et al. (1996), arXiv:quant-ph/9602019](https://arxiv.org/abs/quant-ph/9602019). Its holographic perfect-tensor use is sourced to [Pastawski et al. (2015), arXiv:1503.06237](https://arxiv.org/abs/1503.06237).

## Variables, assumptions, and command

- Exact state-vector dimension: (2^6=64) for the purified tensor; encoding isometry (V:\mathbb C^2\to(\mathbb C^2)^{\otimes5}).
- Stabilizers: `XZZXI`, `IXZZX`, `XIXZZ`, `ZXIXZ`; logical (Z=ZZZZZ), logical (X=XXXXX).
- Entropy unit: bit; perturbation (epsilon) in radians; all residuals dimensionless.
- Perturbation: (|0_L\rangle\mapsto\cos\epsilon|0_L\rangle+\sin\epsilon|w\rangle), where (|w\rangle) is deterministically chosen orthogonal to both logical codewords. (|1_L\rangle) is unchanged, so the map remains an isometry.
- Sweep: (epsilon=0,0.01,0.03,0.10,0.20,0.35).
- Static, noiseless finite-dimensional quantum mechanics; no metric, Hamiltonian time evolution, or matter stress tensor.

```bash
MPLCONFIGDIR=python-code/.mplconfig python-code/.venv/bin/python python-code/toy_models/t2_perfect_tensor.py
```

## Results

| ε (rad) | Isometry residual | Max erasure residual | Max min-cut entropy deviation (bits) |
|---:|---:|---:|---:|
| 0.00 | 0 | 0 | 8.88e-16 |
| 0.01 | 4.44e-16 | 0.005830 | 0.0000870 |
| 0.03 | 1.11e-16 | 0.017828 | 0.0007910 |
| 0.10 | 1.11e-16 | 0.063265 | 0.009081 |
| 0.20 | 0 | 0.136732 | 0.037794 |
| 0.35 | 1.11e-16 | 0.261750 | 0.120794 |

At baseline, every entropy/min-cut check and every one- or two-qubit erasure condition passes at (10^{-12}) tolerance. Isometry residual remains below (5\times10^{-16}) across the sweep, while erasure and min-cut properties degrade immediately. Therefore perfect-tensor geometry is special structure, not a generic consequence of an isometric quantum encoding.

## Required checks

- **Dimensional analysis:** all Hilbert-space quantities are dimensionless; entropy is explicitly in bits.
- **Covariance:** no spacetime covariance is present. It is replaced only by exact stabilizer/code symmetries. This is a failure against the full gravity checklist, not something to conceal.
- **Conservation and causality:** not applicable to this static model; no Hamiltonian or causal propagation exists.
- **Stability:** the sensitivity sweep shows that error-correction and min-cut equalities are not stable under the chosen generic isometric perturbation.
- **Unitarity:** the finite encoding is an isometry to machine precision for every (epsilon). This demonstrates that unitarity/isometry alone is insufficient for the geometric interpretation.
- **Newtonian/weak-field GR and semiclassical behavior:** absent.
- **Horizon thermodynamics:** the entropy computed is subsystem von Neumann entropy, not Bekenstein–Hawking entropy. No (S=A/4) claim is made.
- **Wolfram/Python cross-check:** Wolfram exact arithmetic confirms mutually commuting involutory stabilizers, a rank-2 code projector, and a rank-1 logical-zero projector. Python independently checks all reduced states and perturbations.

## Failure conditions and conclusion

The exact baseline would fail if any up-to-three-leg entropy differed from its min-cut value or any up-to-two-qubit erasure leaked logical information. It passes. The robustness hypothesis—that these properties follow merely from isometry—fails. Any hybrid using tensor-network geometry must add and justify dynamics that protects or selects the perfect/code structure; otherwise its geometric dictionary is fine-tuned.

Canonical outputs: `results/t2_perfect_tensor/`.
