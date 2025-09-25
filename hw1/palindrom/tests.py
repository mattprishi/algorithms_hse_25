import pytest
from solution import is_palindrome


class TestIsPalindrome:
    def test_single_digit(self):
        """Тест однозначных чисел"""
        assert is_palindrome(0) == True
        assert is_palindrome(5) == True
        assert is_palindrome(9) == True
    
    def test_two_digit_palindrome(self):
        """Тест двузначных палиндромов"""
        assert is_palindrome(11) == True
        assert is_palindrome(22) == True
        assert is_palindrome(99) == True
    
    def test_two_digit_non_palindrome(self):
        """Тест двузначных не палиндромов"""
        assert is_palindrome(12) == False
        assert is_palindrome(23) == False
        assert is_palindrome(98) == False
    
    def test_multi_digit_palindrome(self):
        """Тест многозначных палиндромов"""
        assert is_palindrome(121) == True
        assert is_palindrome(1221) == True
        assert is_palindrome(12321) == True
        assert is_palindrome(123454321) == True
    
    def test_multi_digit_non_palindrome(self):
        """Тест многозначных не палиндромов"""
        assert is_palindrome(123) == False
        assert is_palindrome(1234) == False
        assert is_palindrome(12345) == False
    
    def test_negative_numbers(self):
        """Тест отрицательных чисел"""
        assert is_palindrome(-1) == False
        assert is_palindrome(-121) == False
    
    def test_large_palindromes(self):
        """Тест больших палиндромов"""
        assert is_palindrome(1234567890987654321) == True
        assert is_palindrome(1234567890123456789) == False