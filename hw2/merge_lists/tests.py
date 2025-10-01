import pytest
from .solution import (
    Node,
    merge_two_lists_with_dummy,
    merge_two_lists_without_dummy,
    list_to_array,
    array_to_list
)


class TestMergeTwoListsWithDummy:
    """Тесты для функции слияния с фиктивным элементом"""
    
    def test_example_case(self):
        """Тест примера из условия"""
        list1 = array_to_list([1, 2, 4])
        list2 = array_to_list([1, 3, 4])
        result = merge_two_lists_with_dummy(list1, list2)
        assert list_to_array(result) == [1, 1, 2, 3, 4, 4]
    
    def test_both_empty(self):
        """Тест: оба списка пусты"""
        result = merge_two_lists_with_dummy(None, None)
        assert result is None
    
    def test_first_empty(self):
        """Тест: первый список пуст"""
        list2 = array_to_list([1, 2, 3])
        result = merge_two_lists_with_dummy(None, list2)
        assert list_to_array(result) == [1, 2, 3]
    
    def test_second_empty(self):
        """Тест: второй список пуст"""
        list1 = array_to_list([1, 2, 3])
        result = merge_two_lists_with_dummy(list1, None)
        assert list_to_array(result) == [1, 2, 3]
    
    def test_single_elements(self):
        """Тест: списки с одним элементом"""
        list1 = array_to_list([1])
        list2 = array_to_list([2])
        result = merge_two_lists_with_dummy(list1, list2)
        assert list_to_array(result) == [1, 2]
    
    def test_single_elements_reverse(self):
        """Тест: списки с одним элементом в обратном порядке"""
        list1 = array_to_list([2])
        list2 = array_to_list([1])
        result = merge_two_lists_with_dummy(list1, list2)
        assert list_to_array(result) == [1, 2]
    
    def test_different_lengths(self):
        """Тест: списки разной длины"""
        list1 = array_to_list([1, 3, 5, 7, 9])
        list2 = array_to_list([2, 4])
        result = merge_two_lists_with_dummy(list1, list2)
        assert list_to_array(result) == [1, 2, 3, 4, 5, 7, 9]
    
    def test_different_lengths_reverse(self):
        """Тест: списки разной длины (обратный случай)"""
        list1 = array_to_list([2, 4])
        list2 = array_to_list([1, 3, 5, 7, 9])
        result = merge_two_lists_with_dummy(list1, list2)
        assert list_to_array(result) == [1, 2, 3, 4, 5, 7, 9]
    
    def test_no_overlap(self):
        """Тест: списки без пересечений (первый меньше второго)"""
        list1 = array_to_list([1, 2, 3])
        list2 = array_to_list([4, 5, 6])
        result = merge_two_lists_with_dummy(list1, list2)
        assert list_to_array(result) == [1, 2, 3, 4, 5, 6]
    
    def test_no_overlap_reverse(self):
        """Тест: списки без пересечений (второй меньше первого)"""
        list1 = array_to_list([4, 5, 6])
        list2 = array_to_list([1, 2, 3])
        result = merge_two_lists_with_dummy(list1, list2)
        assert list_to_array(result) == [1, 2, 3, 4, 5, 6]
    
    def test_duplicate_values(self):
        """Тест: списки с дублирующимися значениями"""
        list1 = array_to_list([1, 1, 2, 2])
        list2 = array_to_list([1, 2, 3, 3])
        result = merge_two_lists_with_dummy(list1, list2)
        assert list_to_array(result) == [1, 1, 1, 2, 2, 2, 3, 3]
    
    def test_all_same_values(self):
        """Тест: все элементы одинаковые"""
        list1 = array_to_list([1, 1, 1])
        list2 = array_to_list([1, 1, 1])
        result = merge_two_lists_with_dummy(list1, list2)
        assert list_to_array(result) == [1, 1, 1, 1, 1, 1]
    
    def test_negative_values(self):
        """Тест: отрицательные значения"""
        list1 = array_to_list([-3, -1, 0])
        list2 = array_to_list([-2, 1, 2])
        result = merge_two_lists_with_dummy(list1, list2)
        assert list_to_array(result) == [-3, -2, -1, 0, 1, 2]
    
    def test_large_numbers(self):
        """Тест: большие числа"""
        list1 = array_to_list([100, 200, 300])
        list2 = array_to_list([150, 250, 350])
        result = merge_two_lists_with_dummy(list1, list2)
        assert list_to_array(result) == [100, 150, 200, 250, 300, 350]


