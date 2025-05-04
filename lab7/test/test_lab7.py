import unittest

from typing import Tuple

def naive_search(haystack: str, needle: str) -> Tuple[int, int]:
    n = len(haystack)
    m = len(needle)
    comparisons = 0
    last_index = -1

    if m == 0:
        return -1, 0

    for i in range(n - m + 1):
        match = True
        for j in range(m):
            comparisons += 1
            if haystack[i + j] != needle[j]:
                match = False
                break
        if match:
            last_index = i + m - 1

    return last_index, comparisons


class TestNaiveSearchLast(unittest.TestCase):

    def test_found_once(self):
        result = naive_search("abcdef", "cde")
        self.assertEqual(result[0], 4)  # кінець входження
        self.assertGreater(result[1], 0)  # має бути хоча б кілька порівнянь

    def test_found_multiple(self):
        result = naive_search("abcabcabc", "abc")
        self.assertEqual(result[0], 8)  # останнє "abc" — індекси 6–8
        self.assertGreater(result[1], 0)

    def test_not_found(self):
        result = naive_search("abcdef", "xyz")
        self.assertEqual(result[0], -1)
        self.assertGreater(result[1], 0)

    def test_full_match(self):
        result = naive_search("abc", "abc")
        self.assertEqual(result[0], 2)
        self.assertGreater(result[1], 0)

    def test_empty_needle(self):
        result = naive_search("abc", "")
        self.assertEqual(result[0], -1)
        self.assertEqual(result[1], 0)

    def test_empty_haystack(self):
        result = naive_search("", "abc")
        self.assertEqual(result[0], -1)
        self.assertEqual(result[1], 0)

    def test_both_empty(self):
        result = naive_search("", "")
        self.assertEqual(result[0], -1)
        self.assertEqual(result[1], 0)

if __name__ == '__main__':
    unittest.main()
