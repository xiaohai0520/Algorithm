使用集合去存储，对于每一个位置的上一个数，都有三种限制，行，列和 本身的小九宫格
我们采用元组的形式，讲此个数的行，列，以及九宫格都存起来，存进数组，每个元组都应该唯一
如果有重复，则不为合理数独


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
