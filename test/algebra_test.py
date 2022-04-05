import unittest

from algorithm.algebra import *


class AlgebraTestCase(unittest.TestCase):

    def test_get_medium(self):
        input_list = [9, 8, 7, 6, 5, 4, 3, 8, 1]
        self.assertEqual(get_median(input_list), 6)
        input_list = [1, 1, 1, 1, 1, 1, 1, 1, 1]
        self.assertEqual(get_median(input_list), 1)
        input_list = [4, 5, 1, 2, -9, -100, 1000, 0, 99999]
        self.assertEqual(get_median(input_list), 2)

    def test_get_mode(self):
        input_list = [9, 8, 7, 6, 5, 4, 3, 8, 1]
        self.assertEqual(sorted(get_mode(input_list)), [8])
        input_list = [1, 1, 1, 1, 1, 1, 1, 1, 1]
        self.assertEqual(sorted(get_mode(input_list)), [1])
        input_list = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6]
        self.assertEqual(sorted(get_mode(input_list)), sorted([2, 1, 3, 4, 5]))


if __name__ == '__main__':
    unittest.main()
