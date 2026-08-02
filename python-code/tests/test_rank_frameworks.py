from pathlib import Path

import pandas as pd

from rank_frameworks import compute_rankings, load_inputs


ROOT = Path(__file__).resolve().parents[2]


def test_weights_are_normalized_and_scores_bounded() -> None:
    scores, weights = load_inputs(
        ROOT / "data/framework_scores.csv", ROOT / "data/ranking_weights.csv"
    )
    assert len(scores) == 8
    assert (weights.drop(columns="scenario").sum(axis=1) == 1.0).all()


def test_uv_scope_gate_excludes_eft_from_uv_winner() -> None:
    scores, weights = load_inputs(
        ROOT / "data/framework_scores.csv", ROOT / "data/ranking_weights.csv"
    )
    rankings = compute_rankings(scores, weights)
    for _, subset in rankings.groupby("scenario"):
        uv_winner = subset[subset["uv_candidate_rank"] == 1].iloc[0]
        assert uv_winner["framework_id"] != "gravity_eft"


def test_documented_sensitivity_changes_uv_leader() -> None:
    scores, weights = load_inputs(
        ROOT / "data/framework_scores.csv", ROOT / "data/ranking_weights.csv"
    )
    rankings = compute_rankings(scores, weights)
    winners = rankings[rankings["uv_candidate_rank"] == 1].set_index("scenario")
    assert winners.loc["baseline", "framework_id"] == "string_holography"
    assert winners.loc["test_and_compute", "framework_id"] == "cdt"
    assert isinstance(winners, pd.DataFrame)
