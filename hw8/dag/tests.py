import pytest
from solution import analyze_graph, find_cycle, topological_sort


def is_valid_topological_sort(graph, topo_order):
    """Проверяет корректность топологической сортировки."""
    if not topo_order:
        return len(graph) == 0
    
    position = {vertex: idx for idx, vertex in enumerate(topo_order)}
    
    for u in graph:
        for v in graph[u]:
            if u not in position or v not in position:
                continue
            if position[u] >= position[v]:
                return False
    
    return True


def is_valid_cycle(graph, cycle):
    """Проверяет, что путь действительно образует цикл в графе."""
    if not cycle or len(cycle) < 2:
        return False
    
    # Проверяем, что начало и конец совпадают
    if cycle[0] != cycle[-1]:
        return False
    
    # Проверяем, что каждое ребро существует в графе
    for i in range(len(cycle) - 1):
        if cycle[i] not in graph or cycle[i + 1] not in graph.get(cycle[i], []):
            return False
    
    return True


# Тесты для графов без циклов


def test_empty_graph():
    """Пустой граф не содержит циклов."""
    graph = {}
    result = analyze_graph(graph)
    
    assert result['has_cycle'] is False
    assert result['cycle'] is None
    assert result['topological_sort'] == []


def test_single_vertex_no_edges():
    """Один узел без рёбер."""
    graph = {'A': []}
    result = analyze_graph(graph)
    
    assert result['has_cycle'] is False
    assert result['cycle'] is None
    assert result['topological_sort'] == ['A']


def test_simple_chain():
    """Простая цепочка: A -> B -> C."""
    graph = {
        'A': ['B'],
        'B': ['C'],
        'C': []
    }
    result = analyze_graph(graph)
    
    assert result['has_cycle'] is False
    assert result['cycle'] is None
    assert is_valid_topological_sort(graph, result['topological_sort'])
    assert result['topological_sort'] == ['A', 'B', 'C']


def test_simple_dag():
    """Простой DAG с ветвлением."""
    graph = {
        'A': ['B', 'C'],
        'B': ['D'],
        'C': ['D'],
        'D': []
    }
    result = analyze_graph(graph)
    
    assert result['has_cycle'] is False
    assert result['cycle'] is None
    assert is_valid_topological_sort(graph, result['topological_sort'])


def test_complex_dag():
    """Сложный DAG с множественными путями."""
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['E', 'F'],
        'D': ['G'],
        'E': ['G'],
        'F': ['G'],
        'G': []
    }
    result = analyze_graph(graph)
    
    assert result['has_cycle'] is False
    assert result['cycle'] is None
    assert is_valid_topological_sort(graph, result['topological_sort'])


def test_disconnected_dag():
    """Несвязный граф без циклов."""
    graph = {
        'A': ['B'],
        'B': [],
        'C': ['D'],
        'D': [],
        'E': []
    }
    result = analyze_graph(graph)
    
    assert result['has_cycle'] is False
    assert result['cycle'] is None
    assert is_valid_topological_sort(graph, result['topological_sort'])


def test_linear_sequence():
    """Длинная линейная последовательность."""
    graph = {
        '1': ['2'],
        '2': ['3'],
        '3': ['4'],
        '4': ['5'],
        '5': []
    }
    result = analyze_graph(graph)
    
    assert result['has_cycle'] is False
    assert result['cycle'] is None
    assert result['topological_sort'] == ['1', '2', '3', '4', '5']


# Тесты для графов с циклами


def test_self_loop():
    """Вершина с петлёй на себя."""
    graph = {
        'A': ['A']
    }
    result = analyze_graph(graph)
    
    assert result['has_cycle'] is True
    assert result['topological_sort'] is None
    assert is_valid_cycle(graph, result['cycle'])


def test_simple_cycle_two_nodes():
    """Простой цикл из двух узлов: A -> B -> A."""
    graph = {
        'A': ['B'],
        'B': ['A']
    }
    result = analyze_graph(graph)
    
    assert result['has_cycle'] is True
    assert result['topological_sort'] is None
    assert is_valid_cycle(graph, result['cycle'])


def test_simple_cycle_three_nodes():
    """Цикл из трёх узлов: A -> B -> C -> A."""
    graph = {
        'A': ['B'],
        'B': ['C'],
        'C': ['A']
    }
    result = analyze_graph(graph)
    
    assert result['has_cycle'] is True
    assert result['topological_sort'] is None
    assert is_valid_cycle(graph, result['cycle'])


def test_cycle_with_tail():
    """Граф с хвостом перед циклом: D -> A -> B -> C -> A."""
    graph = {
        'D': ['A'],
        'A': ['B'],
        'B': ['C'],
        'C': ['A']
    }
    result = analyze_graph(graph)
    
    assert result['has_cycle'] is True
    assert result['topological_sort'] is None
    assert is_valid_cycle(graph, result['cycle'])


def test_complex_graph_with_cycle():
    """Сложный граф с циклом."""
    graph = {
        'A': ['B', 'C'],
        'B': ['D'],
        'C': ['D'],
        'D': ['E'],
        'E': ['B']  # Цикл: B -> D -> E -> B
    }
    result = analyze_graph(graph)
    
    assert result['has_cycle'] is True
    assert result['topological_sort'] is None
    assert is_valid_cycle(graph, result['cycle'])


