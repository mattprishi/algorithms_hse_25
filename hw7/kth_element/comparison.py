import time
import random
from solution_1 import find_kth_largest as find_kth_custom
from solution_2 import find_kth_largest as find_kth_heapq


def benchmark(func, nums, k, name):
    start = time.perf_counter()
    result = func(nums.copy(), k)
    elapsed = time.perf_counter() - start
    return result, elapsed


def compare_performance():
    print("=" * 80)
    print("Сравнение производительности двух реализаций поиска k-го максимального элемента")
    print("=" * 80)
    print("Solution 1: Собственная реализация MinHeap")
    print("Solution 2: Встроенная библиотека heapq")
    print("=" * 80)
    
    test_cases = [
        ("Малый массив (n=100, k=10)", 100, 10),
        ("Средний массив (n=1000, k=100)", 1000, 100),
        ("Большой массив (n=5000, k=500)", 5000, 500),
        ("Очень большой массив (n=10000, k=1000)", 10000, 1000),
    ]
    
    random.seed(42)
    
    for name, size, k in test_cases:
        nums = [random.randint(-10000, 10000) for _ in range(size)]
        
        result1, time1 = benchmark(find_kth_custom, nums, k, "Custom")
        result2, time2 = benchmark(find_kth_heapq, nums, k, "Heapq")
        
        speedup = time1 / time2 if time2 > 0 else float('inf')
        
        print(f"\n{name}")
        print(f"  Собственная реализация: {time1:.6f}s")
        print(f"  heapq библиотека:       {time2:.6f}s")
        print(f"  Ускорение heapq:        {speedup:.2f}x")
        
        assert result1 == result2, f"Результаты не совпадают: {result1} != {result2}"
    
    print("\n" + "=" * 80)
    print("Тестирование при различных значениях k")
    print("=" * 80)
    
    size = 5000
    k_values = [1, 10, 100, 1000, 2500, 4999]
    nums = [random.randint(-10000, 10000) for _ in range(size)]
    
    for k in k_values:
        result1, time1 = benchmark(find_kth_custom, nums, k, "Custom")
        result2, time2 = benchmark(find_kth_heapq, nums, k, "Heapq")
        
        speedup = time1 / time2 if time2 > 0 else float('inf')
        
        print(f"\nk = {k:4d} (из {size})")
        print(f"  Собственная: {time1:.6f}s")
        print(f"  heapq:       {time2:.6f}s")
        print(f"  Ускорение:   {speedup:.2f}x")
        
        assert result1 == result2
    
    print("\n" + "=" * 80)
    print("Все тесты пройдены успешно!")
    print("=" * 80)


if __name__ == "__main__":
    compare_performance()

