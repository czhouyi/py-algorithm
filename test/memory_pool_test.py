import unittest

from algorithm.memory_pool import MemoryPool


class MemoryPoolTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.pool = MemoryPool(100)

    def test(self):
        self.assertEqual(self.pool.request(10), 0)
        self.assertEqual(self.pool.request(20), 10)
        self.assertEqual(self.pool.request(30), 30)
        self.assertEqual(self.pool.request(30), 60)
        self.assertEqual(self.pool.request(11), 'error')
        self.assertEqual(self.pool.release(5), 'error')
        self.assertEqual(self.pool.release(30), None)
        self.assertEqual(self.pool.request(11), 30)
        self.assertEqual(self.pool.request(11), 41)
        self.assertEqual(self.pool.request(11), 'error')


if __name__ == '__main__':
    unittest.main()
