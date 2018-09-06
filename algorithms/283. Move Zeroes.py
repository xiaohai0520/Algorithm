#like quick sort

class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = -1
        for j in range(len(nums)):
            if nums[j] != 0:
                i += 1
                nums[i],nums[j] = nums[j],nums[i]
