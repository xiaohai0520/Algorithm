class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        max_len = i = 0
        while i < len(nums):
            curr = 1
            while i + 1 < len(nums) and nums[i] < nums[i + 1]:
                curr, i = curr + 1, i + 1
            max_len = max(max_len, curr)
            i += 1
        return max_len
