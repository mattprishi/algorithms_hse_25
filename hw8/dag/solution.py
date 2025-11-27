"""
Задача: Поиск циклов в ориентированном графе и топологическая сортировка.

Используется алгоритм DFS с тремя цветами:
- Белый (0): вершина не посещена
- Серый (1): вершина в процессе обработки (в стеке рекурсии)
- Чёрный (2): вершина полностью обработана

Временная сложность: O(V + E)
Пространственная сложность: O(V)
"""


def analyze_graph(graph):
    """
    Анализирует граф на наличие циклов и выполняет топологическую сортировку.
    
    Args:
        graph: словарь, где ключи - вершины, значения - списки смежных вершин
        
    Returns:
        dict: словарь с ключами:
            - 'has_cycle': bool, есть ли цикл в графе
            - 'cycle': list или None, цикл если есть
            - 'topological_sort': list или None, топологическая сортировка если нет цикла
    """
    if not graph:
        return {
            'has_cycle': False,
            'cycle': None,
            'topological_sort': []
        }
    
    # Состояния вершин: 0 - белый, 1 - серый, 2 - чёрный
    colors = {vertex: 0 for vertex in graph}
    parent = {}
    result = []
    cycle_info = {'found': False, 'start': None, 'end': None}
    
    def dfs(u):
        """Рекурсивный DFS для обнаружения циклов и топологической сортировки."""
        colors[u] = 1  # Помечаем как серый (в процессе)
        
        for v in graph.get(u, []):
            # Если v ещё не в словаре colors, добавляем его
            if v not in colors:
                colors[v] = 0
            
            if colors[v] == 1:  # Нашли обратное ребро - это цикл
                cycle_info['found'] = True
                cycle_info['start'] = v
                cycle_info['end'] = u
                return True
            
            if colors[v] == 0:  # Белая вершина - продолжаем поиск
                parent[v] = u
                if dfs(v):
                    return True
        
        colors[u] = 2  # Помечаем как чёрный (обработан)
        result.insert(0, u)  # Добавляем в начало для топологической сортировки
        return False
    
    # Запускаем DFS из всех непосещённых вершин
    for vertex in graph:
        if colors[vertex] == 0:
            if dfs(vertex):
                break
    
    # Формируем результат
    if cycle_info['found']:
        # Восстанавливаем цикл
        # Когда нашли обратное ребро u -> v (где v серая),
        # цикл: v -> ... -> u -> v
        cycle = [cycle_info['start']]  # Начинаем с v
        current = cycle_info['end']  # u
        
        # Собираем путь от u назад до v
        path = []
        while current != cycle_info['start']:
            path.append(current)
            current = parent.get(current)
            if current is None:
                # Не должно происходить, но на всякий случай
                break
        
        # Разворачиваем путь и добавляем к циклу
        path.reverse()
        cycle.extend(path)
        # Замыкаем цикл
        cycle.append(cycle_info['start'])
        
        return {
            'has_cycle': True,
            'cycle': cycle,
            'topological_sort': None
        }
    
    return {
        'has_cycle': False,
        'cycle': None,
        'topological_sort': result
    }


def find_cycle(graph):
    """
    Находит цикл в графе, если он есть.
    
    Args:
        graph: словарь со списками смежности
        
    Returns:
        list или None: список вершин, образующих цикл, или None если цикла нет
    """
    result = analyze_graph(graph)
    return result['cycle']


def topological_sort(graph):
    """
    Выполняет топологическую сортировку графа.
    
    Args:
        graph: словарь со списками смежности
        
    Returns:
        list или None: топологически отсортированный список вершин, 
                       или None если граф содержит цикл
    """
    result = analyze_graph(graph)
    return result['topological_sort']

