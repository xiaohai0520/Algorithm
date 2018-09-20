#you can find the number yourself in O(n)

class Solution:
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return min(2**32-1, max(nums[-1]*nums[-2]*nums[-3],nums[-1]*nums[0]*nums[1]))
