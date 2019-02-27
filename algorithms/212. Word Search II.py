class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self,word):
        cur = self.root
        for ch in word:
            cur = cur.children[ch]
        cur.end = True
    
    def search(self,word):
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                return False
            cur = cur.chilren[ch]
        return cur.end
    


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        
        
        trie=Trie()
        for word in words:
            trie.insert(word)
        
        row,col=len(board),len(board[0])
        res=[]
        
        def check(root,i,j,path):
            if root.end==True:
                res.append(path)
                root.end=False
                return
            if i<0 or i>=row or j<0 or j>=col:
                return
            letter=board[i][j]
            if not letter in root.children:
                return
            board[i][j]='#'
            check(root.children[letter],i+1,j,path+letter)
            check(root.children[letter],i-1,j,path+letter)
            check(root.children[letter],i,j+1,path+letter)
            check(root.children[letter],i,j-1,path+letter)
            board[i][j]=letter
            
        for i in range(row):
            for j in range(col):
                check(trie.root,i,j,'')
        return res
#         if not words:
#             return []
#         trie = Trie()
#         for word in words:
#             trie.insert(word)
#         self.res = []   
#         for i in range(len(board)):
#             for j in range(len(board[0])):
#                 self.check(trie.root,i,j,board,'')
#         return self.res
    
    
    
#     def check(self,trie,i,j,board,path):
#         if trie.end:
#             self.res.append(path)
#             trie.end = False
#             return
#         if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]): 
#             return 

#         if not board[i][j] in trie.children:
#             return 
#         ch = board[i][j]
#         board[i][j] = '#'
#         self.check(trie.children[ch],i-1,j,board,path+ch)
#         self.check(trie.children[ch],i+1,j,board,path+ch)
#         self.check(trie.children[ch],i,j-1,board,path+ch)
#         self.check(trie.children[ch],i,j+1,board,path+ch)
#         board[i][j] = ch
            
        
        
        
        
        
        
        
        
#         res = []
#         for word in set(words):
#             if self.exist(board,word):
#                 res.append(word)
#         return res
        
        
#     def exist(self,board,word):
#         for i in range(len(board)):
#             for j in range(len(board[0])):
#                 if word[0] == board[i][j]:
#                     if self.helper(board,word,i,j):
#                         return True
#         return False
        
        
#     def helper(self,board,word,i,j):
#         if not word:
#             return True
#         if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] != word[0]:
#             return False
#         ch = board[i][j]
#         board[i][j] = '#'
#         res = self.helper(board,word[1:],i-1,j) or self.helper(board,word[1:],i+1,j) or self.helper(board,word[1:],i,j-1) or self.helper(board,word[1:],i,j+1)
#         board[i][j] = ch
#         return res
