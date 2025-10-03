import pytest
from .solution import two_sum


class TestTwoSum:
    """Тесты для функции two_sum"""
    
    def test_example_1(self):
        """Тест из примера 1"""
        arr = [1, 3, 4, 10]
        k = 7
        result = two_sum(arr, k)
        assert result == (1, 2), f"Ожидалось (1, 2), получено {result}"
        assert arr[result[0]] + arr[result[1]] == k
    
    def test_example_2(self):
        """Тест из примера 2"""
        arr = [5, 5, 1, 4]
        k = 10
        result = two_sum(arr, k)
        assert result == (0, 1), f"Ожидалось (0, 1), получено {result}"
        assert arr[result[0]] + arr[result[1]] == k
    
    def test_two_elements(self):
        """Массив из двух элементов"""
        arr = [2, 7]
        k = 9
        result = two_sum(arr, k)
        assert result == (0, 1)
        assert arr[result[0]] + arr[result[1]] == k
    
    def test_negative_numbers(self):
        """Массив с отрицательными числами"""
        arr = [-1, -2, -3, 5, 7]
        k = 4
        result = two_sum(arr, k)
        assert arr[result[0]] + arr[result[1]] == k
        assert result[0] < result[1]
    
    def test_zero_sum(self):
        """Сумма равна нулю"""
        arr = [3, -3, 5, 1]
        k = 0
        result = two_sum(arr, k)
        assert arr[result[0]] + arr[result[1]] == k
        assert result[0] < result[1]
    
    def test_large_numbers(self):
        """Большие числа"""
        arr = [1000000, 2, 3, 999999]
        k = 1999999
        result = two_sum(arr, k)
        assert arr[result[0]] + arr[result[1]] == k
        assert result[0] < result[1]
    
    def test_elements_at_ends(self):
        """Элементы в начале и в конце массива"""
        arr = [10, 2, 3, 4, 20]
        k = 30
        result = two_sum(arr, k)
        assert result == (0, 4)
        assert arr[result[0]] + arr[result[1]] == k
    
    def test_consecutive_elements(self):
        """Соседние элементы"""
        arr = [1, 2, 3, 4, 5]
        k = 5
        result = two_sum(arr, k)
        assert arr[result[0]] + arr[result[1]] == k
        assert result[0] < result[1]
    
    def test_duplicate_values(self):
        """Массив с повторяющимися значениями"""
        arr = [3, 3, 1, 2, 3]
        k = 6
        result = two_sum(arr, k)
        assert arr[result[0]] + arr[result[1]] == k
        assert result[0] < result[1]
    
    def test_result_order(self):
        """Проверка, что результат возвращается в порядке возрастания индексов"""
        arr = [4, 5, 6, 7]
        k = 11
        result = two_sum(arr, k)
        assert result[0] < result[1], "Индексы должны быть в порядке возрастания"
        assert arr[result[0]] + arr[result[1]] == k