def test_multiple_cycles():
    """Граф с несколькими циклами."""
    graph = {
        'A': ['B'],
        'B': ['C'],
        'C': ['A'],  # Первый цикл
        'D': ['E'],
        'E': ['D']   # Второй цикл
    }
    result = analyze_graph(graph)
    
    assert result['has_cycle'] is True
    assert result['topological_sort'] is None
    # Должен найти хотя бы один цикл
    assert result['cycle'] is not None


def test_long_cycle():
    """Длинный цикл."""
    graph = {
        '1': ['2'],
        '2': ['3'],
        '3': ['4'],
        '4': ['5'],
        '5': ['1']
    }
    result = analyze_graph(graph)
    
    assert result['has_cycle'] is True
    assert result['topological_sort'] is None
    assert is_valid_cycle(graph, result['cycle'])


# Тесты вспомогательных функций


def test_find_cycle_no_cycle():
    """find_cycle возвращает None для ациклического графа."""
    graph = {
        'A': ['B'],
        'B': ['C'],
        'C': []
    }
    cycle = find_cycle(graph)
    assert cycle is None


def test_find_cycle_with_cycle():
    """find_cycle возвращает цикл, если он есть."""
    graph = {
        'A': ['B'],
        'B': ['C'],
        'C': ['A']
    }
    cycle = find_cycle(graph)
    assert cycle is not None
    assert is_valid_cycle(graph, cycle)


def test_topological_sort_dag():
    """topological_sort возвращает правильный порядок для DAG."""
    graph = {
        'A': ['B', 'C'],
        'B': ['D'],
        'C': ['D'],
        'D': []
    }
    topo = topological_sort(graph)
    assert topo is not None
    assert is_valid_topological_sort(graph, topo)


def test_topological_sort_with_cycle():
    """topological_sort возвращает None для графа с циклом."""
    graph = {
        'A': ['B'],
        'B': ['C'],
        'C': ['A']
    }
    topo = topological_sort(graph)
    assert topo is None


# Дополнительные граничные случаи


def test_graph_with_isolated_vertices():
    """Граф с изолированными вершинами."""
    graph = {
        'A': ['B'],
        'B': [],
        'C': [],
        'D': []
    }
    result = analyze_graph(graph)
    
    assert result['has_cycle'] is False
    assert result['cycle'] is None
    assert is_valid_topological_sort(graph, result['topological_sort'])


def test_complete_dag():
    """Полный DAG (все возможные рёбра без нарушения порядка)."""
    graph = {
        '1': ['2', '3', '4'],
        '2': ['3', '4'],
        '3': ['4'],
        '4': []
    }
    result = analyze_graph(graph)
    
    assert result['has_cycle'] is False
    assert result['cycle'] is None
    assert is_valid_topological_sort(graph, result['topological_sort'])


def test_tree_structure():
    """Древовидная структура."""
    graph = {
        'root': ['left', 'right'],
        'left': ['left_child1', 'left_child2'],
        'right': ['right_child1', 'right_child2'],
        'left_child1': [],
        'left_child2': [],
        'right_child1': [],
        'right_child2': []
    }
    result = analyze_graph(graph)
    
    assert result['has_cycle'] is False
    assert result['cycle'] is None
    assert is_valid_topological_sort(graph, result['topological_sort'])


def test_diamond_shape():
    """Ромбовидный граф."""
    graph = {
        'A': ['B', 'C'],
        'B': ['D'],
        'C': ['D'],
        'D': []
    }
    result = analyze_graph(graph)
    
    assert result['has_cycle'] is False
    assert result['cycle'] is None
    topo = result['topological_sort']
    assert topo[0] == 'A'
    assert topo[-1] == 'D'
    assert is_valid_topological_sort(graph, topo)


def test_numeric_vertices():
    """Граф с числовыми вершинами."""
    graph = {
        1: [2, 3],
        2: [4],
        3: [4],
        4: []
    }
    result = analyze_graph(graph)
    
    assert result['has_cycle'] is False
    assert result['cycle'] is None
    assert is_valid_topological_sort(graph, result['topological_sort'])


def test_mixed_connectivity():
    """Граф со смешанной связностью."""
    graph = {
        'A': ['B'],
        'B': ['C', 'D'],
        'C': ['E'],
        'D': ['E'],
        'E': ['F'],
        'F': [],
        'G': ['H'],
        'H': []
    }
    result = analyze_graph(graph)
    
    assert result['has_cycle'] is False
    assert result['cycle'] is None
    assert is_valid_topological_sort(graph, result['topological_sort'])


# Тесты для проверки корректности обнаружения конкретных циклов


def test_cycle_detection_path():
    """Проверка, что обнаруженный цикл действительно существует."""
    graph = {
        'A': ['B'],
        'B': ['C'],
        'C': ['D'],
        'D': ['B']  # Цикл: B -> C -> D -> B
    }
    result = analyze_graph(graph)
    
    assert result['has_cycle'] is True
    cycle = result['cycle']
    assert cycle is not None
    
    # Проверяем, что цикл содержит узлы B, C, D
    cycle_set = set(cycle[:-1])  # Исключаем последний элемент (дубликат начала)
    assert 'B' in cycle_set
    assert 'C' in cycle_set
    assert 'D' in cycle_set


def test_early_cycle_detection():
    """Алгоритм должен остановиться при первом обнаружении цикла."""
    graph = {
        'A': ['B'],
        'B': ['A'],  # Цикл прямо здесь
        'C': ['D'],
        'D': ['C']   # И здесь тоже цикл
    }
    result = analyze_graph(graph)
    
    assert result['has_cycle'] is True
    assert result['cycle'] is not None
    # Должен найти один из циклов
    assert is_valid_cycle(graph, result['cycle'])

