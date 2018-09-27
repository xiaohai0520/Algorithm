#dp


class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        row = len(grid)
        col = len(grid[0])
        
        res = [[0 for _ in range(col)] for _ in range(row)]
        res[0][0] = grid[0][0]
        for c in range(1,col):
            res[0][c] = res[0][c-1] + grid[0][c]
        for r in range(1,row):
            res[r][0] = res[r-1][0] + grid[r][0]
        
        for i in range(1,row):
            for j in range(1,col):
                res[i][j] = min(res[i-1][j] , res[i][j-1]) + grid[i][j]
        return res[-1][-1]
                
        
