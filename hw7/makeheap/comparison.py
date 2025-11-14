import random
import time
from solution import makeheap_n_log_n, makeheap, timer


@timer
def timed_makeheap_n_log_n(arr):
    return makeheap_n_log_n(arr)


@timer
def timed_makeheap(arr):
    return makeheap(arr)


def compare_performance(sizes):
    print("=" * 80)
    print("Сравнение производительности makeheap_n_log_n (O(N log N)) vs makeheap (O(N))")
    print("=" * 80)
    
    for size in sizes:
        arr = list(range(size, 0, -1))
        
        result_nlogn, time_nlogn = timed_makeheap_n_log_n(arr.copy())
        result_n, time_n = timed_makeheap(arr.copy())
        
        ratio = time_nlogn / time_n if time_n > 0 else float('inf')
        
        print(f"\nРазмер массива: {size:,}")
        print(f"  makeheap_n_log_n (O(N log N)): {time_nlogn:.6f}s")
        print(f"  makeheap (O(N)):                {time_n:.6f}s")
        print(f"  Разница во времени:             {ratio:.2f}x")
    
    print("\n" + "=" * 80)
    print("Тестирование на случайных данных")
    print("=" * 80)
    
    random.seed(42)
    for size in sizes:
        arr = [random.randint(-10000, 10000) for _ in range(size)]
        
        result_nlogn, time_nlogn = timed_makeheap_n_log_n(arr.copy())
        result_n, time_n = timed_makeheap(arr.copy())
        
        ratio = time_nlogn / time_n if time_n > 0 else float('inf')
        
        print(f"\nРазмер массива: {size:,}")
        print(f"  makeheap_n_log_n (O(N log N)): {time_nlogn:.6f}s")
        print(f"  makeheap (O(N)):                {time_n:.6f}s")
        print(f"  Разница во времени:             {ratio:.2f}x")


if __name__ == "__main__":
    sizes = [100, 500, 1000, 5000, 10000, 20000]
    compare_performance(sizes)