class TestMergeTwoListsWithoutDummy:
    """Тесты для функции слияния без фиктивного элемента"""
    
    def test_example_case(self):
        """Тест примера из условия"""
        list1 = array_to_list([1, 2, 4])
        list2 = array_to_list([1, 3, 4])
        result = merge_two_lists_without_dummy(list1, list2)
        assert list_to_array(result) == [1, 1, 2, 3, 4, 4]
    
    def test_both_empty(self):
        """Тест: оба списка пусты"""
        result = merge_two_lists_without_dummy(None, None)
        assert result is None
    
    def test_first_empty(self):
        """Тест: первый список пуст"""
        list2 = array_to_list([1, 2, 3])
        result = merge_two_lists_without_dummy(None, list2)
        assert list_to_array(result) == [1, 2, 3]
    
    def test_second_empty(self):
        """Тест: второй список пуст"""
        list1 = array_to_list([1, 2, 3])
        result = merge_two_lists_without_dummy(list1, None)
        assert list_to_array(result) == [1, 2, 3]
    
    def test_single_elements(self):
        """Тест: списки с одним элементом"""
        list1 = array_to_list([1])
        list2 = array_to_list([2])
        result = merge_two_lists_without_dummy(list1, list2)
        assert list_to_array(result) == [1, 2]
    
    def test_single_elements_reverse(self):
        """Тест: списки с одним элементом в обратном порядке"""
        list1 = array_to_list([2])
        list2 = array_to_list([1])
        result = merge_two_lists_without_dummy(list1, list2)
        assert list_to_array(result) == [1, 2]
    
    def test_different_lengths(self):
        """Тест: списки разной длины"""
        list1 = array_to_list([1, 3, 5, 7, 9])
        list2 = array_to_list([2, 4])
        result = merge_two_lists_without_dummy(list1, list2)
        assert list_to_array(result) == [1, 2, 3, 4, 5, 7, 9]
    
    def test_different_lengths_reverse(self):
        """Тест: списки разной длины (обратный случай)"""
        list1 = array_to_list([2, 4])
        list2 = array_to_list([1, 3, 5, 7, 9])
        result = merge_two_lists_without_dummy(list1, list2)
        assert list_to_array(result) == [1, 2, 3, 4, 5, 7, 9]
    
    def test_no_overlap(self):
        """Тест: списки без пересечений (первый меньше второго)"""
        list1 = array_to_list([1, 2, 3])
        list2 = array_to_list([4, 5, 6])
        result = merge_two_lists_without_dummy(list1, list2)
        assert list_to_array(result) == [1, 2, 3, 4, 5, 6]
    
    def test_no_overlap_reverse(self):
        """Тест: списки без пересечений (второй меньше первого)"""
        list1 = array_to_list([4, 5, 6])
        list2 = array_to_list([1, 2, 3])
        result = merge_two_lists_without_dummy(list1, list2)
        assert list_to_array(result) == [1, 2, 3, 4, 5, 6]
    
    def test_duplicate_values(self):
        """Тест: списки с дублирующимися значениями"""
        list1 = array_to_list([1, 1, 2, 2])
        list2 = array_to_list([1, 2, 3, 3])
        result = merge_two_lists_without_dummy(list1, list2)
        assert list_to_array(result) == [1, 1, 1, 2, 2, 2, 3, 3]
    
    def test_all_same_values(self):
        """Тест: все элементы одинаковые"""
        list1 = array_to_list([1, 1, 1])
        list2 = array_to_list([1, 1, 1])
        result = merge_two_lists_without_dummy(list1, list2)
        assert list_to_array(result) == [1, 1, 1, 1, 1, 1]
    
    def test_negative_values(self):
        """Тест: отрицательные значения"""
        list1 = array_to_list([-3, -1, 0])
        list2 = array_to_list([-2, 1, 2])
        result = merge_two_lists_without_dummy(list1, list2)
        assert list_to_array(result) == [-3, -2, -1, 0, 1, 2]
    
    def test_large_numbers(self):
        """Тест: большие числа"""
        list1 = array_to_list([100, 200, 300])
        list2 = array_to_list([150, 250, 350])
        result = merge_two_lists_without_dummy(list1, list2)
        assert list_to_array(result) == [100, 150, 200, 250, 300, 350]


