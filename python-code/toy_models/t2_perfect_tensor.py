"""T2: exact five-qubit-code perfect tensor and controlled perturbation."""

from __future__ import annotations

import argparse
import itertools
import json
import os
import platform
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", str(Path(__file__).resolve().parents[1] / ".mplconfig"))

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Z = np.array([[1, 0], [0, -1]], dtype=complex)
PAULI = {"I": I2, "X": X, "Z": Z}
STABILIZERS = ("XZZXI", "IXZZX", "XIXZZ", "ZXIXZ")


def pauli_string(specification: str) -> np.ndarray:
    result = np.array([[1.0 + 0.0j]])
    for symbol in specification:
        result = np.kron(result, PAULI[symbol])
    return result


def five_qubit_codewords() -> tuple[np.ndarray, np.ndarray]:
    """Construct logical codewords from the stabilizer and logical-Z projectors."""
    dimension = 2**5
    projector = np.eye(dimension, dtype=complex)
    for specification in STABILIZERS:
        generator = pauli_string(specification)
        projector = projector @ ((np.eye(dimension) + generator) / 2)
    logical_z = pauli_string("ZZZZZ")
    projector = projector @ ((np.eye(dimension) + logical_z) / 2)

    logical_zero = None
    for index in range(dimension):
        basis = np.zeros(dimension, dtype=complex)
        basis[index] = 1
        candidate = projector @ basis
        norm = np.linalg.norm(candidate)
        if norm > 1e-12:
            logical_zero = candidate / norm
            break
    if logical_zero is None:
        raise RuntimeError("Failed to construct five-qubit logical zero")
    logical_one = pauli_string("XXXXX") @ logical_zero
    logical_one /= np.linalg.norm(logical_one)
    return logical_zero, logical_one


def state_matrix(state: np.ndarray, keep: tuple[int, ...], qubits: int) -> np.ndarray:
    remainder = tuple(index for index in range(qubits) if index not in keep)
    tensor = state.reshape((2,) * qubits)
    return np.transpose(tensor, keep + remainder).reshape(2 ** len(keep), -1)


def reduced_cross(
    left: np.ndarray, right: np.ndarray, keep: tuple[int, ...], qubits: int
) -> np.ndarray:
    left_matrix = state_matrix(left, keep, qubits)
    right_matrix = state_matrix(right, keep, qubits)
    return left_matrix @ right_matrix.conj().T


def entropy_bits(state: np.ndarray, keep: tuple[int, ...], qubits: int) -> float:
    rho = reduced_cross(state, state, keep, qubits)
    eigenvalues = np.linalg.eigvalsh(rho).real
    eigenvalues = eigenvalues[eigenvalues > 1e-14]
    return float(-(eigenvalues * np.log2(eigenvalues)).sum())


def perfect_tensor_state(codewords: tuple[np.ndarray, np.ndarray]) -> np.ndarray:
    zero, one = codewords
    return np.concatenate([zero, one]) / np.sqrt(2)


def isometry_residual(codewords: tuple[np.ndarray, np.ndarray]) -> float:
    isometry = np.column_stack(codewords)
    return float(np.linalg.norm(isometry.conj().T @ isometry - np.eye(2), ord="fro"))


def stabilizer_residual(codewords: tuple[np.ndarray, np.ndarray]) -> float:
    residuals = []
    for specification in STABILIZERS:
        generator = pauli_string(specification)
        for state in codewords:
            residuals.append(np.linalg.norm(generator @ state - state))
    return float(max(residuals))


def erasure_kl_residual(codewords: tuple[np.ndarray, np.ndarray], max_erased: int = 2) -> float:
    zero, one = codewords
    residuals = []
    for size in range(1, max_erased + 1):
        for erased in itertools.combinations(range(5), size):
            rho_zero = reduced_cross(zero, zero, erased, 5)
            rho_one = reduced_cross(one, one, erased, 5)
            cross = reduced_cross(zero, one, erased, 5)
            residuals.extend(
                [
                    np.linalg.norm(rho_zero - rho_one, ord="fro"),
                    np.linalg.norm(cross, ord="fro"),
                ]
            )
    return float(max(residuals))


def entropy_table(state: np.ndarray) -> pd.DataFrame:
    rows = []
    for size in range(1, 4):
        expected = float(size)
        for subset in itertools.combinations(range(6), size):
            entropy = entropy_bits(state, subset, 6)
            rows.append(
                {
                    "subset": "".join(str(index) for index in subset),
                    "subset_size": size,
                    "entropy_bits": entropy,
                    "min_cut_bits": expected,
                    "absolute_deviation": abs(entropy - expected),
                }
            )
    return pd.DataFrame(rows)


def orthogonal_perturbation(codewords: tuple[np.ndarray, np.ndarray]) -> np.ndarray:
    zero, one = codewords
    for index in range(zero.size):
        vector = np.zeros_like(zero)
        vector[index] = 1
        vector = vector - np.vdot(zero, vector) * zero - np.vdot(one, vector) * one
        norm = np.linalg.norm(vector)
        if norm > 1e-10:
            return vector / norm
    raise RuntimeError("Failed to find deterministic orthogonal perturbation")


