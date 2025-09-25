def is_palindrome(n: int) -> bool:
    """
    Проверяет, является ли целое положительное число палиндромом.
    
    Args:
        n: целое положительное число
        
    Returns:
        True если число является палиндромом, False иначе
    """
    if n < 0:
        return False
    
    if n < 10:
        return True

    original = n
    reversed_num = 0
    
    while n > 0:
        reversed_num = reversed_num * 10 + n % 10
        n //= 10
    
    return original == reversed_num