"""
Алгоритм Рабина-Карпа для поиска подстроки в строке.

Rolling Hash (скользящий хэш):
    Техника, позволяющая пересчитывать хэш для сдвигаемого окна данных за O(1).
    При сдвиге окна вправо:
    - Вычитаем вклад символа, покидающего окно слева
    - Добавляем вклад нового символа, входящего справа
    Используется полиномиальный хэш: hash = (c[0] * base^(m-1) + c[1] * base^(m-2) + ... + c[m-1]) % mod
    
Оценка сложности:
    Среднее время: O(N + M), где N - длина текста, M - длина образца.
        - O(M) на вычисление хэша образца
        - O(M) на вычисление хэша первого окна
        - O(N - M) на обновление хэша при сдвиге окна (каждое обновление за O(1))
    Худшее время: O(N * M) при большом количестве коллизий хэшей,
        когда требуется много посимвольных проверок.
"""


class RabinKarp:
    """Класс для поиска подстроки в строке алгоритмом Рабина-Карпа."""
    
    def __init__(self, base=256, mod=10**9 + 7):
        """
        Инициализация параметров хэш-функции.
        
        Args:
            base: Основание для полиномиального хэша (обычно размер алфавита)
            mod: Модуль для предотвращения переполнения
        """
        self.base = base
        self.mod = mod
    
    def _hash(self, s):
        """
        Вычисляет полиномиальный хэш строки.
        
        Args:
            s: Строка для хэширования
            
        Returns:
            Хэш-значение строки
        """
        h = 0
        for char in s:
            h = (h * self.base + ord(char)) % self.mod
        return h
    
    def _recalculate_hash(self, old_hash, old_char, new_char, h):
        """
        Пересчитывает хэш при сдвиге окна (rolling hash).
        
        Args:
            old_hash: Текущий хэш окна
            old_char: Символ, покидающий окно слева
            new_char: Символ, входящий в окно справа
            h: Предвычисленное значение base^(pattern_len-1) % mod
            
        Returns:
            Новый хэш окна
        """
        # Удаляем вклад старого символа (добавляем mod для гарантии положительного результата)
        new_hash = (old_hash - ord(old_char) * h + self.mod) % self.mod
        
        # Сдвигаем и добавляем новый символ
        new_hash = (new_hash * self.base + ord(new_char)) % self.mod
        
        return new_hash
    
    def _search_generator(self, text, pattern):
        """
        Генератор, находящий все индексы вхождений подстроки.
        
        Args:
            text: Текст для поиска
            pattern: Искомый образец (подстрока)
            
        Yields:
            Индексы вхождений подстроки
        """
        if not pattern or not text:
            return
        
        n = len(text)
        m = len(pattern)
        
        if m > n:
            return
        
        # Предварительно вычисляем h = base^(m-1) % mod (критично для производительности!)
        h = pow(self.base, m - 1, self.mod)
        
        # Вычисляем хэш образца
        pattern_hash = self._hash(pattern)
        
        # Вычисляем хэш первого окна текста
        window_hash = self._hash(text[:m])
        
        # Проверяем первое окно
        if window_hash == pattern_hash and text[:m] == pattern:
            yield 0
        
        # Сдвигаем окно по тексту
        for i in range(1, n - m + 1):
            # Обновляем хэш с помощью rolling hash
            window_hash = self._recalculate_hash(
                window_hash,
                text[i - 1],
                text[i + m - 1],
                h
            )
            
            # При совпадении хэшей проверяем строки посимвольно
            if window_hash == pattern_hash and text[i:i + m] == pattern:
                yield i
    
    def search(self, text, pattern):
        """
        Ищет первое вхождение подстроки в строке.
        
        Args:
            text: Текст для поиска
            pattern: Искомый образец (подстрока)
            
        Returns:
            Индекс первого вхождения или -1, если не найдено
        """
        try:
            return next(self._search_generator(text, pattern))
        except StopIteration:
            return -1
    
    def search_all(self, text, pattern):
        """
        Ищет все вхождения подстроки в строке.
        
        Args:
            text: Текст для поиска
            pattern: Искомый образец (подстрока)
            
        Returns:
            Список индексов всех вхождений
        """
        return list(self._search_generator(text, pattern))


def rabin_karp_search(text, pattern):
    """
    Вспомогательная функция для поиска первого вхождения подстроки.
    
    Args:
        text: Текст для поиска
        pattern: Искомый образец (подстрока)
        
    Returns:
        Индекс первого вхождения или -1, если не найдено
    """
    rk = RabinKarp()
    return rk.search(text, pattern)


def rabin_karp_search_all(text, pattern):
    """
    Вспомогательная функция для поиска всех вхождений подстроки.
    
    Args:
        text: Текст для поиска
        pattern: Искомый образец (подстрока)
        
    Returns:
        Список индексов всех вхождений
    """
    rk = RabinKarp()
    return rk.search_all(text, pattern)

