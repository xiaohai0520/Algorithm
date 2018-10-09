#trie tree and dfs

class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False
        
class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        node = self.root
        for w in word:
            node = node.children[w]
        node.isWord = True
        

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        node = self.root
        self.res = False
        self.dfs(word,node)
        return self.res 
    
    def dfs(self, word, node):
        if not word:
            if node.isWord:
                self.res = True
            return
        
        if word[0] == ".":
            for n in node.children.values():
                self.dfs(word[1:],n)
        else:
            node = node.children.get(word[0])
            if not node:
                return
            self.dfs(word[1:],node)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
