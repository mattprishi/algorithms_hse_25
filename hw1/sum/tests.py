import pytest
from solution import max_even_sum

class TestMaxEvenSum:
    def test_empty_array(self):
        """Тест пустого массива"""
        assert max_even_sum([]) == 0
    
    def test_single_even_number(self):
        """Тест одного четного числа"""
        assert max_even_sum([2]) == 2
        assert max_even_sum([4]) == 4
    
    def test_single_odd_number(self):
        """Тест одного нечетного числа"""
        assert max_even_sum([1]) == 0
        assert max_even_sum([3]) == 0
    
    def test_all_even_numbers(self):
        """Тест массива из четных чисел"""
        assert max_even_sum([2, 4, 6]) == 12
        assert max_even_sum([2, 4, 6, 8]) == 20
    
    def test_all_odd_numbers(self):
        """Тест массива из нечетных чисел"""
        assert max_even_sum([1, 3, 5]) == 8  # 1+3+5=9, убираем 1, получаем 8
        assert max_even_sum([1, 3, 5, 7]) == 16  # сумма 16, четная
    
    def test_mixed_numbers_even_sum(self):
        """Тест смешанного массива с четной суммой"""
        assert max_even_sum([1, 2, 3, 4]) == 10  # 1+2+3+4=10
        assert max_even_sum([2, 3, 4, 5]) == 14  # 2+3+4+5=14
    
    def test_mixed_numbers_odd_sum(self):
        """Тест смешанного массива с нечетной суммой"""
        assert max_even_sum([1, 2, 4]) == 6  # 1+2+4=7, убираем 1, получаем 6
        assert max_even_sum([1, 3, 4, 6]) == 14  # 1+3+4+6=14, четная
    
    def test_large_numbers(self):
        """Тест больших чисел"""
        assert max_even_sum([100, 200, 300]) == 600
        assert max_even_sum([101, 201, 301]) == 502  # убираем 101
    
    def test_duplicate_numbers(self):
        """Тест с повторяющимися числами"""
        assert max_even_sum([1, 1, 2, 2]) == 6
        assert max_even_sum([3, 3, 3]) == 6  # убираем одну тройку
