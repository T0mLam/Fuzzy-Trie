import os
import unittest

from py_trie.trie import Trie


class TestTrie(unittest.TestCase):
    """Test the trie properties."""

    def setUp(self):
        self.trie = Trie()
        self.lower_case_trie = Trie(lower_case=True)

    def test_insert(self):
        self.assertRaises(TypeError, self.trie.insert, 1)
        self.assertRaises(TypeError, self.trie.insert, '')
        self.assertTrue(self.trie.insert('apple'))
        self.assertTrue(self.lower_case_trie.insert('ApPlE'))
        
    def test_find(self):
        self.test_insert()
        self.assertRaises(TypeError, self.trie.find, '')
        self.assertRaises(TypeError, self.trie.find, None)
        self.assertTrue(self.trie.find('apple'))
        self.assertFalse(self.trie.find('app'))
        self.assertFalse(self.trie.find('aPple'))
        self.assertTrue(self.lower_case_trie.find('ApPlE'))
        self.assertTrue(self.lower_case_trie.find('apple'))
        
    def test_complete(self):
        self.test_insert()
        self.assertRaises(TypeError, self.trie.complete, None)
        self.assertIn('apple', self.trie.complete('app'))
        self.assertIn('apple', self.trie.complete(''))
        self.assertNotIn('apple', self.trie.complete('apple'))
        self.assertNotIn('apple', self.trie.complete('Ap'))
        self.assertIn('apple', self.lower_case_trie.complete('aPp'))
        self.assertIn('apple', self.lower_case_trie.complete('app'))
        
    def test_from_list(self):
        words = ['apps', 'apple', 'apply']
        self.trie = self.trie.from_list(words)
        self.assertEqual(len(self.trie), 3)
        self.assertListEqual(sorted(self.trie.complete('app')), sorted(words))
        invalid_list = words + [1]
        self.assertRaises(TypeError, self.trie.from_list, invalid_list)

    def test_from_txt(self):
        words = ['apps', 'apple', 'apples', 'apply']
        path = os.path.dirname(__file__) + '/example.txt'
        self.assertRaises(FileNotFoundError, self.trie.from_txt, path + 'x')
        self.assertRaises(TypeError, self.trie.from_txt, 0)
        self.trie = self.trie.from_txt(path)
        self.assertEqual(len(self.trie), 4)
        self.assertListEqual(sorted(self.trie.complete('app')), sorted(words))


if __name__ == '__main__':
    unittest.main()