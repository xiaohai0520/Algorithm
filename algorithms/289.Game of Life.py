class Solution:
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        
        def getneighbor(board,i,j):
            
            count = 0
            for i,j in [(i+1,j),(i-1,j),(i+1,j+1),(i-1,j-1),(i,j+1),(i,j-1),(i-1,j+1),(i+1,j-1)]:
                if 0 <= i < len(board) and 0 <= j < len(board[0]) and board[i][j] > 0:
                    count += 1
            return count
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                count = getneighbor(board,i,j)
                board[i][j] = count + 1 if board[i][j] == 1 else -count
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = 1 if board[i][j] in [3,4,-3] else 0
