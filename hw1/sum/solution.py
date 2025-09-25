def max_even_sum(numbers: list[int]) -> int:
    """
    Находит максимальную четную сумму элементов массива.
    
    Args:
        numbers: массив целых положительных чисел
        
    Returns:
        максимальная четная сумма элементов массива
    """
    if not numbers:
        return 0
    
    ans = 0
    min_odd = float('inf')
    for i in range(len(numbers)):
        ans += numbers[i]
        if numbers[i] % 2 == 1:
            min_odd = min(min_odd, numbers[i])

    if ans % 2 == 0:
        return ans

    return ans - min_odd
