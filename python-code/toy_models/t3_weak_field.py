"""T3: symbolic weak-field GR/EFT matching benchmark."""

from __future__ import annotations

import argparse
import json
import os
import platform
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", str(Path(__file__).resolve().parents[1] / ".mplconfig"))

import matplotlib.pyplot as plt
import pandas as pd
import sympy as sp


Dimension = tuple[int, int, int]  # exponents of (mass, length, time)


def add_dimensions(left: Dimension, right: Dimension) -> Dimension:
    return tuple(a + b for a, b in zip(left, right))  # type: ignore[return-value]


def scale_dimension(value: Dimension, power: int) -> Dimension:
    return tuple(power * component for component in value)  # type: ignore[return-value]


def dimension_checks() -> dict[str, object]:
    mass: Dimension = (1, 0, 0)
    length: Dimension = (0, 1, 0)
    time: Dimension = (0, 0, 1)
    gravitational_constant = add_dimensions(
        add_dimensions(scale_dimension(length, 3), scale_dimension(mass, -1)),
        scale_dimension(time, -2),
    )
    density = add_dimensions(mass, scale_dimension(length, -3))
    speed = add_dimensions(length, scale_dimension(time, -1))
    potential = scale_dimension(speed, 2)
    laplacian_potential = add_dimensions(potential, scale_dimension(length, -2))
    poisson_source = add_dimensions(gravitational_constant, density)
    stress_energy_00 = add_dimensions(density, scale_dimension(speed, 2))
    einstein_rhs = add_dimensions(
        add_dimensions(gravitational_constant, stress_energy_00), scale_dimension(speed, -4)
    )
    return {
        "basis": "(mass, length, time) exponents",
        "G": gravitational_constant,
        "rho": density,
        "Phi": potential,
        "laplacian_Phi": laplacian_potential,
        "G_times_rho": poisson_source,
        "T00": stress_energy_00,
        "G_T00_over_c4": einstein_rhs,
        "poisson_dimensions_match": laplacian_potential == poisson_source,
        "einstein_rhs_is_inverse_length_squared": einstein_rhs == (0, -2, 0),
    }


def newtonian_limit() -> dict[str, sp.Expr]:
    gravitational_constant, density, speed, laplacian = sp.symbols(
        "G rho c laplacian_Phi", positive=True
    )
    einstein_00 = sp.Eq(2 * laplacian / speed**2, 8 * sp.pi * gravitational_constant * density / speed**2)
    solution = sp.solve(einstein_00, laplacian)[0]

    radius, mass = sp.symbols("r M", positive=True)
    potential = -gravitational_constant * mass / radius
    radial_derivative = sp.diff(potential, radius)
    flux = sp.simplify(4 * sp.pi * radius**2 * radial_derivative)
    acceleration = sp.simplify(-radial_derivative)
    return {
        "poisson_solution": solution,
        "point_mass_potential": potential,
        "radial_acceleration": acceleration,
        "gauss_flux": flux,
    }


def linearized_einstein_bianchi_residuals() -> list[sp.Expr]:
    """Return k^mu G^L_{mu nu} for a generic Fourier-mode metric perturbation."""
    eta = sp.diag(-1, 1, 1, 1)
    k_covariant = sp.Matrix(sp.symbols("k0:4"))
    k_contravariant = eta * k_covariant

    symbols: dict[tuple[int, int], sp.Symbol] = {}
    for row in range(4):
        for column in range(row, 4):
            symbols[(row, column)] = sp.symbols(f"h{row}{column}")
    h_covariant = sp.Matrix(
        4,
        4,
        lambda row, column: symbols[(min(row, column), max(row, column))],
    )
    h_mixed = eta * h_covariant
    h_contravariant = eta * h_covariant * eta
    trace_h = sp.trace(eta * h_covariant)
    k_squared = (k_covariant.T * eta * k_covariant)[0]
    kk_h = (k_covariant.T * h_contravariant * k_covariant)[0]

    einstein = sp.MutableDenseMatrix.zeros(4, 4)
    for mu in range(4):
        for nu in range(4):
            first = -sum(
                k_covariant[sigma] * k_covariant[nu] * h_mixed[sigma, mu]
                for sigma in range(4)
            )
            second = -sum(
                k_covariant[sigma] * k_covariant[mu] * h_mixed[sigma, nu]
                for sigma in range(4)
            )
            einstein[mu, nu] = sp.Rational(1, 2) * (
                first
                + second
                + k_squared * h_covariant[mu, nu]
                + k_covariant[mu] * k_covariant[nu] * trace_h
                - eta[mu, nu] * (-kk_h + k_squared * trace_h)
            )

    return [
        sp.simplify(sum(k_contravariant[mu] * einstein[mu, nu] for mu in range(4)))
        for nu in range(4)
    ]


