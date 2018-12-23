#dfs

class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def dfs(i,j):
            if j != 0 and grid[i][j-1] == '1':
                grid[i][j-1] = '2'
                dfs(i,j-1)
            if j != len(grid[0]) -1 and grid[i][j+1] == '1':
                grid[i][j+1] = '2'
                dfs(i,j+1)
            if i != 0 and grid[i-1][j] == '1':
                grid[i-1][j] = '2'
                dfs(i-1,j)
            if i != len(grid) -1 and grid[i+1][j] == '1':
                grid[i+1][j] = '2'
                dfs(i+1,j)
        
        count = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    grid[i][j] = '2'
                    
                    dfs(i,j)
                    count += 1
        return count
