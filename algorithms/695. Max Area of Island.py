#dfs to calculate the areas of each island


class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        areas = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] :
                    areas.append(self.dfs(grid,i,j))
        return max(areas) if areas else 0
        
        
    def dfs(self,grid,i,j):
        if 0<= i < len(grid) and 0<= j < len(grid[0]) and grid[i][j]:
            grid[i][j] = 0
            return 1+ self.dfs(grid,i-1,j) + self.dfs(grid,i+1,j) + self.dfs(grid,i,j-1) + self.dfs(grid,i,j+1)
        else:
            return 0
