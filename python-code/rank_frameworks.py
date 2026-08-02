"""Compute deterministic framework rankings under fixed weight scenarios."""

from __future__ import annotations

import argparse
import json
import os
import platform
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", str(Path(__file__).resolve().parent / ".mplconfig"))

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


CRITERIA = [
    "quantum_consistency",
    "gr_recovery",
    "conservation_causality",
    "mathematical_clarity",
    "testability",
    "computational_feasibility",
]


def load_inputs(scores_path: Path, weights_path: Path) -> tuple[pd.DataFrame, pd.DataFrame]:
    scores = pd.read_csv(scores_path)
    weights = pd.read_csv(weights_path)
    missing_scores = set(CRITERIA) - set(scores.columns)
    missing_weights = set(CRITERIA) - set(weights.columns)
    if missing_scores or missing_weights:
        raise ValueError(
            f"Missing criteria: scores={sorted(missing_scores)}, weights={sorted(missing_weights)}"
        )
    values = scores[CRITERIA].to_numpy(dtype=float)
    if not np.logical_and(values >= 0, values <= 5).all():
        raise ValueError("Every framework score must be in [0, 5]")
    weight_sums = weights[CRITERIA].sum(axis=1).to_numpy(dtype=float)
    if not np.allclose(weight_sums, 1.0, rtol=0.0, atol=1e-12):
        raise ValueError(f"Weights must sum to 1; got {weight_sums.tolist()}")
    if scores["framework_id"].duplicated().any():
        raise ValueError("framework_id values must be unique")
    return scores, weights


def compute_rankings(scores: pd.DataFrame, weights: pd.DataFrame) -> pd.DataFrame:
    rows: list[pd.DataFrame] = []
    for _, weight_row in weights.iterrows():
        scenario = str(weight_row["scenario"])
        vector = weight_row[CRITERIA].to_numpy(dtype=float)
        scenario_rows = scores[["framework_id", "framework", "is_uv_candidate"]].copy()
        scenario_rows.insert(0, "scenario", scenario)
        scenario_rows["weighted_score"] = scores[CRITERIA].to_numpy(dtype=float) @ vector
        scenario_rows["overall_rank"] = (
            scenario_rows["weighted_score"].rank(method="min", ascending=False).astype(int)
        )
        scenario_rows["uv_candidate_rank"] = pd.Series(pd.NA, index=scenario_rows.index, dtype="Int64")
        uv_mask = scenario_rows["is_uv_candidate"].astype(bool)
        scenario_rows.loc[uv_mask, "uv_candidate_rank"] = (
            scenario_rows.loc[uv_mask, "weighted_score"]
            .rank(method="min", ascending=False)
            .astype(int)
        )
        rows.append(scenario_rows)
    return pd.concat(rows, ignore_index=True).sort_values(
        ["scenario", "overall_rank", "framework_id"], ignore_index=True
    )


def plot_rankings(rankings: pd.DataFrame, output_path: Path) -> None:
    scenarios = rankings["scenario"].drop_duplicates().tolist()
    fig, axes = plt.subplots(1, len(scenarios), figsize=(13, 6), sharex=True)
    if len(scenarios) == 1:
        axes = [axes]
    for axis, scenario in zip(axes, scenarios):
        subset = rankings[rankings["scenario"] == scenario].sort_values("weighted_score")
        colors = ["#4C78A8" if value else "#B8B8B8" for value in subset["is_uv_candidate"]]
        axis.barh(subset["framework"], subset["weighted_score"], color=colors)
        axis.set_title(scenario.replace("_", " ").title())
        axis.set_xlabel("Weighted score (0–5)")
        axis.set_xlim(0, 5)
        axis.grid(axis="x", alpha=0.25)
    fig.suptitle("Quantum-gravity framework ranking sensitivity\nGray = infrared benchmark, not UV candidate")
    fig.tight_layout()
    fig.savefig(output_path, dpi=180, bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser()
    parser.add_argument("--scores", type=Path, default=root / "data/framework_scores.csv")
    parser.add_argument("--weights", type=Path, default=root / "data/ranking_weights.csv")
    parser.add_argument("--output-dir", type=Path, default=root / "results")
    args = parser.parse_args()

    scores, weights = load_inputs(args.scores, args.weights)
    rankings = compute_rankings(scores, weights)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    ranking_path = args.output_dir / "framework_rankings.csv"
    figure_path = args.output_dir / "framework_ranking_sensitivity.png"
    metadata_path = args.output_dir / "framework_ranking_metadata.json"
    rankings.to_csv(ranking_path, index=False, float_format="%.3f")
    plot_rankings(rankings, figure_path)

    winners = {}
    for scenario, subset in rankings.groupby("scenario", sort=False):
        overall = subset.sort_values("overall_rank").iloc[0]
        uv = subset[subset["is_uv_candidate"]].sort_values("uv_candidate_rank").iloc[0]
        winners[scenario] = {
            "overall": str(overall["framework_id"]),
            "uv_candidate": str(uv["framework_id"]),
        }
    metadata = {
        "command": (
            "MPLCONFIGDIR=python-code/.mplconfig python-code/.venv/bin/python "
            "python-code/rank_frameworks.py"
        ),
        "inputs": [str(args.scores), str(args.weights)],
        "criteria": CRITERIA,
        "weight_sums": {
            str(row["scenario"]): float(row[CRITERIA].sum()) for _, row in weights.iterrows()
        },
        "winners": winners,
        "versions": {
            "python": platform.python_version(),
            "numpy": np.__version__,
            "pandas": pd.__version__,
            "matplotlib": __import__("matplotlib").__version__,
        },
        "units": "dimensionless ordinal scores on [0, 5]",
        "randomness_used": False,
    }
    metadata_path.write_text(json.dumps(metadata, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(rankings.to_string(index=False))


if __name__ == "__main__":
    main()
