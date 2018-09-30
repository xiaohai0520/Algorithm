#dfs
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board:
            return False
        row = len(board)
        col = len(board[0])

        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0]:
                    if self.dfs(board,i,j,word):
                        return True
        return False
                
 
    def dfs(self,board,i,j,word):
        if not word:
            return True
        if i < 0 or i >= len(board) or j < 0 or j >=len(board[0]) or board[i][j] != word[0]:
            return False
        if board[i][j] == word[0]:
            board[i][j] = '.'
            res = self.dfs(board,i+1,j,word[1:]) or self.dfs(board,i-1,j,word[1:]) or self.dfs(board,i,j+1,word[1:]) or self.dfs(board,i,j-1,word[1:])
            board[i][j] = word[0]
            
            return res
