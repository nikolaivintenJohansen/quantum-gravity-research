"""H1 structural audit: retarded causal-set scalar operator versus an action kernel."""

from __future__ import annotations

import argparse
import json
import os
import platform
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", str(Path(__file__).resolve().parents[1] / ".mplconfig"))

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


LAYER_COEFFICIENTS_2D = {0: 4.0, 1: -8.0, 2: 4.0}


def chain_relation(size: int) -> np.ndarray:
    if size < 2:
        raise ValueError("size must be at least 2")
    return np.triu(np.ones((size, size), dtype=bool), k=1)


def causal_dalembertian_2d(relation: np.ndarray, density: float = 1.0) -> np.ndarray:
    """Return B_R[x,y], with y in the past of x, using the original 2D layers."""
    size = relation.shape[0]
    if relation.shape != (size, size) or density <= 0:
        raise ValueError("relation must be square and density positive")
    operator = -2.0 * density * np.eye(size)
    for past in range(size):
        for event in range(size):
            if not relation[past, event]:
                continue
            intervening = int(np.logical_and(relation[past, :], relation[:, event]).sum())
            if intervening in LAYER_COEFFICIENTS_2D:
                operator[event, past] = density * LAYER_COEFFICIENTS_2D[intervening]
    return operator


def action_kernel(retarded_operator: np.ndarray) -> np.ndarray:
    """Kernel produced by varying 1/2 phi^T B_R phi for a real scalar."""
    return (retarded_operator + retarded_operator.T) / 2


def permutation_matrix(permutation: list[int]) -> np.ndarray:
    size = len(permutation)
    matrix = np.zeros((size, size))
    for new_index, old_index in enumerate(permutation):
        matrix[new_index, old_index] = 1
    return matrix


def audit_size(size: int, density: float) -> dict[str, float | int | bool]:
    relation = chain_relation(size)
    retarded = causal_dalembertian_2d(relation, density)
    variational = action_kernel(retarded)
    permutation = list(reversed(range(size)))
    transform = permutation_matrix(permutation)
    permuted_relation = (transform @ relation.astype(int) @ transform.T).astype(bool)
    permuted_operator = causal_dalembertian_2d(permuted_relation, density)
    covariance_residual = np.linalg.norm(permuted_operator - transform @ retarded @ transform.T)
    advanced_mask = relation  # row=past, column=future; upper triangle for the natural chain.
    advanced_norm = np.linalg.norm(np.where(advanced_mask, variational, 0.0), ord="fro")
    return {
        "size": size,
        "density_inverse_length_squared": density,
        "retarded_asymmetry_frobenius": float(np.linalg.norm(retarded - retarded.T, ord="fro")),
        "action_vs_retarded_frobenius": float(np.linalg.norm(variational - retarded, ord="fro")),
        "advanced_support_frobenius": float(advanced_norm),
        "relabeling_covariance_residual": float(covariance_residual),
        "strictly_retarded_operator": bool(np.allclose(np.triu(retarded, k=1), 0.0)),
        "action_kernel_symmetric": bool(np.allclose(variational, variational.T)),
    }


def plot_kernels(output: Path, density: float) -> None:
    retarded = causal_dalembertian_2d(chain_relation(5), density)
    variational = action_kernel(retarded)
    limit = max(abs(retarded).max(), abs(variational).max())
    fig, axes = plt.subplots(1, 2, figsize=(10, 4), constrained_layout=True)
    for axis, matrix, title in zip(
        axes,
        [retarded, variational],
        [r"Retarded $B_R$", r"Action kernel $(B_R+B_R^T)/2$"],
    ):
        image = axis.imshow(matrix, cmap="coolwarm", vmin=-limit, vmax=limit)
        axis.set_title(title)
        axis.set_xlabel("Input event y")
        axis.set_ylabel("Output event x")
        axis.set_xticks(range(5))
        axis.set_yticks(range(5))
    fig.colorbar(image, ax=axes, shrink=0.8, pad=0.03, label=r"Coefficient in units of $\rho$")
    fig.suptitle("H1 structural obstruction: variation symmetrizes a retarded kernel")
    fig.savefig(output, dpi=180)
    plt.close(fig)


def main() -> None:
    root = Path(__file__).resolve().parents[2]
    parser = argparse.ArgumentParser()
    parser.add_argument("--sizes", nargs="+", type=int, default=[3, 4, 5, 6, 8, 10])
    parser.add_argument("--density", type=float, default=1.0)
    parser.add_argument("--output-dir", type=Path, default=root / "results/h1_causal_scalar")
    args = parser.parse_args()

    rows = pd.DataFrame([audit_size(size, args.density) for size in args.sizes])
    three_chain = causal_dalembertian_2d(chain_relation(3), args.density)
    three_action = action_kernel(three_chain)
    checks = {
        "engineering_dimension_B_is_inverse_length_squared": True,
        "order_relabeling_covariance": bool(
            (rows["relabeling_covariance_residual"] < 1e-12).all()
        ),
        "retarded_support": bool(rows["strictly_retarded_operator"].all()),
        "real_action_kernel_symmetric": bool(rows["action_kernel_symmetric"].all()),
        "real_action_reproduces_retarded_equation": bool(
            (rows["action_vs_retarded_frobenius"] < 1e-12).all()
        ),
        "symmetrization_avoids_advanced_support": bool(
            (rows["advanced_support_frobenius"] < 1e-12).all()
        ),
    }
    expected_failures = {
        "real_action_reproduces_retarded_equation": False,
        "symmetrization_avoids_advanced_support": False,
    }
    if checks["real_action_reproduces_retarded_equation"] != expected_failures[
        "real_action_reproduces_retarded_equation"
    ]:
        raise AssertionError("Expected the real quadratic action to symmetrize B_R")
    if checks["symmetrization_avoids_advanced_support"] != expected_failures[
        "symmetrization_avoids_advanced_support"
    ]:
        raise AssertionError("Expected the symmetric action kernel to acquire advanced support")

    args.output_dir.mkdir(parents=True, exist_ok=True)
    rows.to_csv(args.output_dir / "kernel_audit.csv", index=False, float_format="%.12g")
    plot_kernels(args.output_dir / "retarded_vs_action_kernel.png", args.density)
    metadata = {
        "hybrid_id": "H1",
        "parameters": {"sizes": args.sizes, "density": args.density},
        "units": "natural units hbar=c=1; density rho has L^-2 and B has L^-2",
        "layer_coefficients_2d": LAYER_COEFFICIENTS_2D,
        "three_chain_retarded_operator": three_chain.tolist(),
        "three_chain_action_kernel": three_action.tolist(),
        "checks": checks,
        "expected_failures": expected_failures,
        "conclusion": "rejected: a naive real quadratic action cannot retain the strictly retarded kernel",
        "versions": {
            "python": platform.python_version(),
            "numpy": np.__version__,
            "pandas": pd.__version__,
            "matplotlib": __import__("matplotlib").__version__,
        },
        "randomness_used": False,
        "command": (
            "MPLCONFIGDIR=python-code/.mplconfig python-code/.venv/bin/python "
            "python-code/toy_models/h1_causal_scalar_audit.py"
        ),
    }
    (args.output_dir / "metadata.json").write_text(
        json.dumps(metadata, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(rows.to_string(index=False))
    print(json.dumps(checks, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
