class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        start,end = 0,0
        flag = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'R':
                    start,end = i,j
                    flag = 1
                    break
            if flag:
                break

        
        res = 0
        while i > 0:
            i -= 1

            if board[i][j] == 'B':
                break
            elif board[i][j] == 'p':
                res += 1
                break

        i = start

        while i < len(board) - 1:
            
            i += 1

            if board[i][j] == 'B':
                break
            elif board[i][j] == 'p':

                res += 1
                break 

        i = start  
        while j > 0:
            j -= 1
            if board[i][j] == 'B':
                break
            elif board[i][j] == 'p':
                res += 1
                break
           
            
        i,j = start,end
        while j < len(board[0])-1:
            j += 1
            if board[i][j] == 'B':
                break
            elif board[i][j] == 'p':
                res += 1
                break
            
        return res
        
            
            
