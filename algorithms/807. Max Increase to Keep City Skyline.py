

class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ls1 = []
        
        for j in range(len(grid[0])):
            maxr = 0
            for i in range(len(grid)):
                maxr = max(maxr,grid[i][j])
            ls1.append(maxr)
        
        ls2 = [max(line) for line in grid]
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                res += min(ls1[j],ls2[i]) - grid[i][j]
        return res
