class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(ls):
            dp = [0]* len(ls)
            dp[0] = ls[0]
            dp[1] = max(ls[0],ls[1])
            for i in range(2,len(ls)):
                dp[i] = max(dp[i-1],dp[i-2]+ls[i])
            return dp[-1]
        
        if not nums:
            return 0
        if len(nums) < 3:
            return max(nums)
        nums1 = nums[1:]
        nums2 = nums[:-1]
        return max(helper(nums1),helper(nums2))
