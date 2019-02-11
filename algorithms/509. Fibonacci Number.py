class Solution:
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N < 2:
            return N
        
        dp = [0] * (N+1)
        dp[1] = 1
        for i in range(2,N+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]
        
