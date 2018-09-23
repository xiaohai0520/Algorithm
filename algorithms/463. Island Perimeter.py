
#right and down are nb to minus 2 times

class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        land = 0
        nb = 0
        if not grid:
            return 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    land += 1
                    if i + 1 < len(grid) and grid[i+1][j] == 1:
                        nb += 1
                    if j + 1< len(grid[0]) and grid[i][j+1] == 1:
                        nb += 1
        return 4*land - 2*nb
                
