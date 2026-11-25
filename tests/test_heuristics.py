
from src.heuristics import minimum_degree, minimum_fill


def test_minimum_degree_returns_all_nodes():
    graph = [
        {1, 2},
        {0, 2},
        {0, 1, 3},
        {2}
    ]

    order = minimum_degree(graph)

    assert sorted(order) == [0, 1, 2, 3]


def test_minimum_fill_returns_all_nodes():
    graph = [
        {1, 2},
        {0, 2},
        {0, 1, 3},
        {2}
    ]

    order = minimum_fill(graph, seed=42)

    assert sorted(order) == [0, 1, 2, 3]


def test_minimum_degree_does_not_modify_original_graph():
    graph = [
        {1, 2},
        {0, 2},
        {0, 1}
    ]

    original_graph = [neighbors.copy() for neighbors in graph]

    minimum_degree(graph)

    assert graph == original_graph


def test_minimum_fill_is_reproducible():
    graph = [
        {1, 2},
        {0, 2},
        {0, 1, 3},
        {2}
    ]

    first_order = minimum_fill(graph, seed=42)
    second_order = minimum_fill(graph, seed=42)

    assert first_order == second_order


def test_heuristics_handle_empty_graph():
    assert minimum_degree([]) == []
    assert minimum_fill([]) == []
