class Solution:
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return 
        
        e = collections.deque()
        for r in range(len(board)):
            for c in range(len(board[0])):
                if (r in [0, len(board)-1] or c in [0, len(board[0])-1]) and board[r][c] == "O":
                    e.append((r, c))
        while e:
            r, c = e.popleft()
            if 0<=r<len(board) and 0<=c<len(board[0]) and board[r][c] == "O":
                board[r][c] = "#"
                e.append((r-1, c))
                e.append((r+1, c))
                e.append((r, c-1))
                e.append((r, c+1))
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] =="O":
                    board[i][j] = 'X'
                elif board[i][j] == "#":
                    board[i][j] = 'O'
#         for i in [0,len(board)-1]:
#             for j in range(len(board[0])):
#                 if board[i][j] == "O":
#                     board[i][j] = '#'
#         for j in [0,len(board[0]) - 1]:
#             for i in range(len(board)):
#                 if board[i][j] == "O":
#                     board[i][j] = '#'
        
        
#     def dfs(self,board,i,j)
        
        
        
   
                
