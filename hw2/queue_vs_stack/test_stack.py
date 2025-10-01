import pytest
from .stack import Stack


class TestStack:
    """Тестовый класс для Stack"""
    
    def test_create_empty_stack(self):
        """Тест создания пустого стека"""
        stack = Stack()
        assert stack.is_empty() is True
        assert stack.size() == 0
        assert len(stack) == 0
    
    def test_push_single_element(self):
        """Тест добавления одного элемента"""
        stack = Stack()
        stack.push(1)
        
        assert stack.is_empty() is False
        assert stack.size() == 1
        assert len(stack) == 1
        assert stack.peek() == 1
    
    def test_push_multiple_elements(self):
        """Тест добавления нескольких элементов"""
        stack = Stack()
        elements = [1, 2, 3, 4, 5]
        
        for element in elements:
            stack.push(element)
        
        assert stack.size() == 5
        assert stack.peek() == 5  # Последний добавленный элемент
    
    def test_pop_single_element(self):
        """Тест извлечения одного элемента"""
        stack = Stack()
        stack.push(42)
        
        popped = stack.pop()
        assert popped == 42
        assert stack.is_empty() is True
        assert stack.size() == 0
    
    def test_pop_multiple_elements_lifo_order(self):
        """Тест извлечения элементов в порядке LIFO"""
        stack = Stack()
        elements = [1, 2, 3, 4, 5]
        
        # Добавляем элементы
        for element in elements:
            stack.push(element)
        
        # Извлекаем в обратном порядке
        popped_elements = []
        while not stack.is_empty():
            popped_elements.append(stack.pop())
        
        assert popped_elements == [5, 4, 3, 2, 1]
        assert stack.size() == 0
    
    def test_peek_without_modification(self):
        """Тест просмотра элемента без изменения стека"""
        stack = Stack()
        stack.push(10)
        stack.push(20)
        
        # Несколько раз проверяем peek
        assert stack.peek() == 20
        assert stack.peek() == 20
        assert stack.size() == 2  # Размер не изменился
    
    def test_mixed_operations(self):
        """Тест смешанных операций"""
        stack = Stack()
        
        # Добавляем элементы
        stack.push(1)
        stack.push(2)
        assert stack.size() == 2
        
        # Извлекаем один
        assert stack.pop() == 2
        assert stack.size() == 1
        
        # Добавляем еще
        stack.push(3)
        stack.push(4)
        assert stack.size() == 3
        assert stack.peek() == 4
        
        # Извлекаем все
        assert stack.pop() == 4
        assert stack.pop() == 3
        assert stack.pop() == 1
        assert stack.is_empty() is True
    
    def test_pop_from_empty_stack_raises_exception(self):
        """Тест исключения при извлечении из пустого стека"""
        stack = Stack()
        
        with pytest.raises(IndexError, match="pop from empty stack"):
            stack.pop()
    
    def test_peek_empty_stack_raises_exception(self):
        """Тест исключения при просмотре пустого стека"""
        stack = Stack()
        
        with pytest.raises(IndexError, match="peek from empty stack"):
            stack.peek()
    
    def test_stack_with_different_data_types(self):
        """Тест стека с различными типами данных"""
        stack = Stack()
        
        stack.push(1)
        stack.push("hello")
        stack.push([1, 2, 3])
        stack.push({"key": "value"})
        
        assert stack.pop() == {"key": "value"}
        assert stack.pop() == [1, 2, 3]
        assert stack.pop() == "hello"
        assert stack.pop() == 1
    
    def test_stack_with_none_values(self):
        """Тест стека с None значениями"""
        stack = Stack()
        
        stack.push(None)
        stack.push(1)
        stack.push(None)
        
        assert stack.pop() is None
        assert stack.pop() == 1
        assert stack.pop() is None
        assert stack.is_empty()
    
    def test_large_stack(self):
        """Тест с большим количеством элементов"""
        stack = Stack()
        n = 1000
        
        # Добавляем много элементов
        for i in range(n):
            stack.push(i)
        
        assert stack.size() == n
        assert stack.peek() == n - 1
        
        # Извлекаем все
        for i in range(n - 1, -1, -1):
            assert stack.pop() == i
        
        assert stack.is_empty()
    
    def test_string_representation(self):
        """Тест строкового представления стека"""
        stack = Stack()
        
        # Пустой стек
        assert str(stack) == "Stack([])"
        
        # Стек с элементами
        stack.push(1)
        stack.push(2)
        stack.push(3)
        
        assert str(stack) == "Stack([3, 2, 1])"
        assert repr(stack) == str(stack)
    
    def test_stack_independence(self):
        """Тест независимости различных стеков"""
        stack1 = Stack()
        stack2 = Stack()
        
        stack1.push(1)
        stack1.push(2)
        
        stack2.push("a")
        stack2.push("b")
        
        assert stack1.size() == 2
        assert stack2.size() == 2
        assert stack1.peek() == 2
        assert stack2.peek() == "b"
        
        stack1.pop()
        assert stack1.size() == 1
        assert stack2.size() == 2  # Не изменился
