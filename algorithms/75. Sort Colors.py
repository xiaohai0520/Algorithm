class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l, r, zero = 0, len(nums)-1, 0
        while l <= r:
            if nums[l] == 0:
                nums[l], nums[zero] = nums[zero], nums[l]
                l += 1
                zero += 1
            elif nums[l] == 2:
                nums[l], nums[r] = nums[r], nums[l]
                r -= 1
            else:
                l += 1
