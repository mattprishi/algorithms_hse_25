from solution import find_connected_components


def print_components(graph, description):
    print(f"\n{description}")
    print(f"Граф: {graph}")
    components = find_connected_components(graph)
    print(f"Компоненты связности: {components}")
    print(f"Количество компонент: {len(components)}")


if __name__ == "__main__":
    print("=" * 70)
    print("Демонстрация поиска компонент связности графа")
    print("=" * 70)
    
    print_components(
        {},
        "1. Пустой граф"
    )
    
    print_components(
        {1: []},
        "2. Одна изолированная вершина"
    )
    
    print_components(
        {1: [2], 2: [1]},
        "3. Два связанных узла"
    )
    
    print_components(
        {1: [], 2: [], 3: []},
        "4. Три изолированные вершины"
    )
    
    print_components(
        {1: [2, 3], 2: [1, 3], 3: [1, 2]},
        "5. Треугольник (полный граф на 3 вершинах)"
    )
    
    print_components(
        {1: [2], 2: [1], 3: [4], 4: [3]},
        "6. Две отдельные компоненты"
    )
    
    print_components(
        {1: [2], 2: [1, 3], 3: [2, 4], 4: [3, 5], 5: [4]},
        "7. Линейная цепь"
    )
    
    print_components(
        {1: [2, 3, 4, 5], 2: [1], 3: [1], 4: [1], 5: [1]},
        "8. Звезда (центр с 4 лучами)"
    )
    
    print_components(
        {1: [2], 2: [1, 3], 3: [2, 4], 4: [3, 1]},
        "9. Цикл"
    )
    
    print_components(
        {
            1: [2],
            2: [1],
            3: [4, 5],
            4: [3, 5],
            5: [3, 4],
            6: [],
            7: [8],
            8: [7]
        },
        "10. Смешанный граф: 4 компоненты разных размеров"
    )
    
    print_components(
        {1: [2, 3], 4: [5, 6], 7: []},
        "11. Критический случай: вершины 2, 3, 5, 6 не являются ключами"
    )
    
    print_components(
        {'a': ['b'], 'b': ['a'], 'c': ['d'], 'd': ['c']},
        "12. Строковые вершины"
    )
    
    print_components(
        {1: [1, 2], 2: [1, 2]},
        "13. Граф с само-петлями и дубликатами"
    )
    
    print_components(
        {i: [i+1] if i < 9 else [0] for i in range(10)},
        "14. Цикл из 10 вершин"
    )
    
    print("\n" + "=" * 70)
    print("Демонстрация завершена")
    print("=" * 70)