def validity_sweep(radius_over_schwarzschild: list[float]) -> pd.DataFrame:
    rows = []
    for ratio in radius_over_schwarzschild:
        if ratio <= 1:
            raise ValueError("weak-field sweep requires r/r_s > 1")
        epsilon = 1.0 / ratio
        rows.append(
            {
                "radius_over_schwarzschild_radius": ratio,
                "weak_field_parameter_abs_2Phi_over_c2": epsilon,
                "nominal_second_order_scale": epsilon**2,
            }
        )
    return pd.DataFrame(rows)


def plot_validity(sweep: pd.DataFrame, output: Path) -> None:
    fig, axis = plt.subplots(figsize=(7, 4.5))
    axis.loglog(
        sweep["radius_over_schwarzschild_radius"],
        sweep["weak_field_parameter_abs_2Phi_over_c2"],
        marker="o",
        label=r"$|2\Phi/c^2|=r_s/r$",
    )
    axis.loglog(
        sweep["radius_over_schwarzschild_radius"],
        sweep["nominal_second_order_scale"],
        marker="s",
        label="Nominal second-order scale",
    )
    axis.set_xlabel(r"Radius $r/r_s$")
    axis.set_ylabel("Dimensionless expansion scale")
    axis.set_title("T3: explicit domain of the weak-field expansion")
    axis.grid(which="both", alpha=0.25)
    axis.legend()
    fig.tight_layout()
    fig.savefig(output, dpi=180, bbox_inches="tight")
    plt.close(fig)


def run(ratios: list[float]) -> tuple[dict[str, object], pd.DataFrame]:
    dimensions = dimension_checks()
    newton = newtonian_limit()
    bianchi = linearized_einstein_bianchi_residuals()
    sweep = validity_sweep(ratios)
    gravitational_constant, density = sp.symbols("G rho", positive=True)
    checks = {
        "poisson_dimensions_match": dimensions["poisson_dimensions_match"],
        "einstein_equation_dimensions_match": dimensions[
            "einstein_rhs_is_inverse_length_squared"
        ],
        "poisson_coefficient_exact": sp.simplify(
            newton["poisson_solution"] - 4 * sp.pi * gravitational_constant * density
        )
        == 0,
        "point_mass_flux_exact": sp.simplify(
            newton["gauss_flux"]
            - 4 * sp.pi * sp.symbols("G", positive=True) * sp.symbols("M", positive=True)
        )
        == 0,
        "linearized_bianchi_identity": all(value == 0 for value in bianchi),
        "weak_field_parameter_monotone": bool(
            sweep["weak_field_parameter_abs_2Phi_over_c2"].is_monotonic_decreasing
        ),
        "second_order_below_first_order": bool(
            (
                sweep["nominal_second_order_scale"]
                < sweep["weak_field_parameter_abs_2Phi_over_c2"]
            ).all()
        ),
    }
    if not all(checks.values()):
        raise AssertionError(f"T3 validation failure: {checks}")
    report = {
        "dimensions": dimensions,
        "symbolic_results": {key: str(value) for key, value in newton.items()},
        "bianchi_residuals": [str(value) for value in bianchi],
        "checks": checks,
    }
    return report, sweep


def main() -> None:
    root = Path(__file__).resolve().parents[2]
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--radius-ratios",
        nargs="+",
        type=float,
        default=[10, 30, 100, 300, 1_000, 10_000, 1_000_000, 100_000_000],
    )
    parser.add_argument("--output-dir", type=Path, default=root / "results/t3_weak_field")
    args = parser.parse_args()

    report, sweep = run(args.radius_ratios)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    sweep.to_csv(args.output_dir / "validity_sweep.csv", index=False, float_format="%.12g")
    plot_validity(sweep, args.output_dir / "weak_field_domain.png")
    metadata = {
        "model_id": "T3",
        "claim": "Linearized Einstein gravity recovers Poisson gravity and obeys the linearized Bianchi identity within an explicit weak-field domain",
        "parameters": {"radius_over_schwarzschild_radius": args.radius_ratios},
        "units": "symbolic SI dimensions; sweep variables are dimensionless ratios",
        "assumptions": [
            "metric signature (-,+,+,+)",
            "g_00 = -(1 + 2 Phi/c^2)",
            "nonrelativistic matter T_00 approximately rho c^2",
            "static weak field and r much greater than Schwarzschild radius",
            "linearized Fourier-mode perturbation for the Bianchi check",
        ],
        **report,
        "versions": {
            "python": platform.python_version(),
            "sympy": sp.__version__,
            "pandas": pd.__version__,
            "matplotlib": __import__("matplotlib").__version__,
        },
        "randomness_used": False,
        "command": (
            "MPLCONFIGDIR=python-code/.mplconfig python-code/.venv/bin/python "
            "python-code/toy_models/t3_weak_field.py"
        ),
    }
    (args.output_dir / "metadata.json").write_text(
        json.dumps(metadata, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(report, indent=2, sort_keys=True))
    print(sweep.to_string(index=False))


if __name__ == "__main__":
    main()
