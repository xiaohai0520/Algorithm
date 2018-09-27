#looks like dp always to find the min num

class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0 for i in range(n)]
        dp[0] = 1
        i2 = i3 = i5 = 0
        for i in range(1,n):
            u2,u3,u5 = dp[i2] * 2,dp[i3] * 3,dp[i5] * 5
            dp[i] = min(u2,u3,u5)
            if dp[i] == u2:
                i2 += 1
            if dp[i] == u3:
                i3 += 1
            if dp[i] == u5:
                i5 += 1
        return dp[-1]
            
        
        
        
        
        
