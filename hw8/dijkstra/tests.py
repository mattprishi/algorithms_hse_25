import pytest
from solution import dijkstra, dijkstra_with_path


def test_empty_graph():
    graph = {}
    result = dijkstra(graph, 1)
    assert result == {}


def test_single_node_no_edges():
    graph = {1: {}}
    result = dijkstra(graph, 1)
    assert result == {1: 0}


def test_single_node_with_end():
    graph = {1: {}}
    result = dijkstra(graph, 1, 1)
    assert result == 0


def test_start_not_in_graph():
    graph = {1: {2: 1}, 2: {}}
    result = dijkstra(graph, 3)
    assert result == {}


def test_start_not_in_graph_with_end():
    graph = {1: {2: 1}, 2: {}}
    result = dijkstra(graph, 3, 2)
    assert result is None


def test_two_nodes_connected():
    graph = {
        1: {2: 5},
        2: {}
    }
    result = dijkstra(graph, 1)
    assert result == {1: 0, 2: 5}


def test_two_nodes_shortest_path():
    graph = {
        1: {2: 5},
        2: {}
    }
    result = dijkstra(graph, 1, 2)
    assert result == 5


def test_two_nodes_unreachable():
    graph = {
        1: {},
        2: {}
    }
    result = dijkstra(graph, 1, 2)
    assert result is None


def test_simple_triangle():
    graph = {
        1: {2: 1, 3: 4},
        2: {3: 2},
        3: {}
    }
    result = dijkstra(graph, 1)
    assert result == {1: 0, 2: 1, 3: 3}


def test_multiple_paths_choose_shortest():
    graph = {
        1: {2: 7, 3: 9, 4: 20},
        2: {3: 10, 4: 15},
        3: {4: 2},
        4: {}
    }
    result = dijkstra(graph, 1)
    assert result == {1: 0, 2: 7, 3: 9, 4: 11}


def test_with_cycle():
    graph = {
        1: {2: 1},
        2: {3: 1},
        3: {1: 1, 4: 1},
        4: {}
    }
    result = dijkstra(graph, 1)
    assert result == {1: 0, 2: 1, 3: 2, 4: 3}


def test_zero_weight_edges():
    graph = {
        1: {2: 0, 3: 5},
        2: {3: 1},
        3: {}
    }
    result = dijkstra(graph, 1)
    assert result == {1: 0, 2: 0, 3: 1}


def test_all_zero_weights():
    graph = {
        1: {2: 0, 3: 0},
        2: {4: 0},
        3: {4: 0},
        4: {}
    }
    result = dijkstra(graph, 1)
    assert result == {1: 0, 2: 0, 3: 0, 4: 0}


def test_unreachable_nodes():
    graph = {
        1: {2: 1},
        2: {},
        3: {4: 1},
        4: {}
    }
    result = dijkstra(graph, 1)
    assert result[1] == 0
    assert result[2] == 1
    assert result[3] == float('inf')
    assert result[4] == float('inf')


def test_self_loop_ignored():
    graph = {
        1: {1: 5, 2: 1},
        2: {3: 1},
        3: {}
    }
    result = dijkstra(graph, 1)
    assert result == {1: 0, 2: 1, 3: 2}


def test_complete_graph():
    graph = {
        1: {2: 1, 3: 2, 4: 5},
        2: {1: 1, 3: 1, 4: 3},
        3: {1: 2, 2: 1, 4: 1},
        4: {1: 5, 2: 3, 3: 1}
    }
    result = dijkstra(graph, 1)
    assert result == {1: 0, 2: 1, 3: 2, 4: 3}


def test_linear_chain():
    graph = {
        1: {2: 1},
        2: {3: 2},
        3: {4: 3},
        4: {5: 4},
        5: {}
    }
    result = dijkstra(graph, 1)
    assert result == {1: 0, 2: 1, 3: 3, 4: 6, 5: 10}


def test_star_topology():
    graph = {
        1: {2: 1, 3: 2, 4: 3, 5: 4},
        2: {},
        3: {},
        4: {},
        5: {}
    }
    result = dijkstra(graph, 1)
    assert result == {1: 0, 2: 1, 3: 2, 4: 3, 5: 4}


def test_diamond_graph():
    graph = {
        1: {2: 1, 3: 4},
        2: {4: 1},
        3: {4: 1},
        4: {}
    }
    result = dijkstra(graph, 1)
    assert result == {1: 0, 2: 1, 3: 4, 4: 2}


def test_large_weights():
    graph = {
        1: {2: 1000000},
        2: {3: 2000000},
        3: {}
    }
    result = dijkstra(graph, 1)
    assert result == {1: 0, 2: 1000000, 3: 3000000}


def test_string_nodes():
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'C': 2, 'D': 5},
        'C': {'D': 1},
        'D': {}
    }
    result = dijkstra(graph, 'A')
    assert result == {'A': 0, 'B': 1, 'C': 3, 'D': 4}


