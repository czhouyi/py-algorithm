import unittest

from algorithm.sort import *


class SortTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.cases = [
            [9, 8, 7, 6, 5, 4, 3, 8, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1],
            [4, 5, 1, 2, -9, -100, 1000, 0, 99999]
        ]

    def test_quick_sort(self):
        for case in self.cases:
            self.assertEqual(quick_sort(case), sorted(case))

    def test_bubble_sort(self):
        for case in self.cases:
            self.assertEqual(quick_sort(case), sorted(case))


if __name__ == '__main__':
    unittest.main()
