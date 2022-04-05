import unittest

from algorithm.algebra import *


class AlgebraTestCase(unittest.TestCase):

    def test_get_medium1(self):
        input_list = [9, 8, 7, 6, 5, 4, 3, 8, 1]
        self.assertEqual(get_median(input_list), 6)

    def test_get_medium2(self):
        input_list = [1, 1, 1, 1, 1, 1, 1, 1, 1]
        self.assertEqual(get_median(input_list), 1)

    def test_get_medium3(self):
        input_list = [4, 5, 1, 2, -9, -100, 1000, 0, 99999]
        self.assertEqual(get_median(input_list), 2)

    def test_get_mode1(self):
        input_list = [9, 8, 7, 6, 5, 4, 3, 8, 1]
        self.assertEqual(sorted(get_mode(input_list)), [8])

    def test_get_mode2(self):
        input_list = [1, 1, 1, 1, 1, 1, 1, 1, 1]
        self.assertEqual(sorted(get_mode(input_list)), [1])

    def test_get_mode3(self):
        input_list = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6]
        self.assertEqual(sorted(get_mode(input_list)), sorted([2, 1, 3, 4, 5]))

    def test_get_gcd1(self):
        self.assertEqual(get_gcd(10, 36), 2)

    def test_get_gcd2(self):
        self.assertEqual(get_gcd(10, 19), 1)

    def test_get_gcd3(self):
        self.assertEqual(get_gcd(16, 24), 8)


if __name__ == '__main__':
    unittest.main()
