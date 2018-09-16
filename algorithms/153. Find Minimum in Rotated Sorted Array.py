class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]

        if left[0] <= left[-1]:
            m = min(left[0],self.findMin(right))
        else:
            m = min(right[0],self.findMin(left))

        return m
