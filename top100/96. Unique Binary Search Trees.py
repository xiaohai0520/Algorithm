class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        # dp = [0] * (n+1)
        # dp[0] = 1
        # for i in range(1,n+1):
        #     for j in range(i):
        #         dp[i] += dp[j] * dp[i-1-j]
        # return dp[-1]
        
        return self.helper(1,n)
        
        
    def helper(self,start,end):
        if start > end:
            return 1
        res = 0
        for i in range(start,end+1):
            res += self.helper(start,i-1) * self.helper(i+1,end)
        return res
