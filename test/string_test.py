import unittest

from algorithm.string import *


class StringTestCase(unittest.TestCase):

    def test_reverse(self):
        input_str = 'hello world'
        self.assertEqual(reverse('hello world'), input_str[::-1])


if __name__ == '__main__':
    unittest.main()
