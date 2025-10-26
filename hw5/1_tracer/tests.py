import pytest
from io import StringIO
import sys
from solution import tracer


def test_factorial():
    @tracer
    def factorial(n):
        if n <= 1:
            return 1
        return n * factorial(n - 1)
    
    output = StringIO()
    sys.stdout = output
    result = factorial(3)
    sys.stdout = sys.__stdout__
    
    assert result == 6
    output_str = output.getvalue()
    assert "factorial(3)" in output_str
    assert "factorial(2)" in output_str
    assert "factorial(1)" in output_str
    assert "-> factorial(1) = 1" in output_str
    assert "-> factorial(2) = 2" in output_str
    assert "-> factorial(3) = 6" in output_str


def test_fibonacci():
    @tracer
    def fib(n):
        if n <= 1:
            return n
        return fib(n - 1) + fib(n - 2)
    
    output = StringIO()
    sys.stdout = output
    result = fib(3)
    sys.stdout = sys.__stdout__
    
    assert result == 2
    output_str = output.getvalue()
    assert "fib(3)" in output_str
    assert "fib(2)" in output_str
    assert "fib(1)" in output_str
    assert "fib(0)" in output_str


def test_sum_recursive():
    @tracer
    def sum_list(lst):
        if not lst:
            return 0
        return lst[0] + sum_list(lst[1:])
    
    output = StringIO()
    sys.stdout = output
    result = sum_list([1, 2, 3])
    sys.stdout = sys.__stdout__
    
    assert result == 6
    output_str = output.getvalue()
    assert "sum_list([1, 2, 3])" in output_str
    assert "sum_list([2, 3])" in output_str
    assert "sum_list([3])" in output_str
    assert "sum_list([])" in output_str


def test_indentation():
    @tracer
    def countdown(n):
        if n <= 0:
            return 0
        return countdown(n - 1)
    
    output = StringIO()
    sys.stdout = output
    countdown(3)
    sys.stdout = sys.__stdout__
    
    lines = output.getvalue().split('\n')
    depth_0 = [l for l in lines if l.startswith("countdown") and not l.startswith("|")]
    depth_1 = [l for l in lines if l.startswith("|  countdown") and not l.startswith("|  |")]
    depth_2 = [l for l in lines if l.startswith("|  |  countdown") and not l.startswith("|  |  |")]
    
    assert len(depth_0) > 0
    assert len(depth_1) > 0
    assert len(depth_2) > 0


def test_kwargs():
    @tracer
    def power(base, exp=2):
        if exp == 0:
            return 1
        return base * power(base, exp=exp-1)
    
    output = StringIO()
    sys.stdout = output
    result = power(2, exp=3)
    sys.stdout = sys.__stdout__
    
    assert result == 8
    output_str = output.getvalue()
    assert "power(2, exp=3)" in output_str or "power(2, exp = 3)" in output_str


def test_base_case():
    @tracer
    def identity(x):
        return x
    
    output = StringIO()
    sys.stdout = output
    result = identity(42)
    sys.stdout = sys.__stdout__
    
    assert result == 42
    output_str = output.getvalue()
    assert "identity(42)" in output_str
    assert "-> identity(42) = 42" in output_str

