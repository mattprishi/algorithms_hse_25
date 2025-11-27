"""
Демонстрация работы алгоритма поиска циклов и топологической сортировки.
"""

from solution import analyze_graph, find_cycle, topological_sort


def print_graph(graph, title="Граф"):
    """Красиво выводит граф."""
    print(f"\n{title}:")
    print("-" * 50)
    for vertex in sorted(graph.keys()):
        neighbors = graph[vertex]
        if neighbors:
            print(f"  {vertex} -> {', '.join(map(str, neighbors))}")
        else:
            print(f"  {vertex} -> (нет исходящих рёбер)")
    print("-" * 50)


def demo_acyclic_graph():
    """Демонстрация работы с ациклическим графом (DAG)."""
    print("\n" + "=" * 70)
    print("ПРИМЕР 1: Ациклический граф (DAG)")
    print("=" * 70)
    
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['E', 'F'],
        'D': ['G'],
        'E': ['G'],
        'F': ['G'],
        'G': []
    }
    
    print_graph(graph)
    
    result = analyze_graph(graph)
    
    print(f"\nНаличие цикла: {result['has_cycle']}")
    print(f"Цикл: {result['cycle']}")
    print(f"Топологическая сортировка: {result['topological_sort']}")
    
    # Проверка корректности
    topo = result['topological_sort']
    print(f"\n✓ Граф является DAG")
    print(f"✓ Топологический порядок: {' -> '.join(topo)}")


def demo_simple_cycle():
    """Демонстрация обнаружения простого цикла."""
    print("\n" + "=" * 70)
    print("ПРИМЕР 2: Граф с простым циклом")
    print("=" * 70)
    
    graph = {
        'A': ['B'],
        'B': ['C'],
        'C': ['A']
    }
    
    print_graph(graph)
    
    result = analyze_graph(graph)
    
    print(f"\nНаличие цикла: {result['has_cycle']}")
    print(f"Обнаруженный цикл: {result['cycle']}")
    print(f"Топологическая сортировка: {result['topological_sort']}")
    
    if result['cycle']:
        cycle_str = ' -> '.join(map(str, result['cycle']))
        print(f"\n✗ Граф содержит цикл: {cycle_str}")


def demo_complex_cycle():
    """Демонстрация обнаружения цикла в сложном графе."""
    print("\n" + "=" * 70)
    print("ПРИМЕР 3: Сложный граф с циклом")
    print("=" * 70)
    
    graph = {
        'A': ['B', 'C'],
        'B': ['D'],
        'C': ['D'],
        'D': ['E'],
        'E': ['B', 'F'],  # E -> B создаёт цикл
        'F': []
    }
    
    print_graph(graph)
    
    result = analyze_graph(graph)
    
    print(f"\nНаличие цикла: {result['has_cycle']}")
    print(f"Обнаруженный цикл: {result['cycle']}")
    print(f"Топологическая сортировка: {result['topological_sort']}")
    
    if result['cycle']:
        cycle_str = ' -> '.join(map(str, result['cycle']))
        print(f"\n✗ Граф содержит цикл: {cycle_str}")


def demo_disconnected_dag():
    """Демонстрация работы с несвязным DAG."""
    print("\n" + "=" * 70)
    print("ПРИМЕР 4: Несвязный ациклический граф")
    print("=" * 70)
    
    graph = {
        'A': ['B'],
        'B': ['C'],
        'C': [],
        'D': ['E'],
        'E': [],
        'F': ['G', 'H'],
        'G': [],
        'H': []
    }
    
    print_graph(graph)
    
    result = analyze_graph(graph)
    
    print(f"\nНаличие цикла: {result['has_cycle']}")
    print(f"Топологическая сортировка: {result['topological_sort']}")
    
    print(f"\n✓ Граф является несвязным DAG")
    print(f"✓ Топологический порядок: {' -> '.join(result['topological_sort'])}")


def demo_self_loop():
    """Демонстрация обнаружения петли (самоцикла)."""
    print("\n" + "=" * 70)
    print("ПРИМЕР 5: Граф с петлёй (самоциклом)")
    print("=" * 70)
    
    graph = {
        'A': ['B'],
        'B': ['B', 'C'],  # B -> B (петля)
        'C': []
    }
    
    print_graph(graph)
    
    result = analyze_graph(graph)
    
    print(f"\nНаличие цикла: {result['has_cycle']}")
    print(f"Обнаруженный цикл: {result['cycle']}")
    
    if result['cycle']:
        cycle_str = ' -> '.join(map(str, result['cycle']))
        print(f"\n✗ Граф содержит петлю: {cycle_str}")


def demo_task_dependencies():
    """Практический пример: зависимости задач."""
    print("\n" + "=" * 70)
    print("ПРАКТИЧЕСКИЙ ПРИМЕР: Планирование задач с зависимостями")
    print("=" * 70)
    
    # Задачи разработки ПО с зависимостями
    tasks = {
        'requirements': ['design'],
        'design': ['backend', 'frontend'],
        'backend': ['api', 'database'],
        'frontend': ['ui_components'],
        'api': ['integration'],
        'database': ['integration'],
        'ui_components': ['integration'],
        'integration': ['testing'],
        'testing': ['deployment'],
        'deployment': []
    }
    
    print("\nЗадачи и их зависимости (A -> B означает 'A должна быть выполнена перед B'):")
    print_graph(tasks, "")
    
    result = analyze_graph(tasks)
    
    if not result['has_cycle']:
        print("\n✓ Зависимости корректны (нет циклических зависимостей)")
        print("\nПорядок выполнения задач:")
        for i, task in enumerate(result['topological_sort'], 1):
            print(f"  {i}. {task}")
    else:
        print("\n✗ Обнаружены циклические зависимости!")
        print(f"Цикл: {' -> '.join(result['cycle'])}")


def demo_circular_dependencies():
    """Пример циклических зависимостей в задачах."""
    print("\n" + "=" * 70)
    print("ПРАКТИЧЕСКИЙ ПРИМЕР: Некорректные циклические зависимости")
    print("=" * 70)
    
    # Некорректные зависимости с циклом
    tasks = {
        'task_A': ['task_B'],
        'task_B': ['task_C'],
        'task_C': ['task_D'],
        'task_D': ['task_B']  # Создаёт цикл!
    }
    
    print("\nЗадачи с циклическими зависимостями:")
    print_graph(tasks, "")
    
    result = analyze_graph(tasks)
    
    if result['has_cycle']:
        print("\n✗ ОШИБКА: Обнаружены циклические зависимости!")
        cycle_str = ' -> '.join(result['cycle'])
        print(f"Цикл: {cycle_str}")
        print("\nЭти задачи не могут быть выполнены, так как зависят друг от друга!")


def main():
    """Запуск всех демонстраций."""
    print("\n" + "=" * 70)
    print("ДЕМОНСТРАЦИЯ АЛГОРИТМА ПОИСКА ЦИКЛОВ И ТОПОЛОГИЧЕСКОЙ СОРТИРОВКИ")
    print("=" * 70)
    
    demo_acyclic_graph()
    demo_simple_cycle()
    demo_complex_cycle()
    demo_disconnected_dag()
    demo_self_loop()
    demo_task_dependencies()
    demo_circular_dependencies()
    
    print("\n" + "=" * 70)
    print("Демонстрация завершена")
    print("=" * 70 + "\n")


if __name__ == '__main__':
    main()

