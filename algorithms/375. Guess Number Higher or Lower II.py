class Solution:
    def getMoneyAmount(self, n: int) -> int:
        # need = [[0] * (n+1) for _ in range(n+1)]
        # for lo in range(n, 0, -1):
        #     for hi in range(lo+1, n+1):
        #         need[lo][hi] = min(x + max(need[lo][x-1], need[x+1][hi]) for x in range(lo, hi))
        # return need[1][n]
        
        
        dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
        for l in range(1, n+1):
            for j in range(l, n+1):
                i = j - l
                dp[i][j] = min(i + dp[i+1][j], j + dp[i][j-1])
                for k in range(i+1, j):
                    dp[i][j] = min(dp[i][j], k + max(dp[i][k-1], dp[k+1][j]))
        return dp[1][n]
