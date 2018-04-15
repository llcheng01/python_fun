# import pdb

class BinaryTree(object):
    def __init__(self):
    # Default None for root
        self.root = None
        self.size = 0

    class TreeNode(object):
        def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None

    def find(self, key):
        pass

    def treeSize(self):
        return self._treeSize(self.root)

    def _treeSize(self, current):
        if current is None:
            return 0

        if current is not None:
            return self._treeSize(current.left) + self._treeSize(current.right) + 1

    def insert(self, x):
        # pdb.set_trace()
        if self.root is None:
            self.root = self.TreeNode(x)
        else:
            self.root = self._insert(x, self.root)

    def _insert(self, x, current):
        # pdb.set_trace()
        # store the parents of current
        if (x < current.val):
            if current.left is None:
                current.left = self.TreeNode(x)
            else:
                self._insert(x, current.left)
        else:
            if current.right is None:
                current.right = self.TreeNode(x)
            else:
                self._insert(x, current.right)

        return current

    def printTree(self):
        if self.root is not None:
            self._printTree(self.root)

    def _printTree(self, current):
        if current is not None:
            self._printTree(current.left)
            print(str(current.val) + '  ')
            self._printTree(current.right)

    def delete(self, key):
        pass
