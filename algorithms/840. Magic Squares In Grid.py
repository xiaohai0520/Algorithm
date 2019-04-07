class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        magicCount = 0

        for i in range(0, len(grid) - 2):
            for j in range(0, len(grid[0]) - 2):
                if self.isMagic(grid, i, j):
                    magicCount += 1
        return magicCount

    
    def isMagic(self, grid, i, j):
        sum = grid[i][j] + grid[i][j+1] + grid[i][j+2]

        #row check
        for r in range(i, i+3):
            if sum != grid[r][j] + grid[r][j+1] + grid[r][j+2]:
                return False                        

        #column check
        for c in range(j, j+3):
             if sum != grid[i][c] + grid[i+1][c] + grid[i+2][c]:
                return False

        #diagonal check 1
        if sum != grid[i][j] + grid[i+1][j+1] + grid[i+2][j+2]:
            return False

        #diagonal check 2
        if sum != grid[i][j+2] + grid[i+1][j+1] + grid[i+2][j]:            
            return False

        #distinct check
        digitMap = {}
        for r in range(i, i+3):
            for c in range(j, j+3):                
                if grid[r][c] not in digitMap and grid[r][c] < 10 and grid[r][c] > 0:
                    digitMap[grid[r][c]] = True                    
                else:                    
                    return False

        return True