def test_mixed_node_types():
    graph = {
        1: {'a': 1},
        'a': {2.5: 2},
        2.5: {}
    }
    result = dijkstra(graph, 1)
    assert result == {1: 0, 'a': 1, 2.5: 3}


def test_dijkstra_with_path_simple():
    graph = {
        1: {2: 1, 3: 4},
        2: {3: 2},
        3: {}
    }
    distance, path = dijkstra_with_path(graph, 1, 3)
    assert distance == 3
    assert path == [1, 2, 3]


def test_dijkstra_with_path_direct():
    graph = {
        1: {2: 5},
        2: {}
    }
    distance, path = dijkstra_with_path(graph, 1, 2)
    assert distance == 5
    assert path == [1, 2]


def test_dijkstra_with_path_same_node():
    graph = {
        1: {2: 1},
        2: {}
    }
    distance, path = dijkstra_with_path(graph, 1, 1)
    assert distance == 0
    assert path == [1]


def test_dijkstra_with_path_unreachable():
    graph = {
        1: {2: 1},
        2: {},
        3: {}
    }
    distance, path = dijkstra_with_path(graph, 1, 3)
    assert distance is None
    assert path == []


def test_dijkstra_with_path_complex():
    graph = {
        1: {2: 7, 3: 9, 4: 20},
        2: {3: 10, 4: 15},
        3: {4: 2},
        4: {}
    }
    distance, path = dijkstra_with_path(graph, 1, 4)
    assert distance == 11
    assert path == [1, 3, 4]


def test_dijkstra_with_path_empty_graph():
    graph = {}
    distance, path = dijkstra_with_path(graph, 1, 2)
    assert distance is None
    assert path == []


def test_dijkstra_with_path_start_not_in_graph():
    graph = {1: {2: 1}, 2: {}}
    distance, path = dijkstra_with_path(graph, 3, 2)
    assert distance is None
    assert path == []


def test_dijkstra_with_path_end_not_in_graph():
    graph = {1: {2: 1}, 2: {}}
    distance, path = dijkstra_with_path(graph, 1, 3)
    assert distance is None
    assert path == []


def test_multiple_calls_same_graph():
    graph = {
        1: {2: 1, 3: 4},
        2: {3: 2, 4: 5},
        3: {4: 1},
        4: {}
    }
    
    result1 = dijkstra(graph, 1, 4)
    result2 = dijkstra(graph, 1, 3)
    result3 = dijkstra(graph, 2, 4)
    
    assert result1 == 4
    assert result2 == 3
    assert result3 == 3


def test_bidirectional_edges():
    graph = {
        1: {2: 5},
        2: {1: 5, 3: 3},
        3: {2: 3}
    }
    
    result_forward = dijkstra(graph, 1, 3)
    result_backward = dijkstra(graph, 3, 1)
    
    assert result_forward == 8
    assert result_backward == 8


def test_floating_point_weights():
    graph = {
        1: {2: 1.5, 3: 2.7},
        2: {3: 0.8},
        3: {}
    }
    result = dijkstra(graph, 1)
    assert result[1] == 0
    assert result[2] == 1.5
    assert abs(result[3] - 2.3) < 0.0001


def test_single_edge_graph():
    graph = {
        1: {2: 10},
        2: {}
    }
    result = dijkstra(graph, 1)
    assert result == {1: 0, 2: 10}


def test_path_with_zero_weight_edges():
    graph = {
        1: {2: 0},
        2: {3: 0},
        3: {4: 1},
        4: {}
    }
    distance, path = dijkstra_with_path(graph, 1, 4)
    assert distance == 1
    assert path == [1, 2, 3, 4]


def test_many_nodes_star():
    graph = {i: {} for i in range(1, 101)}
    graph[0] = {i: i for i in range(1, 101)}
    
    result = dijkstra(graph, 0, 50)
    assert result == 50


def test_no_outgoing_edges_from_start():
    graph = {
        1: {},
        2: {3: 1},
        3: {}
    }
    result = dijkstra(graph, 1)
    assert result[1] == 0
    assert result[2] == float('inf')
    assert result[3] == float('inf')


def test_complex_weighted_graph():
    graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'C': 1, 'D': 5},
        'C': {'D': 8, 'E': 10},
        'D': {'E': 2, 'F': 6},
        'E': {'F': 3},
        'F': {}
    }
    result = dijkstra(graph, 'A')
    assert result == {'A': 0, 'B': 4, 'C': 2, 'D': 9, 'E': 11, 'F': 14}


def test_equal_weight_multiple_paths():
    graph = {
        1: {2: 1, 3: 1},
        2: {4: 1},
        3: {4: 1},
        4: {}
    }
    result = dijkstra(graph, 1, 4)
    assert result == 2

