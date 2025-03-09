import unittest
from main import find_largest_k

class TestFindLargestK(unittest.TestCase):
    def test_valid_cases(self):
        self.assertEqual(find_largest_k([10, 20, 30, 40, 50], 1), (50, [4]))
        self.assertEqual(find_largest_k([5, 3, 8, 6, 2, 7, 4, 1], 5), (4, [6]))
        self.assertEqual(find_largest_k([15, 7, 22, 9, 36, 2, 42, 18], 3), (22, [2]))

    def test_k_out_of_range(self):
        with self.assertRaises(ValueError):
            find_largest_k([10, 20, 30], 4)
        with self.assertRaises(ValueError):
            find_largest_k([1, 2, 3, 4, 5], -1)

    def test_empty_array(self):
        with self.assertRaises(ValueError):
            find_largest_k([], 1)

    def test_duplicate_values(self):
        self.assertEqual(find_largest_k([10, 10, 20, 30, 30], 2), (30, [3, 4]))


if __name__ == "__main__":
    unittest.main()
