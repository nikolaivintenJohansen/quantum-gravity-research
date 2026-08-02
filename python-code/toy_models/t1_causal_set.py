"""T1: conditioned Poisson sprinklings in a 1+1D causal diamond."""

from __future__ import annotations

import argparse
import bisect
import json
import os
import platform
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", str(Path(__file__).resolve().parents[1] / ".mplconfig"))

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy
from scipy.optimize import brentq
from scipy.special import gamma


def expected_ordering_fraction(dimension: float) -> float:
    """Myrheim–Meyer ordering fraction for a Minkowski Alexandrov interval."""
    d = float(dimension)
    if d <= 0:
        raise ValueError("dimension must be positive")
    return float(gamma(d + 1) * gamma(d / 2) / (2 * gamma(3 * d / 2)))


def infer_dimension(ordering_fraction: float) -> float:
    """Invert the Myrheim–Meyer expectation on 1 <= d <= 20."""
    r = float(ordering_fraction)
    lower = expected_ordering_fraction(20.0)
    if not lower < r <= 1.0:
        raise ValueError(f"ordering fraction {r} outside inversion range ({lower}, 1]")
    if np.isclose(r, 1.0):
        return 1.0
    return float(brentq(lambda d: expected_ordering_fraction(d) - r, 1.0, 20.0))


def sprinkle_conditioned(count: int, rng: np.random.Generator, half_extent: float = 1.0) -> np.ndarray:
    """Uniformly sprinkle count points conditional on N in null coordinates (u, v)."""
    if count < 2 or half_extent <= 0:
        raise ValueError("count must be >= 2 and half_extent must be positive")
    return rng.uniform(-half_extent, half_extent, size=(count, 2))


def causal_matrix(points_uv: np.ndarray) -> np.ndarray:
    """Return C[i,j] = True exactly when point i causally precedes point j."""
    u = points_uv[:, 0]
    v = points_uv[:, 1]
    return (u[:, None] < u[None, :]) & (v[:, None] < v[None, :])


def ordering_fraction(relation: np.ndarray) -> float:
    n = relation.shape[0]
    if relation.shape != (n, n) or n < 2:
        raise ValueError("relation must be a square matrix with n >= 2")
    return float(2 * relation.sum() / (n * (n - 1)))


def longest_chain_length(points_uv: np.ndarray) -> int:
    """Longest strict chain via a longest-increasing-subsequence calculation."""
    order = np.argsort(points_uv[:, 0], kind="stable")
    tails: list[float] = []
    for value in points_uv[order, 1]:
        position = bisect.bisect_left(tails, float(value))
        if position == len(tails):
            tails.append(float(value))
        else:
            tails[position] = float(value)
    return len(tails)


def lorentz_boost_null(points_uv: np.ndarray, rapidity: float) -> np.ndarray:
    """Apply u -> exp(eta)u, v -> exp(-eta)v."""
    factors = np.array([np.exp(rapidity), np.exp(-rapidity)])
    return points_uv * factors


def run_sweep(sizes: list[int], repeats: int, seed: int, half_extent: float) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    rows: list[dict[str, float | int]] = []
    for count in sizes:
        for replicate in range(repeats):
            points = sprinkle_conditioned(count, rng, half_extent)
            relation = causal_matrix(points)
            fraction = ordering_fraction(relation)
            rows.append(
                {
                    "count": count,
                    "replicate": replicate,
                    "ordering_fraction": fraction,
                    "dimension_estimate": infer_dimension(fraction),
                    "longest_chain": longest_chain_length(points),
                }
            )
    return pd.DataFrame(rows)


def summarize(samples: pd.DataFrame) -> pd.DataFrame:
    grouped = samples.groupby("count", sort=True)
    summary = grouped.agg(
        repeats=("replicate", "count"),
        mean_ordering_fraction=("ordering_fraction", "mean"),
        sd_ordering_fraction=("ordering_fraction", "std"),
        mean_dimension=("dimension_estimate", "mean"),
        sd_dimension=("dimension_estimate", "std"),
        mean_longest_chain=("longest_chain", "mean"),
        sd_longest_chain=("longest_chain", "std"),
    ).reset_index()
    summary["se_ordering_fraction"] = summary["sd_ordering_fraction"] / np.sqrt(summary["repeats"])
    summary["se_dimension"] = summary["sd_dimension"] / np.sqrt(summary["repeats"])
    summary["normalized_longest_chain"] = summary["mean_longest_chain"] / (
        2 * np.sqrt(summary["count"])
    )
    return summary


