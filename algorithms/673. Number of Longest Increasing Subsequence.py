class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp1 = [1] * len(nums)
        dp2 = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp1[j] + 1 > dp1[i]:
                        dp1[i] = dp1[j] + 1
                        dp2[i] = dp2[j]
                    elif dp1[j] + 1 == dp1[i]:
                        dp2[i] += dp2[j]
        res = 0
        maxl = max(dp1)
        for i,num in enumerate(dp1):
            if num == maxl:
                res += dp2[i]
        return res
            
        
