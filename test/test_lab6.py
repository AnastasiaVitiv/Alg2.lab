import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from lab6 import count_pairs


class TestCountPairs(unittest.TestCase):

    def test_single_tribe(self):
        n = 3
        pairs = [(1, 2), (2, 3), (3, 4)]
        result, combinations = count_pairs(n, pairs)
        self.assertEqual(result, 0)
        self.assertEqual(combinations, [])

    def test_two_tribes(self):
        n = 2
        pairs = [(1, 2), (3, 4)]
        result, combinations = count_pairs(n, pairs)
        self.assertEqual(result, 2)
        self.assertIn((1, 4), combinations)
        self.assertIn((3, 2), combinations)

    def test_three_tribes(self):
        n = 3
        pairs = [(1, 2), (3, 4), (5, 6)]
        result, combinations = count_pairs(n, pairs)
        self.assertEqual(result, 6)

    def test_no_pairs(self):
        n = 0
        pairs = []
        result, combinations = count_pairs(n, pairs)
        self.assertEqual(result, 0)
        self.assertEqual(combinations, [])

    def test_odd_only(self):
        n = 1
        pairs = [(1, 3)]
        result, combinations = count_pairs(n, pairs)
        self.assertEqual(result, 0)

    def test_even_only(self):
        n = 1
        pairs = [(2, 4)]
        result, combinations = count_pairs(n, pairs)
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()
