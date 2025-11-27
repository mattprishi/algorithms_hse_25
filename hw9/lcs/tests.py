import pytest
from .solution import LongestCommonSubsequence, lcs, lcs_length


class TestLCSBasic:
    """Базовые тесты алгоритма LCS."""
    
    def test_example_from_task(self):
        """Тест из условия задачи."""
        solver = LongestCommonSubsequence()
        result = solver.find("AGGTAB", "GXTXAYB")
        assert result == "GTAB"
    
    def test_empty_strings_both(self):
        solver = LongestCommonSubsequence()
        assert solver.find("", "") == ""
    
    def test_empty_string_first(self):
        solver = LongestCommonSubsequence()
        assert solver.find("", "ABC") == ""
    
    def test_empty_string_second(self):
        solver = LongestCommonSubsequence()
        assert solver.find("ABC", "") == ""
    
    def test_identical_strings(self):
        solver = LongestCommonSubsequence()
        assert solver.find("ABCDEF", "ABCDEF") == "ABCDEF"
    
    def test_no_common_subsequence(self):
        solver = LongestCommonSubsequence()
        assert solver.find("ABC", "DEF") == ""
    
    def test_single_character_match(self):
        solver = LongestCommonSubsequence()
        assert solver.find("A", "A") == "A"
    
    def test_single_character_no_match(self):
        solver = LongestCommonSubsequence()
        assert solver.find("A", "B") == ""
    
    def test_one_character_in_common(self):
        solver = LongestCommonSubsequence()
        result = solver.find("ABC", "XBY")
        assert result == "B"


class TestLCSLength:
    """Тесты для метода определения длины LCS."""
    
    def test_length_example(self):
        solver = LongestCommonSubsequence()
        assert solver.length("AGGTAB", "GXTXAYB") == 4
    
    def test_length_empty_strings(self):
        solver = LongestCommonSubsequence()
        assert solver.length("", "") == 0
        assert solver.length("ABC", "") == 0
        assert solver.length("", "ABC") == 0
    
    def test_length_identical(self):
        solver = LongestCommonSubsequence()
        assert solver.length("TEST", "TEST") == 4
    
    def test_length_no_match(self):
        solver = LongestCommonSubsequence()
        assert solver.length("ABC", "XYZ") == 0
    
    def test_length_consistency(self):
        """Проверка, что length и find возвращают согласованные результаты."""
        solver = LongestCommonSubsequence()
        s1, s2 = "ABCDEF", "ACDXEF"
        result = solver.find(s1, s2)
        length = solver.length(s1, s2)
        assert len(result) == length


class TestLCSSimplePatterns:
    """Тесты с простыми паттернами."""
    
    def test_substring_at_beginning(self):
        solver = LongestCommonSubsequence()
        result = solver.find("ABCDEF", "ABXYZ")
        assert result == "AB"
    
    def test_substring_at_end(self):
        solver = LongestCommonSubsequence()
        result = solver.find("XYZDEF", "ABCDEF")
        assert result == "DEF"
    
    def test_alternating_characters(self):
        solver = LongestCommonSubsequence()
        result = solver.find("ABAB", "BABA")
        assert result in ["ABA", "BAB"]  # Может быть несколько правильных ответов
    
    def test_all_characters_in_different_order(self):
        solver = LongestCommonSubsequence()
        result = solver.find("ABC", "CBA")
        # LCS может быть любой из символов длины 1
        assert len(result) == 1 and result in "ABC"
    
    def test_repeated_characters(self):
        solver = LongestCommonSubsequence()
        result = solver.find("AAA", "AAA")
        assert result == "AAA"


class TestLCSComplexPatterns:
    """Тесты со сложными паттернами."""
    
    def test_complex_case_1(self):
        solver = LongestCommonSubsequence()
        result = solver.find("ABCDGH", "AEDFHR")
        assert result == "ADH"
    
    def test_complex_case_2(self):
        solver = LongestCommonSubsequence()
        result = solver.find("XMJYAUZ", "MZJAWXU")
        assert result == "MJAU"
    
    def test_many_common_subsequences(self):
        solver = LongestCommonSubsequence()
        result = solver.find("ABCBDAB", "BDCABA")
        # Одна из возможных LCS длины 4
        assert len(result) == 4
        assert result in ["BCAB", "BCBA", "BDAB"]
    
    def test_dna_sequence(self):
        solver = LongestCommonSubsequence()
        result = solver.find("ACCGGTCGAGTGCGCGGAAGCCGGCCGAA", "GTCGTTCGGAATGCCGTTGCTCTGTAAA")
        # Проверяем только длину для упрощения теста
        assert len(result) == 20
    
    def test_long_repeated_pattern(self):
        solver = LongestCommonSubsequence()
        s1 = "ABCABC" * 10
        s2 = "ABCABC" * 10
        result = solver.find(s1, s2)
        assert result == s1


class TestLCSRepeatingCharacters:
    """Тесты с повторяющимися символами."""
    
    def test_all_same_characters(self):
        solver = LongestCommonSubsequence()
        result = solver.find("AAAA", "AAAA")
        assert result == "AAAA"
    
    def test_different_counts_same_char(self):
        solver = LongestCommonSubsequence()
        result = solver.find("AAA", "AA")
        assert result == "AA"
    
    def test_repeated_with_different(self):
        solver = LongestCommonSubsequence()
        result = solver.find("AAABBB", "ABABAB")
        # LCS длины 4, например "AABB" или "ABBB"
        assert len(result) == 4
    
    def test_interleaved_repeats(self):
        solver = LongestCommonSubsequence()
        result = solver.find("ABABAB", "BABABA")
        assert len(result) == 5


