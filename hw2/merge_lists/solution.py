class Node:
    """Узел связного списка"""
    
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __repr__(self):
        return f"Node({self.data})"


def merge_two_lists_with_dummy(list1: Node, list2: Node) -> Node:
    """
    Слияние двух отсортированных односвязных списков с использованием фиктивного элемента.
    
    Алгоритм:
    1. Создаем фиктивный узел (dummy node), который упрощает логику
    2. Используем указатель current для построения результирующего списка
    3. Сравниваем элементы из list1 и list2, добавляя меньший в результат
    4. После завершения одного списка добавляем остаток другого
    5. Возвращаем dummy.next (первый реальный узел)
    
    Временная сложность: O(n + m), где n и m - длины списков
    Пространственная сложность: O(1) - используем только указатели
    
    Args:
        list1: Голова первого отсортированного списка
        list2: Голова второго отсортированного списка
    
    Returns:
        Голова объединенного отсортированного списка
    """
    # Создаем фиктивный узел для упрощения логики
    dummy = Node(0)
    current = dummy
    
    # Проходим по обоим спискам, пока оба не пусты
    while list1 and list2:
        if list1.data <= list2.data:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    
    # Добавляем остаток непустого списка
    if list1:
        current.next = list1
    elif list2:
        current.next = list2
    
    return dummy.next


def merge_two_lists_without_dummy(list1: Node, list2: Node) -> Node:
    """
    Слияние двух отсортированных односвязных списков без использования фиктивного элемента.
    
    Алгоритм:
    1. Обрабатываем граничные случаи (пустые списки)
    2. Определяем голову результирующего списка, сравнивая первые элементы
    3. Используем указатель current для построения результирующего списка
    4. Сравниваем элементы из list1 и list2, добавляя меньший в результат
    5. После завершения одного списка добавляем остаток другого
    6. Возвращаем голову результирующего списка
    
    Временная сложность: O(n + m), где n и m - длины списков
    Пространственная сложность: O(1) - используем только указатели
    
    Args:
        list1: Голова первого отсортированного списка
        list2: Голова второго отсортированного списка
    
    Returns:
        Голова объединенного отсортированного списка
    """
    # Обрабатываем граничные случаи
    if not list1:
        return list2
    if not list2:
        return list1
    
    # Определяем голову результирующего списка
    if list1.data <= list2.data:
        head = list1
        list1 = list1.next
    else:
        head = list2
        list2 = list2.next
    
    current = head
    
    # Проходим по обоим спискам, пока оба не пусты
    while list1 and list2:
        if list1.data <= list2.data:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    
    # Добавляем остаток непустого списка
    if list1:
        current.next = list1
    elif list2:
        current.next = list2
    
    return head


def list_to_array(head: Node) -> list:
    """
    Вспомогательная функция для преобразования односвязного списка в массив.
    Используется для тестирования и отладки.
    
    Args:
        head: Голова односвязного списка
    
    Returns:
        Список значений узлов
    """
    result = []
    current = head
    while current:
        result.append(current.data)
        current = current.next
    return result


def array_to_list(arr: list) -> Node:
    """
    Вспомогательная функция для преобразования массива в односвязный список.
    Используется для тестирования и отладки.
    
    Args:
        arr: Список значений
    
    Returns:
        Голова односвязного списка
    """
    if not arr:
        return None
    
    head = Node(arr[0])
    current = head
    
    for i in range(1, len(arr)):
        current.next = Node(arr[i])
        current = current.next
    
    return head

