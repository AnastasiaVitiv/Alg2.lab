import unittest

from lab9 import longest_chain

class TestLongestChain(unittest.TestCase):
    def test_example1(self):
        words = [
            "crates", "car", "cats", "crate", "rate",
            "at", "ate", "tea", "rat", "a"
        ]
        self.assertEqual(longest_chain(words), 6)

    def test_example2(self):
        words = [
            "b", "bcad", "bca", "bad", "bd"
        ]
        self.assertEqual(longest_chain(words), 4)

    def test_example3(self):
        words = [
            "word", "anotherword", "yetanotherword"
        ]
        self.assertEqual(longest_chain(words), 1)

    def test_single_letter(self):
        words = ["a"]
        self.assertEqual(longest_chain(words), 1)

    def test_chain_breaks(self):
        words = ["abc", "ab", "a", "x", "xy", "xyz"]
        self.assertEqual(longest_chain(words), 3)

    def test_no_chain(self):
        words = ["abc", "def", "ghi"]
        self.assertEqual(longest_chain(words), 1)

if __name__ == '__main__':
    unittest.main()
