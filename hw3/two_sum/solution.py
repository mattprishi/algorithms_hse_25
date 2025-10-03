def two_sum(arr, k):
    """
    Находит индексы двух элементов массива, сумма которых равна k.
    
    Args:
        arr: список целых чисел
        k: целевая сумма
    
    Returns:
        tuple: индексы двух элементов в порядке возрастания
    
    Example:
        >>> two_sum([1, 3, 4, 10], 7)
        (1, 2)
        >>> two_sum([5, 5, 1, 4], 10)
        (0, 1)
    """

    seen = {}
    
    for i, num in enumerate(arr):

        complement = k - num
        if complement in seen:
            return seen[complement], i
        
        seen[num] = i
    
    # По условию задачи такая пара всегда есть
    return None