def perturbed_codewords(
    codewords: tuple[np.ndarray, np.ndarray], epsilon: float
) -> tuple[np.ndarray, np.ndarray]:
    zero, one = codewords
    direction = orthogonal_perturbation(codewords)
    perturbed_zero = np.cos(epsilon) * zero + np.sin(epsilon) * direction
    return perturbed_zero, one.copy()


def sweep(codewords: tuple[np.ndarray, np.ndarray], epsilons: list[float]) -> pd.DataFrame:
    rows = []
    for epsilon in epsilons:
        perturbed = perturbed_codewords(codewords, epsilon)
        entropies = entropy_table(perfect_tensor_state(perturbed))
        rows.append(
            {
                "epsilon_radians": epsilon,
                "isometry_residual": isometry_residual(perturbed),
                "max_erasure_kl_residual": erasure_kl_residual(perturbed),
                "max_mincut_entropy_deviation_bits": entropies["absolute_deviation"].max(),
            }
        )
    return pd.DataFrame(rows)


def plot_sweep(sweep_data: pd.DataFrame, output: Path) -> None:
    fig, axis = plt.subplots(figsize=(7, 4.5))
    axis.plot(
        sweep_data["epsilon_radians"],
        sweep_data["max_erasure_kl_residual"],
        marker="o",
        label="Erasure Knill–Laflamme residual",
    )
    axis.plot(
        sweep_data["epsilon_radians"],
        sweep_data["max_mincut_entropy_deviation_bits"],
        marker="s",
        label="Max min-cut entropy deviation (bits)",
    )
    axis.set_yscale("symlog", linthresh=1e-14)
    axis.set_xlabel("Isometry-preserving perturbation ε (radians)")
    axis.set_ylabel("Residual / deviation")
    axis.set_title("T2: perfect-code properties are not generic isometry properties")
    axis.grid(alpha=0.25)
    axis.legend()
    fig.tight_layout()
    fig.savefig(output, dpi=180, bbox_inches="tight")
    plt.close(fig)


def run(epsilons: list[float]) -> tuple[pd.DataFrame, pd.DataFrame, dict[str, object]]:
    codewords = five_qubit_codewords()
    state = perfect_tensor_state(codewords)
    baseline = entropy_table(state)
    sweep_data = sweep(codewords, epsilons)
    checks = {
        "baseline_isometry_residual_below_1e_12": isometry_residual(codewords) < 1e-12,
        "baseline_stabilizer_residual_below_1e_12": stabilizer_residual(codewords) < 1e-12,
        "baseline_erasure_kl_residual_below_1e_12": erasure_kl_residual(codewords) < 1e-12,
        "baseline_perfect_tensor_entropy_residual_below_1e_12": (
            float(baseline["absolute_deviation"].max()) < 1e-12
        ),
        "perturbed_isometries_preserved_below_1e_12": bool(
            (sweep_data["isometry_residual"] < 1e-12).all()
        ),
        "perturbation_breaks_erasure_correction": bool(
            sweep_data.iloc[-1]["max_erasure_kl_residual"] > 1e-3
        ),
        "perturbation_breaks_unweighted_mincut_entropy": bool(
            sweep_data.iloc[-1]["max_mincut_entropy_deviation_bits"] > 1e-3
        ),
    }
    if not all(checks.values()):
        raise AssertionError(f"T2 validation failure: {checks}")
    return baseline, sweep_data, checks


def main() -> None:
    root = Path(__file__).resolve().parents[2]
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--epsilons", nargs="+", type=float, default=[0.0, 0.01, 0.03, 0.1, 0.2, 0.35]
    )
    parser.add_argument("--output-dir", type=Path, default=root / "results/t2_perfect_tensor")
    args = parser.parse_args()

    baseline, sweep_data, checks = run(args.epsilons)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    baseline.to_csv(args.output_dir / "baseline_entropies.csv", index=False, float_format="%.12g")
    sweep_data.to_csv(args.output_dir / "perturbation_sweep.csv", index=False, float_format="%.12g")
    plot_sweep(sweep_data, args.output_dir / "perturbation_sensitivity.png")
    metadata = {
        "model_id": "T2",
        "claim": "The five-qubit-code purification is a six-qubit perfect tensor, and generic isometric perturbations break its code/min-cut properties",
        "parameters": {"epsilons_radians": args.epsilons},
        "units": "entropies in bits; perturbation angle in radians; all other quantities dimensionless",
        "assumptions": [
            "exact finite-dimensional qubits",
            "pure states and noiseless linear algebra",
            "five-qubit stabilizer code",
            "static kinematics only; no spacetime dynamics",
        ],
        "checks": checks,
        "versions": {
            "python": platform.python_version(),
            "numpy": np.__version__,
            "pandas": pd.__version__,
            "matplotlib": __import__("matplotlib").__version__,
        },
        "randomness_used": False,
        "command": (
            "MPLCONFIGDIR=python-code/.mplconfig python-code/.venv/bin/python "
            "python-code/toy_models/t2_perfect_tensor.py"
        ),
    }
    (args.output_dir / "metadata.json").write_text(
        json.dumps(metadata, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(sweep_data.to_string(index=False))
    print(json.dumps(checks, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
