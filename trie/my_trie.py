class MyTrie(object):
    def __init__(self):
        self.radix = 26
        self.root = self.TrieNode()
    """
    Capture the list of nodes that represent lowercase character in the alphabet
    """
    class TrieNode(object):
        def __init__(self):
            self.isEnd = False
            self.children = [None] * 26;

    def get(self, key):
        pass

    def _get(self, node, key, index):
        pass

    def _charToIndex(self, char):
        return ord(char) - ord('a')

    def size(self):
        return self._size(self.root)

    """
    Lazy recursive size. Not performance
    """
    def _size(self, node):
        if node is None:
            return 0

        count = 0
        if (node.isEnd != True):
            count += 1

        # Loop thru 26 chars
        for n in node.children:
            count += self._size(n)

        return count

    def search(self, key):
        return self._search(self.root, key, 0)

    def _search(self, node, key, level):
        if level == len(key):
            return node != None and node.isEnd

        index = self._charToIndex(key[level])

        if not node.children[index]:
            return False

        return self._search(node.children[index], key, level + 1)


    def put(self, key):
        self.root = self._put(self.root, key, 0)

    """
    If not present, inserts key into trie
    If the key is prefix of the trie node, marks as leaf node
    """
    def _put(self, node, key, level):
        if node is None:
            node = self.TrieNode()

        """
        Finished adding the whole string
        """
        if level == len(key):
            node.isEnd = True
            return node

        index = self._charToIndex(key[level])

        node.children[index] = self._put(node.children[index], key, level + 1)
        return node
