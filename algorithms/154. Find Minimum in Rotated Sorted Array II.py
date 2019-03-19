class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        j = len(nums) - 1
        while i < j:
            # jump duplicate
            while i < j and nums[i] == nums[i + 1]:
                i += 1
            
            while i < j and nums[j] == nums[j - 1]:
                j -= 1
                
            if i == j:
                break
            
            m = (i + j) >> 1
                
            # in lower area
            if nums[m] < nums[j]:
                j = m
            else:
                i = m + 1
                
        return nums[i]
