import pytest
from solution import find_connected_components


def assert_components_equal(result, expected):
    result_set = {frozenset(component) for component in result}
    expected_set = {frozenset(component) for component in expected}
    assert result_set == expected_set


def test_empty_graph():
    graph = {}
    result = find_connected_components(graph)
    assert result == []


def test_single_node_no_edges():
    graph = {1: []}
    result = find_connected_components(graph)
    assert result == [[1]]


def test_single_node_with_self_loop():
    graph = {1: [1]}
    result = find_connected_components(graph)
    assert result == [[1]]


def test_two_connected_nodes():
    graph = {
        1: [2],
        2: [1]
    }
    result = find_connected_components(graph)
    assert result == [[1, 2]]


def test_two_isolated_nodes():
    graph = {
        1: [],
        2: []
    }
    result = find_connected_components(graph)
    assert result == [[1], [2]]


def test_simple_connected_graph():
    graph = {
        1: [2, 3],
        2: [1, 3],
        3: [1, 2]
    }
    result = find_connected_components(graph)
    assert result == [[1, 2, 3]]


def test_two_separate_components():
    graph = {
        1: [2],
        2: [1],
        3: [4],
        4: [3]
    }
    result = find_connected_components(graph)
    assert_components_equal(result, [[1, 2], [3, 4]])


def test_three_components():
    graph = {
        1: [2],
        2: [1],
        3: [4, 5],
        4: [3, 5],
        5: [3, 4],
        6: []
    }
    result = find_connected_components(graph)
    assert_components_equal(result, [[1, 2], [3, 4, 5], [6]])


def test_linear_chain():
    graph = {
        1: [2],
        2: [1, 3],
        3: [2, 4],
        4: [3, 5],
        5: [4]
    }
    result = find_connected_components(graph)
    assert result == [[1, 2, 3, 4, 5]]


def test_graph_with_cycle():
    graph = {
        1: [2],
        2: [1, 3],
        3: [2, 4],
        4: [3, 1]
    }
    result = find_connected_components(graph)
    assert result == [[1, 2, 3, 4]]


def test_star_graph():
    graph = {
        1: [2, 3, 4, 5],
        2: [1],
        3: [1],
        4: [1],
        5: [1]
    }
    result = find_connected_components(graph)
    assert result == [[1, 2, 3, 4, 5]]


def test_complete_graph():
    graph = {
        1: [2, 3, 4],
        2: [1, 3, 4],
        3: [1, 2, 4],
        4: [1, 2, 3]
    }
    result = find_connected_components(graph)
    assert result == [[1, 2, 3, 4]]


def test_many_isolated_nodes():
    graph = {
        1: [],
        2: [],
        3: [],
        4: [],
        5: []
    }
    result = find_connected_components(graph)
    assert result == [[1], [2], [3], [4], [5]]


def test_mixed_components_various_sizes():
    graph = {
        1: [],
        2: [3],
        3: [2],
        4: [5, 6, 7],
        5: [4, 6],
        6: [4, 5, 7],
        7: [4, 6],
        8: [9, 10],
        9: [8],
        10: [8]
    }
    result = find_connected_components(graph)
    assert_components_equal(result, [[1], [2, 3], [4, 5, 6, 7], [8, 9, 10]])


def test_string_nodes():
    graph = {
        'a': ['b'],
        'b': ['a', 'c'],
        'c': ['b'],
        'd': ['e'],
        'e': ['d']
    }
    result = find_connected_components(graph)
    assert_components_equal(result, [['a', 'b', 'c'], ['d', 'e']])


def test_large_graph():
    graph = {}
    for i in range(100):
        graph[i] = [i + 1] if i < 99 else [0]
    
    result = find_connected_components(graph)
    assert len(result) == 1
    assert len(result[0]) == 100


def test_asymmetric_edges():
    graph = {
        1: [2],
        2: [3],
        3: [1]
    }
    result = find_connected_components(graph)
    assert result == [[1, 2, 3]]


def test_nodes_with_multiple_self_loops():
    graph = {
        1: [1, 1, 2],
        2: [1, 2, 2]
    }
    result = find_connected_components(graph)
    assert result == [[1, 2]]


def test_bridge_node():
    graph = {
        1: [2],
        2: [1, 3],
        3: [2, 4],
        4: [3]
    }
    result = find_connected_components(graph)
    assert result == [[1, 2, 3, 4]]


def test_disconnected_pairs():
    graph = {
        1: [2],
        2: [1],
        3: [4],
        4: [3],
        5: [6],
        6: [5],
        7: [8],
        8: [7]
    }
    result = find_connected_components(graph)
    assert_components_equal(result, [[1, 2], [3, 4], [5, 6], [7, 8]])


def test_node_not_a_key():
    graph = {
        1: [2],
        3: []
    }
    result = find_connected_components(graph)
    assert_components_equal(result, [[1, 2], [3]])


def test_multiple_nodes_not_keys():
    graph = {
        1: [2, 3, 4]
    }
    result = find_connected_components(graph)
    assert_components_equal(result, [[1, 2, 3, 4]])


def test_chain_with_missing_keys():
    graph = {
        1: [2],
        3: [4]
    }
    result = find_connected_components(graph)
    assert_components_equal(result, [[1, 2], [3, 4]])


def test_isolated_node_referenced_but_not_key():
    graph = {
        1: [2],
        2: [1]
    }
    result = find_connected_components(graph)
    assert_components_equal(result, [[1, 2]])


def test_complex_missing_keys():
    graph = {
        1: [2, 3],
        4: [5, 6],
        7: []
    }
    result = find_connected_components(graph)
    assert_components_equal(result, [[1, 2, 3], [4, 5, 6], [7]])


def test_all_neighbors_not_keys():
    graph = {
        'a': ['b', 'c', 'd']
    }
    result = find_connected_components(graph)
    assert_components_equal(result, [['a', 'b', 'c', 'd']])


def test_partial_symmetry():
    graph = {
        1: [2, 3],
        2: [1]
    }
    result = find_connected_components(graph)
    assert_components_equal(result, [[1, 2, 3]])

