import sympy as sp

from toy_models.t3_weak_field import (
    dimension_checks,
    linearized_einstein_bianchi_residuals,
    newtonian_limit,
    validity_sweep,
)


def test_poisson_and_einstein_dimensions_match() -> None:
    checks = dimension_checks()
    assert checks["poisson_dimensions_match"]
    assert checks["einstein_rhs_is_inverse_length_squared"]


def test_newtonian_limit_and_gauss_flux_are_exact() -> None:
    results = newtonian_limit()
    gravitational_constant, density, mass = sp.symbols("G rho M", positive=True)
    assert sp.simplify(results["poisson_solution"] - 4 * sp.pi * gravitational_constant * density) == 0
    assert sp.simplify(results["gauss_flux"] - 4 * sp.pi * gravitational_constant * mass) == 0


def test_linearized_bianchi_identity_for_generic_mode() -> None:
    assert linearized_einstein_bianchi_residuals() == [0, 0, 0, 0]


def test_validity_parameter_decreases_and_second_order_is_smaller() -> None:
    sweep = validity_sweep([10, 100, 1_000])
    assert sweep["weak_field_parameter_abs_2Phi_over_c2"].is_monotonic_decreasing
    assert (
        sweep["nominal_second_order_scale"]
        < sweep["weak_field_parameter_abs_2Phi_over_c2"]
    ).all()
