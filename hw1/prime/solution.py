def count_primes(n: int) -> int:
    """
    Находит количество простых чисел меньше n, используя решето Эратосфена.
    
    Args:
        n: целое число
        
    Returns:
        количество простых чисел < n
    """
    if n <= 2:
        return 0

    is_prime = [True] * n
    is_prime[0] = False
    is_prime[1] = False
    
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n, i):
                is_prime[j] = False

    return sum(is_prime)