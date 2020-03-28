class Solution:
    def rob(self, nums: List[int]) -> int:
  
        dp = [0] * (len(nums) + 2)    
        for i in range(len(nums)-1,-1,-1):
            dp[i] = max(dp[i+1],nums[i] + dp[i+2])        
        return dp[0]
        
        
#         his = {}        
#         def dp(index):
#             if index >= len(nums):
#                 return 0            
#             if index in his:
#                 return his[index]                
#             max_money = max(nums[index] + dp(index+2),dp(index+1))
#             his[index] = max_money
#             return max_money
#         return dp(0)
            
        
                
        
#         if not nums:return 0
#         if len(nums) <= 2:return max(nums)
#         dp = [0]*len(nums)
#         dp[0] = nums[0]
#         dp[1] = max(nums[0],nums[1])
        
#         for i in range(2,len(nums)):
#             dp[i] = max(dp[i-2]+nums[i],dp[i-1])
#         return dp[-1]
