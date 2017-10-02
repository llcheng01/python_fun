import unittest

import my_trie

class MyTrie(unittest.TestCase):

    def setUp(self):
        self.myTrie = my_trie.MyTrie()

    def test_put(self):
        self.myTrie.put('foo')
        self.myTrie.put('bar')
        print(self.myTrie)
        print(self.myTrie.size())
        self.assertEqual(self.myTrie.size(), 5)

    def test_search(self):
        self.myTrie.put('foo')
        self.myTrie.put('food')
        self.assertEqual(self.myTrie.search('food'), True)
        self.assertEqual(self.myTrie.search('fat'), False)


if __name__ == '__main__':
    unittest.main()
