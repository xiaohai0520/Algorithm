class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        o = obstacleGrid
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        
        
        dp = [[0 for _ in range(col)] for _ in range(row)]
        
        
        for i in range(row):
            if o[i][0] == 0:
                dp[i][0] = 1
            else:
                break
        for i in range(col):
            if o[0][i] == 0:
                dp[0][i] = 1
            else:
                break
                
       
        for i in range(1,row):
            for j in range(1,col):
                if o[i][j] == 1 or (o[i-1][j] == 1 and o[i][j-1] == 1):
                    dp[i][j] = 0
                    continue
                elif o[i-1][j] == 1:
                    dp[i][j] = dp[i][j-1]
                elif o[i][j-1] == 1:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
