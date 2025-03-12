import unittest
from lab2 import min_eating_gorilla


class TestMinEatingGorilla(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(min_eating_gorilla([3, 6, 7, 11], 8), 4)
        self.assertEqual(min_eating_gorilla([30, 11, 23, 4, 20], 5), 30)
        self.assertEqual(min_eating_gorilla([30, 11, 23, 4, 20], 6), 23)

    def test_edge_cases(self):
        self.assertEqual(min_eating_gorilla([1], 1), 1)
        self.assertEqual(min_eating_gorilla([1000000000], 2), 500000000)
        self.assertEqual(min_eating_gorilla([1, 1, 1, 1, 1], 5), 1)


if __name__ == "__main__":
    unittest.main()
