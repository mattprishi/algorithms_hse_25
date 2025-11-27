"""
Практические примеры использования алгоритма поиска циклов и топологической сортировки.
"""

from solution import analyze_graph, find_cycle, topological_sort


def example_1_simple_dag():
    """Пример 1: Простой ациклический граф."""
    print("\n" + "=" * 60)
    print("Пример 1: Простой DAG")
    print("=" * 60)
    
    graph = {
        'A': ['B', 'C'],
        'B': ['D'],
        'C': ['D'],
        'D': []
    }
    
    print("\nГраф: A -> B -> D")
    print("           -> C -> D")
    
    result = analyze_graph(graph)
    print(f"\nЦикл найден: {result['has_cycle']}")
    print(f"Топологическая сортировка: {result['topological_sort']}")


def example_2_simple_cycle():
    """Пример 2: Простой цикл."""
    print("\n" + "=" * 60)
    print("Пример 2: Граф с циклом")
    print("=" * 60)
    
    graph = {
        'A': ['B'],
        'B': ['C'],
        'C': ['A']
    }
    
    print("\nГраф: A -> B -> C -> A (цикл)")
    
    result = analyze_graph(graph)
    print(f"\nЦикл найден: {result['has_cycle']}")
    print(f"Найденный цикл: {result['cycle']}")


def example_3_course_prerequisites():
    """Пример 3: Предварительные условия для курсов."""
    print("\n" + "=" * 60)
    print("Пример 3: Предварительные условия для курсов")
    print("=" * 60)
    
    # Граф зависимостей курсов
    courses = {
        'Введение в программирование': ['Структуры данных'],
        'Структуры данных': ['Алгоритмы', 'Базы данных'],
        'Алгоритмы': ['Машинное обучение'],
        'Базы данных': ['Web-разработка'],
        'Математический анализ': ['Линейная алгебра'],
        'Линейная алгебра': ['Машинное обучение'],
        'Машинное обучение': [],
        'Web-разработка': []
    }
    
    print("\nЗависимости между курсами:")
    for course, prereqs in courses.items():
        if prereqs:
            print(f"  {course} требует: {', '.join(prereqs)}")
    
    result = analyze_graph(courses)
    
    if not result['has_cycle']:
        print("\n✓ Курсы можно пройти в следующем порядке:")
        for i, course in enumerate(result['topological_sort'], 1):
            print(f"  {i}. {course}")
    else:
        print("\n✗ Обнаружены циклические зависимости между курсами!")


def example_4_build_system():
    """Пример 4: Система сборки проекта."""
    print("\n" + "=" * 60)
    print("Пример 4: Система сборки проекта")
    print("=" * 60)
    
    # Зависимости модулей при сборке
    modules = {
        'utils': [],
        'config': ['utils'],
        'database': ['config', 'utils'],
        'auth': ['database', 'config'],
        'api': ['auth', 'database'],
        'frontend': ['api'],
        'tests': ['frontend', 'api', 'database']
    }
    
    print("\nЗависимости модулей:")
    for module, deps in modules.items():
        if deps:
            print(f"  {module} зависит от: {', '.join(deps)}")
        else:
            print(f"  {module} — независимый модуль")
    
    result = analyze_graph(modules)
    
    if not result['has_cycle']:
        print("\n✓ Порядок компиляции модулей:")
        for i, module in enumerate(result['topological_sort'], 1):
            print(f"  {i}. {module}")


def example_5_circular_import():
    """Пример 5: Обнаружение циклических импортов."""
    print("\n" + "=" * 60)
    print("Пример 5: Обнаружение циклических импортов")
    print("=" * 60)
    
    # Граф с циклическими импортами
    imports = {
        'module_a.py': ['module_b.py'],
        'module_b.py': ['module_c.py'],
        'module_c.py': ['module_d.py'],
        'module_d.py': ['module_b.py']  # Циклический импорт!
    }
    
    print("\nГраф импортов:")
    for module, imported in imports.items():
        print(f"  {module} импортирует: {', '.join(imported)}")
    
    result = analyze_graph(imports)
    
    if result['has_cycle']:
        print("\n✗ ОШИБКА: Обнаружен циклический импорт!")
        print(f"Цикл: {' -> '.join(result['cycle'])}")
        print("\nЭто приведет к ошибке ImportError в Python!")


def example_6_task_scheduling():
    """Пример 6: Планирование задач в проекте."""
    print("\n" + "=" * 60)
    print("Пример 6: Планирование задач в проекте")
    print("=" * 60)
    
    tasks = {
        'Планирование': ['Дизайн', 'Архитектура'],
        'Дизайн': ['Разработка UI'],
        'Архитектура': ['Разработка Backend', 'Разработка Frontend'],
        'Разработка Backend': ['Интеграция'],
        'Разработка Frontend': ['Разработка UI'],
        'Разработка UI': ['Интеграция'],
        'Интеграция': ['Тестирование'],
        'Тестирование': ['Развертывание'],
        'Развертывание': []
    }
    
    result = analyze_graph(tasks)
    
    if not result['has_cycle']:
        print("\n✓ План выполнения задач:")
        print("\nФаза | Задача")
        print("-" * 40)
        for i, task in enumerate(result['topological_sort'], 1):
            print(f"  {i:2}  | {task}")
        
        print(f"\nОбщее количество задач: {len(result['topological_sort'])}")


def example_7_using_helper_functions():
    """Пример 7: Использование вспомогательных функций."""
    print("\n" + "=" * 60)
    print("Пример 7: Использование вспомогательных функций")
    print("=" * 60)
    
    # DAG для топологической сортировки
    dag = {
        '1': ['2', '3'],
        '2': ['4'],
        '3': ['4'],
        '4': []
    }
    
    print("\nПроверка на наличие цикла:")
    cycle = find_cycle(dag)
    print(f"Цикл: {cycle}")
    
    print("\nТопологическая сортировка:")
    topo = topological_sort(dag)
    print(f"Результат: {topo}")
    
    # Граф с циклом
    cyclic = {
        'X': ['Y'],
        'Y': ['Z'],
        'Z': ['X']
    }
    
    print("\n\nПроверка графа с циклом:")
    cycle = find_cycle(cyclic)
    print(f"Цикл: {cycle}")
    
    topo = topological_sort(cyclic)
    print(f"Топологическая сортировка: {topo}")


def main():
    """Запуск всех примеров."""
    print("\n" + "=" * 60)
    print("ПРАКТИЧЕСКИЕ ПРИМЕРЫ ИСПОЛЬЗОВАНИЯ")
    print("=" * 60)
    
    example_1_simple_dag()
    example_2_simple_cycle()
    example_3_course_prerequisites()
    example_4_build_system()
    example_5_circular_import()
    example_6_task_scheduling()
    example_7_using_helper_functions()
    
    print("\n" + "=" * 60)
    print("Все примеры выполнены")
    print("=" * 60 + "\n")


if __name__ == '__main__':
    main()

