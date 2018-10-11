#dp

class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
#         self.res = 0
#         coins.sort(reverse=True)
        
#         def dfs(amount,coins,start,cur):
#             if cur > amount:
#                 return 
#             if cur == amount:
#                 self.res += 1
#                 return 

#             for i in range(start,len(coins)):
#                 dfs(amount,coins,i,cur+coins[i])
#         dfs(amount,coins,0,0)
#         return self.res
    
    
        dp = [0] * (amount + 1)
        dp[0] = 1
        for i in coins:
            for j in range(i, amount + 1):
                dp[j] += dp[j - i]
        return dp[amount]
        
        
    
