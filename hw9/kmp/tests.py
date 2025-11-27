import pytest
from solution import KnuthMorrisPratt, kmp_search, kmp_search_all, compute_lps


class TestKMPBasic:
    """Базовые тесты алгоритма Кнута — Морриса — Пратта."""
    
    def test_empty_pattern(self):
        kmp = KnuthMorrisPratt()
        assert kmp.search("hello", "") == -1
    
    def test_empty_text(self):
        kmp = KnuthMorrisPratt()
        assert kmp.search("", "pattern") == -1
    
    def test_both_empty(self):
        kmp = KnuthMorrisPratt()
        assert kmp.search("", "") == -1
    
    def test_pattern_longer_than_text(self):
        kmp = KnuthMorrisPratt()
        assert kmp.search("hi", "hello") == -1
    
    def test_single_character_match(self):
        kmp = KnuthMorrisPratt()
        assert kmp.search("a", "a") == 0
    
    def test_single_character_no_match(self):
        kmp = KnuthMorrisPratt()
        assert kmp.search("a", "b") == -1
    
    def test_pattern_at_beginning(self):
        kmp = KnuthMorrisPratt()
        assert kmp.search("hello world", "hello") == 0
    
    def test_pattern_at_end(self):
        kmp = KnuthMorrisPratt()
        assert kmp.search("hello world", "world") == 6
    
    def test_pattern_in_middle(self):
        kmp = KnuthMorrisPratt()
        assert kmp.search("abcdefgh", "cde") == 2
    
    def test_pattern_not_found(self):
        kmp = KnuthMorrisPratt()
        assert kmp.search("hello world", "xyz") == -1


class TestKMPRepeating:
    """Тесты с повторяющимися символами и паттернами."""
    
    def test_repeating_characters(self):
        kmp = KnuthMorrisPratt()
        assert kmp.search("aaaaaaa", "aaa") == 0
    
    def test_pattern_with_repeats(self):
        kmp = KnuthMorrisPratt()
        assert kmp.search("abababab", "abab") == 0
    
    def test_overlapping_pattern(self):
        kmp = KnuthMorrisPratt()
        result = kmp.search("aaaa", "aa")
        assert result == 0
    
    def test_text_equals_pattern(self):
        kmp = KnuthMorrisPratt()
        assert kmp.search("pattern", "pattern") == 0
    
    def test_multiple_occurrences_first(self):
        kmp = KnuthMorrisPratt()
        assert kmp.search("abcabcabc", "abc") == 0


class TestKMPSearchAll:
    """Тесты для поиска всех вхождений."""
    
    def test_search_all_single_occurrence(self):
        kmp = KnuthMorrisPratt()
        assert kmp.search_all("hello world", "world") == [6]
    
    def test_search_all_multiple_occurrences(self):
        kmp = KnuthMorrisPratt()
        assert kmp.search_all("abcabcabc", "abc") == [0, 3, 6]
    
    def test_search_all_overlapping(self):
        kmp = KnuthMorrisPratt()
        assert kmp.search_all("aaaa", "aa") == [0, 1, 2]
    
    def test_search_all_no_match(self):
        kmp = KnuthMorrisPratt()
        assert kmp.search_all("hello world", "xyz") == []
    
    def test_search_all_empty_pattern(self):
        kmp = KnuthMorrisPratt()
        assert kmp.search_all("hello", "") == []
    
    def test_search_all_entire_text(self):
        kmp = KnuthMorrisPratt()
        assert kmp.search_all("test", "test") == [0]


