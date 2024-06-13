import unittest

from py_trie.trie import Trie


class TestTrie(unittest.TestCase):
    """Test the trie properties."""

    def setUp(self):, None)
        self.assertTrue(self.trie.find('apple'))
        self.assertFalse(self.trie.find('app'))
        self.assertFalse(self.trie.find('aPple'))
        
        self.trie = Trie()

    def test_insert(self):
        self.assertRaises(TypeError, self.trie.insert, 1)
        self.assertRaises(TypeError, self.trie.insert, '')
        self.assertTrue(self.trie.insert('apple'))
        
    def test_find(self):
        self.test_insert()
        self.assertRaises(TypeError, self.trie.find, '')
        self.assertRaises(TypeError, self.trie.find
    def test_complete(self):
        self.test_insert()
        self.assertIn('apple', self.trie.complete('app'))
        self.assertIn('apple', self.trie.complete(''))
        self.assertNotIn('apple', self.trie.complete('apple'))
        self.assertNotIn('apple', self.trie.complete('Ap'))


if __name__ == '__main__':
    unittest.main()