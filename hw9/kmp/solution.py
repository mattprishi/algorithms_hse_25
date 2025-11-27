"""
Алгоритм Кнута — Морриса — Пратта (KMP) для поиска подстроки в строке.

Основная идея:
    При несовпадении символов алгоритм не сдвигает подстроку на 1 позицию назад,
    а использует предварительно вычисленную префикс-функцию для "умного" перескока.
    Это позволяет избежать повторных проверок уже просмотренных символов текста.

Префикс-функция (LPS - Longest Proper Prefix which is also Suffix):
    Для каждой позиции i в pattern, π[i] хранит длину самого длинного собственного
    префикса pattern[0...i], который также является его суффиксом.
    
    Пример: для pattern = "abacaba"
    π = [0, 0, 1, 0, 1, 2, 3]
    π[6] = 3, потому что у "abacaba" самый длинный собственный префикс,
    являющийся суффиксом, — это "aba" (длина 3).

Оценка сложности:
    Время: O(N + M)
        - O(M) на вычисление префикс-функции, где M - длина pattern
        - O(N) на поиск в тексте, где N - длина text
        Итоговая сложность линейна относительно суммы длин.
    
    Память: O(M)
        - Требуется массив префикс-функции размером M
"""


class KnuthMorrisPratt:
    """Класс для поиска подстроки в строке алгоритмом Кнута — Морриса — Пратта."""
    
    def __init__(self):
        """Инициализация класса KMP."""
        self.lps = None
    
    def _compute_lps(self, pattern):
        """
        Вычисляет префикс-функцию (LPS array) для pattern.
        
        LPS[i] = длина самого длинного собственного префикса pattern[0..i],
        который также является суффиксом.
        
        Args:
            pattern: Строка, для которой вычисляется префикс-функция
            
        Returns:
            Массив префикс-функции
        """
        m = len(pattern)
        lps = [0] * m
        length = 0  # Длина предыдущего самого длинного префикса-суффикса
        i = 1
        
        while i < m:
            if pattern[i] == pattern[length]:
                # Символы совпали - увеличиваем длину
                length += 1
                lps[i] = length
                i += 1
            else:
                # Символы не совпали
                if length != 0:
                    # Пробуем более короткий префикс-суффикс
                    length = lps[length - 1]
                else:
                    # Нет совпадающего префикса
                    lps[i] = 0
                    i += 1
        
        return lps
    
    def search(self, text, pattern):
        """
        Ищет первое вхождение подстроки в строке.
        
        Args:
            text: Текст для поиска
            pattern: Искомый образец (подстрока)
            
        Returns:
            Индекс первого вхождения или -1, если не найдено
        """
        if not pattern or not text:
            return -1
        
        n = len(text)
        m = len(pattern)
        
        if m > n:
            return -1
        
        # Вычисляем префикс-функцию для pattern
        self.lps = self._compute_lps(pattern)
        
        i = 0  # Индекс для text
        j = 0  # Индекс для pattern
        
        while i < n:
            if text[i] == pattern[j]:
                # Символы совпали - двигаемся дальше
                i += 1
                j += 1
                
                if j == m:
                    # Нашли полное совпадение
                    return i - j
            else:
                # Символы не совпали
                if j != 0:
                    # Используем префикс-функцию для "умного" сдвига
                    j = self.lps[j - 1]
                else:
                    # Сдвигаем только указатель текста
                    i += 1
        
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
        if not pattern or not text:
            return []
        
        n = len(text)
        m = len(pattern)
        
        if m > n:
            return []
        
        result = []
        
        # Вычисляем префикс-функцию для pattern
        self.lps = self._compute_lps(pattern)
        
        i = 0  # Индекс для text
        j = 0  # Индекс для pattern
        
        while i < n:
            if text[i] == pattern[j]:
                # Символы совпали - двигаемся дальше
                i += 1
                j += 1
                
                if j == m:
                    # Нашли полное совпадение
                    result.append(i - j)
                    # Продолжаем поиск с использованием префикс-функции
                    j = self.lps[j - 1]
            else:
                # Символы не совпали
                if j != 0:
                    # Используем префикс-функцию для "умного" сдвига
                    j = self.lps[j - 1]
                else:
                    # Сдвигаем только указатель текста
                    i += 1
        
        return result
    
    def get_lps(self):
        """
        Возвращает последнюю вычисленную префикс-функцию.
        
        Returns:
            Массив префикс-функции или None
        """
        return self.lps


def kmp_search(text, pattern):
    """
    Вспомогательная функция для поиска первого вхождения подстроки.
    
    Args:
        text: Текст для поиска
        pattern: Искомый образец (подстрока)
        
    Returns:
        Индекс первого вхождения или -1, если не найдено
    """
    kmp = KnuthMorrisPratt()
    return kmp.search(text, pattern)


def kmp_search_all(text, pattern):
    """
    Вспомогательная функция для поиска всех вхождений подстроки.
    
    Args:
        text: Текст для поиска
        pattern: Искомый образец (подстрока)
        
    Returns:
        Список индексов всех вхождений
    """
    kmp = KnuthMorrisPratt()
    return kmp.search_all(text, pattern)


def compute_lps(pattern):
    """
    Вспомогательная функция для вычисления префикс-функции.
    
    Args:
        pattern: Строка для вычисления префикс-функции
        
    Returns:
        Массив префикс-функции
    """
    kmp = KnuthMorrisPratt()
    return kmp._compute_lps(pattern)

