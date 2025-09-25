import pytest
from solution import count_primes


class TestCountPrimes:
    def test_small_numbers(self):
        """Тест малых чисел"""
        assert count_primes(0) == 0
        assert count_primes(1) == 0
        assert count_primes(2) == 0
        assert count_primes(3) == 1  # только 2
    
    def test_first_primes(self):
        """Тест первых простых чисел"""
        assert count_primes(4) == 2   # 2, 3
        assert count_primes(5) == 2   # 2, 3
        assert count_primes(6) == 3   # 2, 3, 5
        assert count_primes(7) == 3   # 2, 3, 5
        assert count_primes(8) == 4   # 2, 3, 5, 7
    
    def test_ten(self):
        """Тест для n = 10"""
        assert count_primes(10) == 4  # 2, 3, 5, 7
    
    def test_twenty(self):
        """Тест для n = 20"""
        assert count_primes(20) == 8  # 2, 3, 5, 7, 11, 13, 17, 19
    
    def test_thirty(self):
        """Тест для n = 30"""
        assert count_primes(30) == 10  # 2, 3, 5, 7, 11, 13, 17, 19, 23, 29
    
    def test_hundred(self):
        """Тест для n = 100"""
        assert count_primes(100) == 25
    
    def test_large_number(self):
        """Тест для больших чисел"""
        assert count_primes(1000) == 168
    
    def test_negative_numbers(self):
        """Тест отрицательных чисел"""
        assert count_primes(-1) == 0
        assert count_primes(-10) == 0
    
    def test_edge_cases(self):
        """Тест граничных случаев"""
        assert count_primes(11) == 4   # 2, 3, 5, 7, но не 11
        assert count_primes(12) == 5   # 2, 3, 5, 7, 11
        assert count_primes(13) == 5   # 2, 3, 5, 7, 11, но не 13