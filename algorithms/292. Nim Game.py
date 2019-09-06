class Solution:
    def canWinNim(self, n: int) -> bool:
        if n >=134882061:
            return n%4 != 0
        if n <= 3:
            return True
        dp = [False] * (n+1)
        dp[1] = dp[2] = dp[3] = True
        for i in range(4,n+1):
            dp[i] = not (dp[i-1] and dp[i-2] and dp[i-3])
        return dp[-1]
