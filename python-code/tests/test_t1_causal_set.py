import numpy as np

from toy_models.t1_causal_set import (
    causal_matrix,
    expected_ordering_fraction,
    infer_dimension,
    lorentz_boost_null,
    ordering_fraction,
    run_sweep,
    sprinkle_conditioned,
    summarize,
)


def test_known_myrheim_meyer_values_and_inverse() -> None:
    assert np.isclose(expected_ordering_fraction(2), 0.5)
    assert np.isclose(expected_ordering_fraction(4), 0.1)
    assert np.isclose(infer_dimension(0.5), 2.0)
    assert np.isclose(infer_dimension(0.1), 4.0)


def test_causal_relation_is_irreflexive_transitive_and_boost_invariant() -> None:
    points = sprinkle_conditioned(64, np.random.default_rng(17))
    relation = causal_matrix(points)
    two_step = (relation.astype(np.uint8) @ relation.astype(np.uint8)) > 0
    assert not relation.diagonal().any()
    assert np.all(~two_step | relation)
    assert np.array_equal(relation, causal_matrix(lorentz_boost_null(points, 2.3)))


def test_seeded_small_sweep_recovers_two_dimensions() -> None:
    samples = run_sweep([128, 256], repeats=20, seed=1234, half_extent=1.0)
    summary = summarize(samples)
    assert (summary["mean_ordering_fraction"].sub(0.5).abs() < 0.04).all()
    assert (summary["mean_dimension"].sub(2.0).abs() < 0.35).all()


def test_ordering_fraction_for_total_and_empty_orders() -> None:
    total = np.triu(np.ones((4, 4), dtype=bool), k=1)
    empty = np.zeros((4, 4), dtype=bool)
    assert ordering_fraction(total) == 1.0
    assert ordering_fraction(empty) == 0.0
