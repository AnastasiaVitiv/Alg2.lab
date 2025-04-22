import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from lab6 import count_pairs


class TestTribeCombinations(unittest.TestCase):

    def test_basic_case(self):
        pairs = [(1, 2), (2, 4), (3, 5)]
        result, combinations = count_pairs(3, pairs)
        self.assertEqual(result, 4)  # Має бути 4 пари

    def test_single_tribe(self):
        pairs = [(1, 2), (1, 3), (1, 4)]
        result, combinations = count_pairs(3, pairs)
        self.assertEqual(result, 0)
        self.assertEqual(combinations, [])

    def test_multiple_tribes(self):
        pairs = [(1, 2), (2, 4), (1, 3), (3, 5), (8, 10)]
        result, combinations = count_pairs(5, pairs)
        self.assertEqual(result, 6)  # Має бути 6 пар

    def test_empty_case(self):
        pairs = []
        result, combinations = count_pairs(0, pairs)
        self.assertEqual(result, 0)
        self.assertEqual(combinations, [])

    def test_edge_case_one_pair(self):
        pairs = [(1, 2)]
        result, combinations = count_pairs(1, pairs)
        self.assertEqual(result, 0)
        self.assertEqual(combinations, [])


if __name__ == "__main__":
    unittest.main()