class TestLCSEdgeCases:
    """Тесты граничных случаев."""
    
    def test_one_char_vs_long_string(self):
        solver = LongestCommonSubsequence()
        result = solver.find("A", "XYZABCDEF")
        assert result == "A"
    
    def test_long_string_vs_one_char(self):
        solver = LongestCommonSubsequence()
        result = solver.find("ABCDEFG", "D")
        assert result == "D"
    
    def test_completely_reversed(self):
        solver = LongestCommonSubsequence()
        result = solver.find("ABCDE", "EDCBA")
        # Только один символ может совпасть в правильном порядке
        assert len(result) == 1
    
    def test_one_substring_of_another(self):
        solver = LongestCommonSubsequence()
        result = solver.find("ABCDEF", "CDE")
        assert result == "CDE"
    
    def test_partial_overlap(self):
        solver = LongestCommonSubsequence()
        result = solver.find("ABCDEFG", "DEFGHIJ")
        assert result == "DEFG"


class TestLCSHelperFunctions:
    """Тесты вспомогательных функций."""
    
    def test_helper_lcs_found(self):
        result = lcs("AGGTAB", "GXTXAYB")
        assert result == "GTAB"
    
    def test_helper_lcs_empty(self):
        result = lcs("ABC", "XYZ")
        assert result == ""
    
    def test_helper_lcs_length_found(self):
        result = lcs_length("AGGTAB", "GXTXAYB")
        assert result == 4
    
    def test_helper_lcs_length_zero(self):
        result = lcs_length("ABC", "")
        assert result == 0


class TestLCSSpecialCharacters:
    """Тесты со специальными символами."""
    
    def test_numbers(self):
        solver = LongestCommonSubsequence()
        result = solver.find("123456", "135246")
        assert result in ["1246", "1346", "1356"]  # Все длины 4
    
    def test_mixed_alphanumeric(self):
        solver = LongestCommonSubsequence()
        result = solver.find("A1B2C3", "ABC123")
        # LCS длины 4, например "ABC3" или "A123"
        assert len(result) == 4
    
    def test_special_symbols(self):
        solver = LongestCommonSubsequence()
        result = solver.find("!@#$%", "@$%&*")
        assert result == "@$%"
    
    def test_spaces(self):
        solver = LongestCommonSubsequence()
        result = solver.find("A B C", "A C B")
        assert "A" in result and "C" in result


class TestLCSMultipleSearches:
    """Тесты множественных поисков с одним экземпляром."""
    
    def test_reuse_instance(self):
        solver = LongestCommonSubsequence()
        assert solver.find("ABC", "AC") == "AC"
        assert solver.find("XYZ", "XZ") == "XZ"
        assert solver.find("123", "13") == "13"
    
    def test_alternating_length_and_find(self):
        solver = LongestCommonSubsequence()
        assert solver.length("ABC", "AC") == 2
        assert solver.find("ABC", "AC") == "AC"
        assert solver.length("AGGTAB", "GXTXAYB") == 4
        assert solver.find("AGGTAB", "GXTXAYB") == "GTAB"


class TestLCSLongStrings:
    """Тесты с длинными строками."""
    
    def test_long_identical_strings(self):
        solver = LongestCommonSubsequence()
        s = "ABC" * 100
        result = solver.find(s, s)
        assert result == s
    
    def test_long_no_match(self):
        solver = LongestCommonSubsequence()
        s1 = "A" * 500
        s2 = "B" * 500
        result = solver.find(s1, s2)
        assert result == ""
    
    def test_long_with_pattern(self):
        solver = LongestCommonSubsequence()
        s1 = "ABCDEF" * 50
        s2 = "ACE" * 100
        result = solver.find(s1, s2)
        # LCS должна содержать много повторений "ACE"
        assert len(result) > 100


class TestLCSGetDPTable:
    """Тесты для метода get_dp_table."""
    
    def test_dp_table_after_find(self):
        solver = LongestCommonSubsequence()
        solver.find("ABC", "AC")
        dp = solver.get_dp_table()
        assert dp is not None
        assert len(dp) == 4  # len("ABC") + 1
        assert len(dp[0]) == 3  # len("AC") + 1
    
    def test_dp_table_before_find(self):
        solver = LongestCommonSubsequence()
        assert solver.get_dp_table() is None
    
    def test_dp_table_values(self):
        solver = LongestCommonSubsequence()
        solver.find("AB", "AB")
        dp = solver.get_dp_table()
        # dp[2][2] должно быть 2 (длина LCS "AB")
        assert dp[2][2] == 2


class TestLCSSymmetry:
    """Тесты симметричности (длина LCS не зависит от порядка строк)."""
    
    def test_symmetry_length(self):
        solver = LongestCommonSubsequence()
        l1 = solver.length("ABCDEF", "ACDF")
        l2 = solver.length("ACDF", "ABCDEF")
        assert l1 == l2
    
    def test_symmetry_find(self):
        solver = LongestCommonSubsequence()
        r1 = solver.find("ABC", "AC")
        r2 = solver.find("AC", "ABC")
        assert r1 == r2
    
    def test_symmetry_complex(self):
        solver = LongestCommonSubsequence()
        l1 = solver.length("AGGTAB", "GXTXAYB")
        l2 = solver.length("GXTXAYB", "AGGTAB")
        assert l1 == l2