class TestKMPSpecialCases:
    """Тесты специальных случаев."""
    
    def test_unicode_characters(self):
        kmp = KnuthMorrisPratt()
        assert kmp.search("привет мир", "мир") == 7
    
    def test_special_characters(self):
        kmp = KnuthMorrisPratt()
        assert kmp.search("hello@world.com", "@world") == 5
    
    def test_numbers_in_string(self):
        kmp = KnuthMorrisPratt()
        assert kmp.search("abc123def456", "123") == 3
    
    def test_whitespace(self):
        kmp = KnuthMorrisPratt()
        assert kmp.search("hello  world", "  ") == 5
    
    def test_newlines(self):
        kmp = KnuthMorrisPratt()
        assert kmp.search("line1\nline2\nline3", "\n") == 5


class TestKMPLongStrings:
    """Тесты с длинными строками."""
    
    def test_long_text_short_pattern(self):
        kmp = KnuthMorrisPratt()
        text = "a" * 1000 + "b" + "a" * 1000
        assert kmp.search(text, "b") == 1000
    
    def test_long_pattern(self):
        kmp = KnuthMorrisPratt()
        pattern = "abc" * 100
        text = "xyz" * 50 + pattern + "xyz" * 50
        assert kmp.search(text, pattern) == 150
    
    def test_no_match_long_string(self):
        kmp = KnuthMorrisPratt()
        text = "a" * 10000
        pattern = "b"
        assert kmp.search(text, pattern) == -1


class TestKMPHelperFunctions:
    """Тесты вспомогательных функций."""
    
    def test_helper_search_found(self):
        assert kmp_search("hello world", "world") == 6
    
    def test_helper_search_not_found(self):
        assert kmp_search("hello world", "xyz") == -1
    
    def test_helper_search_all_found(self):
        assert kmp_search_all("abcabcabc", "abc") == [0, 3, 6]
    
    def test_helper_search_all_not_found(self):
        assert kmp_search_all("hello world", "xyz") == []


class TestKMPEdgeCases:
    """Тесты граничных случаев."""
    
    def test_single_char_text_match(self):
        kmp = KnuthMorrisPratt()
        assert kmp.search("x", "x") == 0
    
    def test_single_char_text_no_match(self):
        kmp = KnuthMorrisPratt()
        assert kmp.search("x", "y") == -1
    
    def test_pattern_at_very_end(self):
        kmp = KnuthMorrisPratt()
        assert kmp.search("abcdefg", "g") == 6
    
    def test_full_match(self):
        kmp = KnuthMorrisPratt()
        text = "exactly"
        assert kmp.search(text, text) == 0
    
    def test_almost_match(self):
        kmp = KnuthMorrisPratt()
        assert kmp.search("abcdef", "abcxef") == -1
    
    def test_case_sensitive(self):
        kmp = KnuthMorrisPratt()
        assert kmp.search("Hello World", "hello") == -1
        assert kmp.search("Hello World", "Hello") == 0


class TestKMPLPSFunction:
    """Тесты префикс-функции (LPS array)."""
    
    def test_lps_simple(self):
        assert compute_lps("ababaca") == [0, 0, 1, 2, 3, 0, 1]
    
    def test_lps_no_prefix_suffix(self):
        assert compute_lps("abcdef") == [0, 0, 0, 0, 0, 0]
    
    def test_lps_all_same(self):
        assert compute_lps("aaaa") == [0, 1, 2, 3]
    
    def test_lps_repeated_pattern(self):
        assert compute_lps("abacaba") == [0, 0, 1, 0, 1, 2, 3]
    
    def test_lps_single_char(self):
        assert compute_lps("a") == [0]
    
    def test_lps_two_chars_same(self):
        assert compute_lps("aa") == [0, 1]
    
    def test_lps_two_chars_different(self):
        assert compute_lps("ab") == [0, 0]
    
    def test_lps_complex_pattern(self):
        assert compute_lps("ababcababa") == [0, 0, 1, 2, 0, 1, 2, 3, 4, 3]


