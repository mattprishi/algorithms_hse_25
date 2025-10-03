from typing import List
from collections import defaultdict


def group_anagrams(strs: List[str]) -> List[List[str]]:
    """
    Группирует слова так, чтобы в одной группе оказались все анаграммы.
    
    Анаграммы - это слова, состоящие из одних и тех же букв.
    
    Args:
        strs: список слов
        
    Returns:
        список групп анаграмм
        
    Examples:
        >>> group_anagrams(["eat","tea","tan","ate","nat","bat"])
        [["eat","tea","ate"],["tan","nat"],["bat"]]
    """

    anagram_groups = defaultdict(list)
    
    for word in strs:
        # tuple нужен, т.к. list не может быть ключом словаря
        key = tuple(sorted(word))
        anagram_groups[key].append(word)
    
    return list(anagram_groups.values())