def validate(samples: pd.DataFrame, summary: pd.DataFrame, seed: int) -> dict[str, object]:
    check_rng = np.random.default_rng(seed + 1)
    points = sprinkle_conditioned(128, check_rng)
    relation = causal_matrix(points)
    two_step = (relation.astype(np.uint8) @ relation.astype(np.uint8)) > 0
    boosted = causal_matrix(lorentz_boost_null(points, rapidity=1.7))
    large = summary[summary["count"] >= 128]
    checks = {
        "irreflexive": bool(not relation.diagonal().any()),
        "transitive": bool(np.all(~two_step | relation)),
        "boost_invariant_relation": bool(np.array_equal(relation, boosted)),
        "mean_ordering_within_0_02": bool(
            (summary["mean_ordering_fraction"].sub(0.5).abs() < 0.02).all()
        ),
        "large_n_mean_dimension_within_0_2": bool(
            (large["mean_dimension"].sub(2.0).abs() < 0.2).all()
        ),
        "all_dimensions_finite": bool(np.isfinite(samples["dimension_estimate"]).all()),
    }
    if not all(checks.values()):
        raise AssertionError(f"T1 validation failure: {checks}")
    return checks


def plot(summary: pd.DataFrame, output: Path) -> None:
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.5))
    axes[0].errorbar(
        summary["count"],
        summary["mean_ordering_fraction"],
        yerr=1.96 * summary["se_ordering_fraction"],
        marker="o",
        capsize=3,
    )
    axes[0].axhline(0.5, color="black", linestyle="--", label="1+1D expectation")
    axes[0].set_xscale("log", base=2)
    axes[0].set_xlabel("Sprinkled elements N")
    axes[0].set_ylabel("Ordering fraction")
    axes[0].legend()
    axes[0].grid(alpha=0.25)

    axes[1].errorbar(
        summary["count"],
        summary["mean_dimension"],
        yerr=1.96 * summary["se_dimension"],
        marker="o",
        capsize=3,
    )
    axes[1].axhline(2.0, color="black", linestyle="--", label="Target dimension")
    axes[1].set_xscale("log", base=2)
    axes[1].set_xlabel("Sprinkled elements N")
    axes[1].set_ylabel("Myrheim–Meyer estimate")
    axes[1].legend()
    axes[1].grid(alpha=0.25)
    fig.suptitle("T1: conditioned Poisson sprinkling in a 1+1D causal diamond")
    fig.tight_layout()
    fig.savefig(output, dpi=180, bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    root = Path(__file__).resolve().parents[2]
    parser = argparse.ArgumentParser()
    parser.add_argument("--sizes", nargs="+", type=int, default=[64, 128, 256, 512, 1024])
    parser.add_argument("--repeats", type=int, default=100)
    parser.add_argument("--seed", type=int, default=20260802)
    parser.add_argument("--half-extent", type=float, default=1.0)
    parser.add_argument("--output-dir", type=Path, default=root / "results/t1_causal_set")
    args = parser.parse_args()

    samples = run_sweep(args.sizes, args.repeats, args.seed, args.half_extent)
    summary = summarize(samples)
    checks = validate(samples, summary, args.seed)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    samples.to_csv(args.output_dir / "samples.csv", index=False)
    summary.to_csv(args.output_dir / "summary.csv", index=False, float_format="%.10g")
    plot(summary, args.output_dir / "ordering_dimension.png")
    metadata = {
        "model_id": "T1",
        "claim": "Recover 1+1D ordering statistics from a conditioned Poisson sprinkling",
        "parameters": {
            "sizes": args.sizes,
            "repeats": args.repeats,
            "seed": args.seed,
            "half_extent": args.half_extent,
        },
        "units": "coordinates are dimensionless in units of the diamond half-extent",
        "assumptions": [
            "Minkowski 1+1D",
            "uniform sprinkling conditional on element count N",
            "strict causal order in null coordinates",
            "no dynamics or matter fields",
        ],
        "expected_ordering_fraction_d2": expected_ordering_fraction(2),
        "checks": checks,
        "versions": {
            "python": platform.python_version(),
            "numpy": np.__version__,
            "scipy": scipy.__version__,
            "pandas": pd.__version__,
            "matplotlib": __import__("matplotlib").__version__,
        },
        "randomness_used": True,
        "random_seed": args.seed,
        "command": (
            "MPLCONFIGDIR=python-code/.mplconfig python-code/.venv/bin/python "
            "python-code/toy_models/t1_causal_set.py"
        ),
    }
    (args.output_dir / "metadata.json").write_text(
        json.dumps(metadata, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(summary.to_string(index=False))
    print(json.dumps(checks, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
