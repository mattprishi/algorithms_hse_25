import pytest
from solution import group_anagrams


def test_basic_example():
    """Тест из примера задачи"""
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result = group_anagrams(strs)
    
    # Преобразуем результат в множество множеств для сравнения
    # (порядок групп и слов внутри групп не важен)
    result_sets = {frozenset(group) for group in result}
    expected_sets = {
        frozenset(["eat", "tea", "ate"]),
        frozenset(["tan", "nat"]),
        frozenset(["bat"])
    }
    
    assert result_sets == expected_sets


def test_empty_list():
    """Тест пустого списка"""
    assert group_anagrams([]) == []


def test_single_word():
    """Тест одного слова"""
    result = group_anagrams(["hello"])
    assert len(result) == 1
    assert result[0] == ["hello"]


def test_no_anagrams():
    """Тест без анаграмм - все слова уникальны"""
    strs = ["abc", "def", "ghi"]
    result = group_anagrams(strs)
    
    assert len(result) == 3
    result_sets = {frozenset(group) for group in result}
    expected_sets = {frozenset(["abc"]), frozenset(["def"]), frozenset(["ghi"])}
    assert result_sets == expected_sets


def test_all_anagrams():
    """Тест когда все слова - анаграммы друг друга"""
    strs = ["abc", "bca", "cab", "acb"]
    result = group_anagrams(strs)
    
    assert len(result) == 1
    assert set(result[0]) == set(strs)


def test_empty_strings():
    """Тест с пустыми строками"""
    strs = ["", "", "a"]
    result = group_anagrams(strs)
    
    result_sets = {frozenset(group) for group in result}
    expected_sets = {frozenset([""]), frozenset(["a"])}
    
    # Учитываем, что две пустые строки должны быть в одной группе
    assert len(result) == 2
    
    # Проверяем, что есть группа с двумя пустыми строками
    empty_groups = [group for group in result if "" in group]
    assert len(empty_groups) == 1
    assert len(empty_groups[0]) == 2


def test_case_sensitive():
    """Тест чувствительности к регистру"""
    strs = ["aEt", "tEa", "tea"]
    result = group_anagrams(strs)
    
    # "aEt" и "tEa" - анаграммы (содержат E, a, t)
    # "tea" - отдельная группа (содержит t, e, a)
    assert len(result) == 2
    
    result_sets = {frozenset(group) for group in result}
    expected_sets = {frozenset(["aEt", "tEa"]), frozenset(["tea"])}
    assert result_sets == expected_sets


def test_single_letter_words():
    """Тест односимвольных слов"""
    strs = ["a", "b", "a", "c", "b"]
    result = group_anagrams(strs)
    
    result_sets = {frozenset(group) for group in result}
    
    # Проверяем количество групп
    assert len(result) == 3
    
    # Проверяем наличие правильных групп
    a_groups = [group for group in result if "a" in group]
    assert len(a_groups) == 1
    assert len(a_groups[0]) == 2  # две буквы "a"


def test_long_anagrams():
    """Тест длинных анаграмм"""
    strs = ["listen", "silent", "enlist", "hello", "world"]
    result = group_anagrams(strs)
    
    assert len(result) == 3
    
    result_sets = {frozenset(group) for group in result}
    expected_sets = {
        frozenset(["listen", "silent", "enlist"]),
        frozenset(["hello"]),
        frozenset(["world"])
    }
    assert result_sets == expected_sets

