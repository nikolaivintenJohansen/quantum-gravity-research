import numpy as np

from toy_models.t2_perfect_tensor import (
    entropy_table,
    erasure_kl_residual,
    five_qubit_codewords,
    isometry_residual,
    perfect_tensor_state,
    perturbed_codewords,
    stabilizer_residual,
)


def test_five_qubit_code_is_stabilized_isometry() -> None:
    codewords = five_qubit_codewords()
    assert isometry_residual(codewords) < 1e-12
    assert stabilizer_residual(codewords) < 1e-12


def test_purification_is_six_qubit_perfect_tensor() -> None:
    state = perfect_tensor_state(five_qubit_codewords())
    table = entropy_table(state)
    assert table["absolute_deviation"].max() < 1e-12


def test_two_known_erasure_qubits_are_correctable() -> None:
    assert erasure_kl_residual(five_qubit_codewords(), max_erased=2) < 1e-12


def test_generic_isometric_perturbation_breaks_special_properties() -> None:
    baseline = five_qubit_codewords()
    perturbed = perturbed_codewords(baseline, epsilon=0.2)
    assert isometry_residual(perturbed) < 1e-12
    assert erasure_kl_residual(perturbed, max_erased=2) > 1e-3
    entropy_deviation = entropy_table(perfect_tensor_state(perturbed))["absolute_deviation"].max()
    assert entropy_deviation > 1e-3
