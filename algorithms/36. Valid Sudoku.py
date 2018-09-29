class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        res = set()
        for i in range(0,9):
            for j in range(0,9):
                if board[i][j] != '.':
                    cur = board[i][j]
                    if (i,cur) in res or (cur,j) in res or (i/3,j/3,cur) in res:
                        return False
                    res.add((i,cur))
                    res.add((cur,j))
                    res.add((i/3,j/3,cur))
        return True
