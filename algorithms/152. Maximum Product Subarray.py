#maintain the max and min all the time,choose the max and min from three numbers

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        maxr = minr = res = nums[0]
        for i in range(1,len(nums)):
            maxr, minr = max(maxr*nums[i],nums[i],minr*nums[i]),min(maxr*nums[i],nums[i],minr*nums[i])
            res = max(maxr,res)
        return res
