#from left to right and from right to left
#res[i] = res[i-1] * nums[i-1]
#res[i] = res[i] * p


class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums or len(nums) == 0:
            return nums
        res = [1 for _ in range(len(nums))]
        for i in range(1,len(nums)):
            res[i] = res[i-1] * nums[i - 1]
        p = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= p
            p *= nums[i]
        return res
