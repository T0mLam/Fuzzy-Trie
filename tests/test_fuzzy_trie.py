import unittest

from py_trie.fuzzy_trie import FuzzyTrie


class TestFuzzyTrie(unittest.TestCase):
    """Test the FuzzyTrie properties."""

    def setUp(self):
        self.words = ['apple', 'abple', 'apples', 'apps', 'app']
        self.trie = FuzzyTrie.from_list(self.words)

    def test_fuzzy_search(self):
        self.assertRaises(
            TypeError, 
            self.trie.fuzzy_search, None, 1, 1, True
        )
        self.assertRaises(
            ValueError,
            self.trie.fuzzy_search, 'a', -1, 1, True
        )
        self.assertRaises(
            ValueError,
            self.trie.fuzzy_search, 'a', 1, -1, True
        )
        self.assertRaises(
            TypeError, 
            self.trie.fuzzy_search, 'a', 1, 1, None
        )
        self.assertListEqual(
            sorted(self.trie.fuzzy_search('apple', 1)),
            ['abple', 'apple', 'apples']
        )
        self.assertListEqual(
            sorted(self.trie.fuzzy_search('apple', 2)),
            sorted(self.words)
        )
        self.assertIn('app', self.trie.fuzzy_search('app', 1))


if __name__ == '__main__':
    unittest.main()