import pytest
from solution import RabinKarp, rabin_karp_search, rabin_karp_search_all


@pytest.fixture
def rk():
    """Фикстура для создания экземпляра RabinKarp."""
    return RabinKarp()


class TestRabinKarpBasic:
    """Базовые тесты алгоритма Рабина-Карпа."""
    
    def test_empty_pattern(self, rk):
        assert rk.search("hello", "") == -1
    
    def test_empty_text(self, rk):
        assert rk.search("", "pattern") == -1
    
    def test_both_empty(self, rk):
        assert rk.search("", "") == -1
    
    def test_pattern_longer_than_text(self, rk):
        assert rk.search("hi", "hello") == -1
    
    def test_single_character_match(self, rk):
        assert rk.search("a", "a") == 0
    
    def test_single_character_no_match(self, rk):
        assert rk.search("a", "b") == -1
    
    def test_pattern_at_beginning(self, rk):
        assert rk.search("hello world", "hello") == 0
    
    def test_pattern_at_end(self, rk):
        assert rk.search("hello world", "world") == 6
    
    def test_pattern_in_middle(self, rk):
        assert rk.search("abcdefgh", "cde") == 2
    
    def test_pattern_not_found(self, rk):
        assert rk.search("hello world", "xyz") == -1


class TestRabinKarpRepeating:
    """Тесты с повторяющимися символами и паттернами."""
    
    def test_repeating_characters(self, rk):
        assert rk.search("aaaaaaa", "aaa") == 0
    
    def test_pattern_with_repeats(self, rk):
        assert rk.search("abababab", "abab") == 0
    
    def test_overlapping_pattern(self, rk):
        result = rk.search("aaaa", "aa")
        assert result == 0
    
    def test_text_equals_pattern(self, rk):
        assert rk.search("pattern", "pattern") == 0
    
    def test_multiple_occurrences_first(self, rk):
        assert rk.search("abcabcabc", "abc") == 0


class TestRabinKarpSearchAll:
    """Тесты для поиска всех вхождений."""
    
    def test_search_all_single_occurrence(self, rk):
        assert rk.search_all("hello world", "world") == [6]
    
    def test_search_all_multiple_occurrences(self, rk):
        assert rk.search_all("abcabcabc", "abc") == [0, 3, 6]
    
    def test_search_all_overlapping(self, rk):
        assert rk.search_all("aaaa", "aa") == [0, 1, 2]
    
    def test_search_all_no_match(self, rk):
        assert rk.search_all("hello world", "xyz") == []
    
    def test_search_all_empty_pattern(self, rk):
        assert rk.search_all("hello", "") == []
    
    def test_search_all_entire_text(self, rk):
        assert rk.search_all("test", "test") == [0]


class TestRabinKarpSpecialCases:
    """Тесты специальных случаев."""
    
    def test_unicode_characters(self, rk):
        assert rk.search("привет мир", "мир") == 7
    
    def test_special_characters(self, rk):
        assert rk.search("hello@world.com", "@world") == 5
    
    def test_numbers_in_string(self, rk):
        assert rk.search("abc123def456", "123") == 3
    
    def test_whitespace(self, rk):
        assert rk.search("hello  world", "  ") == 5
    
    def test_newlines(self, rk):
        assert rk.search("line1\nline2\nline3", "\n") == 5


class TestRabinKarpLongStrings:
    """Тесты с длинными строками."""
    
    def test_long_text_short_pattern(self, rk):
        text = "a" * 1000 + "b" + "a" * 1000
        assert rk.search(text, "b") == 1000
    
    def test_long_pattern(self, rk):
        pattern = "abc" * 100
        text = "xyz" * 50 + pattern + "xyz" * 50
        assert rk.search(text, pattern) == 150
    
    def test_no_match_long_string(self, rk):
        text = "a" * 10000
        pattern = "b"
        assert rk.search(text, pattern) == -1


class TestRabinKarpHelperFunctions:
    """Тесты вспомогательных функций."""
    
    def test_helper_search_found(self):
        assert rabin_karp_search("hello world", "world") == 6
    
    def test_helper_search_not_found(self):
        assert rabin_karp_search("hello world", "xyz") == -1
    
    def test_helper_search_all_found(self):
        assert rabin_karp_search_all("abcabcabc", "abc") == [0, 3, 6]
    
    def test_helper_search_all_not_found(self):
        assert rabin_karp_search_all("hello world", "xyz") == []


