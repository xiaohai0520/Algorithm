class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    curarea = self.dfs(grid,i,j)
                    area = max(area,curarea)
        return area
        
        
    def dfs(self,grid,i,j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0:
            return 0
        grid[i][j] = 0
        return 1 + self.dfs(grid,i+1,j) + self.dfs(grid,i-1,j) + self.dfs(grid,i,j+1) + self.dfs(grid,i,j-1)
        
