""" merge_sort tests """
import unittest
import random
from merge_sort import merge_sort


def rand(start, end, num):
    """ helper function to generate random arrays """

    res = []
    for j in range(num):
        res.append(int(random.randint(start, end)))
    return res


class KnownValues(unittest.TestCase):
    """ Class to test merge_sort """

    def test_ms_two_sorted_arrays(self):
        """ merges two sorted arrays """
        arr1 = [1, 3, 5]
        arr2 = [2, 4, 6]
        expected = [1, 2, 3, 4, 5, 6]
        result = merge_sort.merge(arr1, arr2)
        self.assertEqual(expected, result)

    def test_ms_arrays_of_two_lengths(self):
        """handles arrays of different length"""
        arr1 = [1, 3]
        arr2 = [2, 4, 5, 6]
        expected = [1, 2, 3, 4, 5, 6]
        result = merge_sort.merge(arr1, arr2)
        self.assertEqual(expected, result)

    def test_ms_arrays_with_dup_values(self):
        """handles arrays of duplicate values"""
        arr1 = [1, 2, 3]
        arr2 = [3, 4, 5]
        expected = [1, 2, 3, 3, 4, 5]
        result = merge_sort.merge(arr1, arr2)
        self.assertEqual(expected, result)

    def test_ms_with_one_empty_array(self):
        """handles an array that is empty"""
        arr1 = [1, 2, 3]
        arr2 = []
        expected = [1, 2, 3]
        result = merge_sort.merge(arr1, arr2)
        self.assertEqual(expected, result)

    def test_ms_send_None_for_non_int(self):
        """handles arrays of different types"""
        arr1 = ["1", "2", "3"]
        arr2 = [4, 5, 6]
        expected = None
        result = merge_sort.merge(arr1, arr2)
        self.assertEqual(expected, result)
        arr1 = [{}, {}, {}]
        arr2 = [4, 5, 6]
        result = merge_sort.merge(arr1, arr2)
        self.assertEqual(expected, result)
        arr1 = [1.1, 1.2, 1.3]
        arr2 = [4, 5, 6]
        result = merge_sort.merge(arr1, arr2)
        self.assertEqual(expected, result)


    def test_ms_with_arrays(self):
        """ tests merge_sort with worst case scenario """
        arr1 = [7, 0, 6, 1, 5, 2, 4, 3]
        expected = [0, 1, 2, 3, 4, 5, 6, 7]
        result = merge_sort.merge_sort(arr1)
        self.assertEqual(expected, result)

    def test_ms_with_dups_rands(self):
        """ tests merge_sort with worst case scenario """
        arr2 = [-4, -66, -22, 0, 0, 3, 4, 999, 33, 2, 111, 55, 33333333]
        expected = [-66, -22, -4, 0, 0, 2, 3, 4, 33, 55, 111, 999, 33333333]
        result = merge_sort.merge_sort(arr2)
        self.assertEqual(expected, result)

    def test_ms_randomly(self):
        """ tests merge_sort with randomly generated arrays """

        for test in range(100):
            num = 100
            start = -500
            end = 500
            arr3 = rand(start, end, num)
            result = merge_sort.merge_sort(arr3)
            expected = sorted(arr3)
            self.assertEqual(expected, result)



if __name__ == '__main__':
    unittest.main()
