import sys
from pathlib import Path

parent_dir = Path(__file__).parent.parent
sys.path.insert(0, str(parent_dir))

# гордо использую мой стек
from queue_vs_stack import Stack


def validate_stack_sequences(pushed, popped):
    """
    Проверяет, можно ли получить последовательность popped из pushed
    с помощью операций push и pop на пустом стеке.
    
    Args:
        pushed: список элементов для push (в порядке добавления)
        popped: список элементов для pop (ожидаемый порядок извлечения)
    
    Returns:
        True, если последовательность возможна, иначе False
    
    Алгоритм:
        1. Создаем пустой стек
        2. Для каждого элемента из pushed:
           - Добавляем его в стек (push)
           - Пока стек не пуст и вершина стека == текущему элементу popped:
             - Делаем pop из стека
             - Переходим к следующему элементу popped
        3. Если в конце стек пуст, последовательность валидна
    
    Временная сложность: O(n), где n = len(pushed)
    Пространственная сложность: O(n) для стека в худшем случае
    """
    if len(pushed) != len(popped):
        return False
    
    stack = Stack()
    pop_index = 0  # Указатель на текущий элемент в popped
    
    # Проходим по pushed и симулируем операции
    for value in pushed:
        stack.push(value)  # Добавляем элемент в стек
        
        # Проверяем, можем ли мы делать pop
        while not stack.is_empty() and stack.peek() == popped[pop_index]:
            stack.pop()
            pop_index += 1
    
    # Если все элементы из popped были извлечены, стек должен быть пуст
    return stack.is_empty()


if __name__ == "__main__":
    # Примеры из условия
    
    # Пример 1
    pushed1 = [1, 2, 3, 4, 5]
    popped1 = [1, 3, 5, 4, 2]
    result1 = validate_stack_sequences(pushed1, popped1)
    print(f"Пример 1: pushed={pushed1}, popped={popped1}")
    print(f"Результат: {result1}")
    print(f"Ожидается: True\n")
    
    # Пример 2
    pushed2 = [1, 2, 3]
    popped2 = [3, 1, 2]
    result2 = validate_stack_sequences(pushed2, popped2)
    print(f"Пример 2: pushed={pushed2}, popped={popped2}")
    print(f"Результат: {result2}")
    print(f"Ожидается: False")

