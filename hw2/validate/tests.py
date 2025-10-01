import pytest
import sys
from pathlib import Path

# Добавляем путь к модулям
sys.path.insert(0, str(Path(__file__).parent))

from solution import validate_stack_sequences


class TestValidateStackSequences:
    """Тесты для функции validate_stack_sequences"""
    
    def test_example_1_from_task(self):
        """Пример 1 из условия задачи: валидная последовательность"""
        pushed = [1, 2, 3, 4, 5]
        popped = [1, 3, 5, 4, 2]
        assert validate_stack_sequences(pushed, popped) is True
    
    def test_example_2_from_task(self):
        """Пример 2 из условия задачи: невалидная последовательность"""
        pushed = [1, 2, 3]
        popped = [3, 1, 2]
        assert validate_stack_sequences(pushed, popped) is False
    
    def test_single_element(self):
        """Один элемент"""
        pushed = [1]
        popped = [1]
        assert validate_stack_sequences(pushed, popped) is True
    
    def test_two_elements_valid(self):
        """Два элемента - валидная последовательность"""
        pushed = [1, 2]
        popped = [2, 1]
        assert validate_stack_sequences(pushed, popped) is True
    
    def test_two_elements_invalid(self):
        """Два элемента - невалидная последовательность"""
        pushed = [1, 2]
        popped = [1, 2]
        assert validate_stack_sequences(pushed, popped) is True
    
    def test_reverse_order(self):
        """Обратный порядок - классический стек (LIFO)"""
        pushed = [1, 2, 3, 4, 5]
        popped = [5, 4, 3, 2, 1]
        assert validate_stack_sequences(pushed, popped) is True
    
    def test_same_order(self):
        """Тот же порядок - выталкиваем сразу после добавления"""
        pushed = [1, 2, 3, 4, 5]
        popped = [1, 2, 3, 4, 5]
        assert validate_stack_sequences(pushed, popped) is True
    
    def test_alternating_pattern(self):
        """Чередующийся паттерн"""
        pushed = [1, 2, 3, 4]
        popped = [2, 1, 4, 3]
        assert validate_stack_sequences(pushed, popped) is True
    
    def test_impossible_sequence_1(self):
        """Невозможная последовательность: нужен элемент не на вершине"""
        pushed = [1, 2, 3, 4]
        popped = [3, 4, 1, 2]
        assert validate_stack_sequences(pushed, popped) is False
    
    def test_impossible_sequence_2(self):
        """Невозможная последовательность"""
        pushed = [1, 2, 3, 4, 5]
        popped = [4, 3, 5, 1, 2]
        assert validate_stack_sequences(pushed, popped) is False
    
    def test_empty_sequences(self):
        """Пустые последовательности"""
        pushed = []
        popped = []
        assert validate_stack_sequences(pushed, popped) is True
    
    def test_different_lengths(self):
        """Разные длины последовательностей"""
        pushed = [1, 2, 3]
        popped = [1, 2]
        assert validate_stack_sequences(pushed, popped) is False
    
    def test_complex_valid_sequence(self):
        """Сложная валидная последовательность"""
        pushed = [1, 2, 3, 4, 5, 6]
        popped = [2, 1, 3, 6, 5, 4]
        assert validate_stack_sequences(pushed, popped) is True
    
    def test_large_sequence(self):
        """Большая последовательность (проверка производительности)"""
        n = 1000
        pushed = list(range(1, n + 1))
        popped = list(range(n, 0, -1))  # Обратный порядок
        assert validate_stack_sequences(pushed, popped) is True
    
    def test_large_sequence_same_order(self):
        """Большая последовательность в том же порядке"""
        n = 1000
        pushed = list(range(1, n + 1))
        popped = list(range(1, n + 1))  # Тот же порядок
        assert validate_stack_sequences(pushed, popped) is True
    
    def test_interleaved_pattern(self):
        """Переплетенный паттерн"""
        pushed = [1, 2, 3, 4, 5, 6, 7, 8]
        popped = [1, 3, 2, 5, 4, 7, 6, 8]
        assert validate_stack_sequences(pushed, popped) is True
    
    def test_invalid_interleaved(self):
        """Невалидный переплетенный паттерн"""
        pushed = [1, 2, 3, 4, 5]
        popped = [2, 1, 5, 3, 4]
        assert validate_stack_sequences(pushed, popped) is False
    
    def test_with_duplicates_note(self):
        """
        Примечание: по условию задачи pushed и popped содержат уникальные числа,
        но проверим поведение с дубликатами на всякий случай
        """
        pushed = [1, 1, 2, 2]
        popped = [1, 2, 1, 2]
        # Ожидается True, так как алгоритм работает и с дубликатами
        assert validate_stack_sequences(pushed, popped) is True
    
    def test_edge_case_max_constraint(self):
        """Граничный случай: максимальная длина по условию"""
        n = 100_000
        pushed = list(range(n))
        popped = list(range(n))
        assert validate_stack_sequences(pushed, popped) is True


class TestStackOperationsTrace:
    """Тесты с трассировкой операций (для понимания алгоритма)"""
    
    def test_trace_example_1(self):
        """
        Трассировка примера 1:
        pushed: [1, 2, 3, 4, 5]
        popped: [1, 3, 5, 4, 2]
        
        Операции:
        push(1) -> стек: [1]
        pop(1)  -> стек: [], popped[0]=1 ✓
        push(2) -> стек: [2]
        push(3) -> стек: [2, 3]
        pop(3)  -> стек: [2], popped[1]=3 ✓
        push(4) -> стек: [2, 4]
        push(5) -> стек: [2, 4, 5]
        pop(5)  -> стек: [2, 4], popped[2]=5 ✓
        pop(4)  -> стек: [2], popped[3]=4 ✓
        pop(2)  -> стек: [], popped[4]=2 ✓
        """
        pushed = [1, 2, 3, 4, 5]
        popped = [1, 3, 5, 4, 2]
        assert validate_stack_sequences(pushed, popped) is True
    
    def test_trace_example_2(self):
        """
        Трассировка примера 2:
        pushed: [1, 2, 3]
        popped: [3, 1, 2]
        
        Операции:
        push(1) -> стек: [1]
        push(2) -> стек: [1, 2]
        push(3) -> стек: [1, 2, 3]
        pop(3)  -> стек: [1, 2], popped[0]=3 ✓
        Нужен pop(1), но на вершине 2 ✗
        """
        pushed = [1, 2, 3]
        popped = [3, 1, 2]
        assert validate_stack_sequences(pushed, popped) is False


if __name__ == "__main__":
    # Запуск тестов с подробным выводом
    pytest.main([__file__, "-v", "--tb=short"])