class TestKMPMultipleSearches:
    """Тесты множественных поисков с одним экземпляром."""
    
    def test_reuse_instance(self):
        kmp = KnuthMorrisPratt()
        assert kmp.search("first text", "text") == 6
        assert kmp.search("second search", "search") == 7
        assert kmp.search("third time", "time") == 6
    
    def test_different_patterns_same_text(self):
        kmp = KnuthMorrisPratt()
        text = "the quick brown fox jumps over the lazy dog"
        assert kmp.search(text, "quick") == 4
        assert kmp.search(text, "fox") == 16
        assert kmp.search(text, "dog") == 40


class TestKMPConsistencyWithBuiltin:
    """Тесты для проверки согласованности со встроенным поиском Python."""
    
    def test_consistency_simple(self):
        kmp = KnuthMorrisPratt()
        text = "hello world"
        pattern = "world"
        assert kmp.search(text, pattern) == text.find(pattern)
    
    def test_consistency_not_found(self):
        kmp = KnuthMorrisPratt()
        text = "hello world"
        pattern = "xyz"
        assert kmp.search(text, pattern) == text.find(pattern)
    
    def test_consistency_multiple_texts(self):
        kmp = KnuthMorrisPratt()
        test_cases = [
            ("abcdefgh", "cde"),
            ("python programming", "prog"),
            ("test string", "string"),
            ("no match here", "xyz"),
        ]
        for text, pattern in test_cases:
            assert kmp.search(text, pattern) == text.find(pattern)


class TestKMPComplexPatterns:
    """Тесты со сложными паттернами."""
    
    def test_pattern_with_spaces(self):
        kmp = KnuthMorrisPratt()
        assert kmp.search("hello world hello", "o w") == 4
    
    def test_pattern_with_punctuation(self):
        kmp = KnuthMorrisPratt()
        assert kmp.search("Hello, world!", ", world") == 5
    
    def test_mixed_content(self):
        kmp = KnuthMorrisPratt()
        text = "User123@email.com visited page at 10:30"
        assert kmp.search(text, "@email") == 7
        assert kmp.search(text, "10:30") == 34
    
    def test_url_pattern(self):
        kmp = KnuthMorrisPratt()
        text = "Visit https://example.com for more info"
        assert kmp.search(text, "://") == 11
    
    def test_repeated_substrings(self):
        kmp = KnuthMorrisPratt()
        text = "ababababab"
        results = kmp.search_all(text, "aba")
        assert results == [0, 2, 4, 6]


class TestKMPAdvancedPatterns:
    """Тесты для продвинутых паттернов, где КМП показывает преимущества."""
    
    def test_worst_case_naive(self):
        """Случай, где наивный алгоритм работает плохо, а КМП - эффективно."""
        kmp = KnuthMorrisPratt()
        text = "a" * 1000 + "b"
        pattern = "a" * 10 + "b"
        assert kmp.search(text, pattern) == 990
    
    def test_partial_matches(self):
        """Много частичных совпадений перед полным."""
        kmp = KnuthMorrisPratt()
        text = "ababababababababc"
        pattern = "ababc"
        assert kmp.search(text, pattern) == 12
    
    def test_self_similar_pattern(self):
        """Паттерн с повторяющейся структурой."""
        kmp = KnuthMorrisPratt()
        text = "abcabcabcabcabcabd"
        pattern = "abcabd"
        assert kmp.search(text, pattern) == 12


class TestKMPGetLPS:
    """Тесты для метода get_lps."""
    
    def test_get_lps_after_search(self):
        kmp = KnuthMorrisPratt()
        kmp.search("hello world", "world")
        lps = kmp.get_lps()
        assert lps == [0, 0, 0, 0, 0]
    
    def test_get_lps_before_search(self):
        kmp = KnuthMorrisPratt()
        assert kmp.get_lps() is None
    
    def test_get_lps_complex_pattern(self):
        kmp = KnuthMorrisPratt()
        kmp.search("xabacabax", "abacaba")
        lps = kmp.get_lps()
        assert lps == [0, 0, 1, 0, 1, 2, 3]

