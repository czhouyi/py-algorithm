import unittest

from algorithm.least_cost import *


class LeastCostTestCase(unittest.TestCase):

    def test_least_cost(self):
        case = [[5, 7, 9], [6, 1, 3], [4, 2, 8]]
        self.assertEqual(least_cost(case), 10)


if __name__ == '__main__':
    unittest.main()