class TestComparisonBothMethods:
    """Тесты для сравнения обоих методов"""
    
    def test_both_methods_same_result_1(self):
        """Тест: оба метода дают одинаковый результат на примере 1"""
        list1_a = array_to_list([1, 2, 4])
        list2_a = array_to_list([1, 3, 4])
        list1_b = array_to_list([1, 2, 4])
        list2_b = array_to_list([1, 3, 4])
        
        result_with_dummy = merge_two_lists_with_dummy(list1_a, list2_a)
        result_without_dummy = merge_two_lists_without_dummy(list1_b, list2_b)
        
        assert list_to_array(result_with_dummy) == list_to_array(result_without_dummy)
    
    def test_both_methods_same_result_2(self):
        """Тест: оба метода дают одинаковый результат на примере 2"""
        list1_a = array_to_list([5, 10, 15])
        list2_a = array_to_list([2, 3, 20])
        list1_b = array_to_list([5, 10, 15])
        list2_b = array_to_list([2, 3, 20])
        
        result_with_dummy = merge_two_lists_with_dummy(list1_a, list2_a)
        result_without_dummy = merge_two_lists_without_dummy(list1_b, list2_b)
        
        assert list_to_array(result_with_dummy) == list_to_array(result_without_dummy)
    
    def test_both_methods_empty_lists(self):
        """Тест: оба метода обрабатывают пустые списки одинаково"""
        result_with_dummy = merge_two_lists_with_dummy(None, None)
        result_without_dummy = merge_two_lists_without_dummy(None, None)
        
        assert result_with_dummy == result_without_dummy == None


class TestHelperFunctions:
    """Тесты для вспомогательных функций"""
    
    def test_list_to_array_empty(self):
        """Тест: преобразование пустого списка в массив"""
        assert list_to_array(None) == []
    
    def test_list_to_array_single(self):
        """Тест: преобразование списка с одним элементом в массив"""
        node = Node(42)
        assert list_to_array(node) == [42]
    
    def test_list_to_array_multiple(self):
        """Тест: преобразование списка с несколькими элементами в массив"""
        head = array_to_list([1, 2, 3, 4, 5])
        assert list_to_array(head) == [1, 2, 3, 4, 5]
    
    def test_array_to_list_empty(self):
        """Тест: преобразование пустого массива в список"""
        assert array_to_list([]) is None
    
    def test_array_to_list_single(self):
        """Тест: преобразование массива с одним элементом в список"""
        head = array_to_list([42])
        assert head.data == 42
        assert head.next is None
    
    def test_array_to_list_multiple(self):
        """Тест: преобразование массива с несколькими элементами в список"""
        head = array_to_list([1, 2, 3])
        assert head.data == 1
        assert head.next.data == 2
        assert head.next.next.data == 3
        assert head.next.next.next is None
    
    def test_roundtrip_conversion(self):
        """Тест: преобразование туда и обратно сохраняет данные"""
        original = [1, 2, 3, 4, 5]
        head = array_to_list(original)
        result = list_to_array(head)
        assert result == original