class TestRabinKarpEdgeCases:
    """Тесты граничных случаев."""
    
    def test_single_char_text_match(self, rk):
        assert rk.search("x", "x") == 0
    
    def test_single_char_text_no_match(self, rk):
        assert rk.search("x", "y") == -1
    
    def test_pattern_at_very_end(self, rk):
        assert rk.search("abcdefg", "g") == 6
    
    def test_full_match(self, rk):
        text = "exactly"
        assert rk.search(text, text) == 0
    
    def test_almost_match(self, rk):
        assert rk.search("abcdef", "abcxef") == -1
    
    def test_case_sensitive(self, rk):
        assert rk.search("Hello World", "hello") == -1
        assert rk.search("Hello World", "Hello") == 0


class TestRabinKarpHashCollisions:
    """Тесты для проверки обработки коллизий хэшей."""
    
    def test_similar_strings(self, rk):
        assert rk.search("abcdefgh", "xyz") == -1
        assert rk.search("abcdefgh", "def") == 3
    
    def test_anagrams_not_matching(self, rk):
        # Полиномиальный хэш чувствителен к порядку символов,
        # поэтому анаграммы не совпадают
        assert rk.search("listen", "silent") == -1
    
    def test_rotated_pattern(self, rk):
        assert rk.search("abcdef", "cdefab") == -1


class TestRabinKarpDifferentBases:
    """Тесты с различными параметрами хэш-функции."""
    
    def test_small_base(self):
        rk = RabinKarp(base=31)
        assert rk.search("hello world", "world") == 6
    
    def test_large_base(self):
        rk = RabinKarp(base=1009)
        assert rk.search("hello world", "world") == 6
    
    def test_custom_modulo(self):
        rk = RabinKarp(base=256, mod=10**9 + 9)
        assert rk.search("hello world", "world") == 6


class TestRabinKarpMultipleSearches:
    """Тесты множественных поисков с одним экземпляром."""
    
    def test_reuse_instance(self, rk):
        assert rk.search("first text", "text") == 6
        assert rk.search("second search", "search") == 7
        assert rk.search("third time", "time") == 6
    
    def test_different_patterns_same_text(self, rk):
        text = "the quick brown fox jumps over the lazy dog"
        assert rk.search(text, "quick") == 4
        assert rk.search(text, "fox") == 16
        assert rk.search(text, "dog") == 40


class TestRabinKarpConsistencyWithBuiltin:
    """Тесты для проверки согласованности со встроенным поиском Python."""
    
    def test_consistency_simple(self, rk):
        text = "hello world"
        pattern = "world"
        assert rk.search(text, pattern) == text.find(pattern)
    
    def test_consistency_not_found(self, rk):
        text = "hello world"
        pattern = "xyz"
        assert rk.search(text, pattern) == text.find(pattern)
    
    @pytest.mark.parametrize("text,pattern", [
        ("abcdefgh", "cde"),
        ("python programming", "prog"),
        ("test string", "string"),
        ("no match here", "xyz"),
    ])
    def test_consistency_multiple_texts(self, rk, text, pattern):
        assert rk.search(text, pattern) == text.find(pattern)


class TestRabinKarpComplexPatterns:
    """Тесты со сложными паттернами."""
    
    def test_pattern_with_spaces(self, rk):
        assert rk.search("hello world hello", "o w") == 4
    
    def test_pattern_with_punctuation(self, rk):
        assert rk.search("Hello, world!", ", world") == 5
    
    def test_mixed_content(self, rk):
        text = "User123@email.com visited page at 10:30"
        assert rk.search(text, "@email") == 7
        assert rk.search(text, "10:30") == 34
    
    def test_url_pattern(self, rk):
        text = "Visit https://example.com for more info"
        assert rk.search(text, "://") == 11
    
    def test_repeated_substrings(self, rk):
        text = "ababababab"
        results = rk.search_all(text, "aba")
        assert results == [0, 2, 4, 6]

