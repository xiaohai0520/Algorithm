class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dic = {}
        dp = [0 for i in range(len(nums))]
        dp[0] = 1
        for i in range(1,len(nums)):
            ls = []
            for j in range(i):
                if nums[j] < nums[i]:
                    ls.append(dp[j])
            dp[i] = 1 + max(ls) if ls else 1
        return max(dp)
        
