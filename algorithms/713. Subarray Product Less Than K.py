#two pointers with windows
class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k <= 1:
            return 0
        
        n = len(nums)
        count = 0
        
        left = 0
        prod = 1
        
        for right, n in enumerate(nums):
            prod *= n
            while prod >= k:
                prod //= nums[left]
                left += 1
            
            count += right - left + 1
        return count
