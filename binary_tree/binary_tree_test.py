import unittest

import binary_tree

class BinaryTree(unittest.TestCase):

    def setUp(self):
        self.tree = binary_tree.BinaryTree()

    def test_insert(self):
        self.tree.insert(10)
        self.tree.insert(7)
        self.tree.insert(23)
        self.tree.insert(55)
        self.tree.insert(13)
        self.assertEqual(self.tree.treeSize(), 5)
        self.tree.printTree()

if __name__ == '__main__':
    unittest.main()
