class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        mod = 10**9+7
        dp = [[0 for _ in range(target + 1)] for _ in range(d+1)] 
        dp[0][0] = 1
        for i in range(1,d+1):
            for j in range(1,target+1):
                for k in range(1,min(f,j)+1):
                    dp[i][j] += dp[i-1][j-k]
                
        return dp[-1][-1]%mod
