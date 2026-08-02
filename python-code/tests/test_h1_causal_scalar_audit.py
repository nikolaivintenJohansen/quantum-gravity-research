import numpy as np

from toy_models.h1_causal_scalar_audit import (
    action_kernel,
    audit_size,
    causal_dalembertian_2d,
    chain_relation,
)


def test_three_chain_retarded_operator_is_exact() -> None:
    operator = causal_dalembertian_2d(chain_relation(3), density=1.0)
    expected = np.array([[-2, 0, 0], [4, -2, 0], [-8, 4, -2]], dtype=float)
    assert np.array_equal(operator, expected)


def test_real_quadratic_action_symmetrizes_kernel() -> None:
    operator = causal_dalembertian_2d(chain_relation(4), density=1.0)
    kernel = action_kernel(operator)
    assert np.array_equal(kernel, kernel.T)
    assert not np.array_equal(kernel, operator)
    assert np.linalg.norm(np.triu(kernel, k=1)) > 0


def test_operator_is_relabeling_covariant() -> None:
    audit = audit_size(6, density=2.5)
    assert audit["relabeling_covariance_residual"] < 1e-12
    assert audit["strictly_retarded_operator"]
