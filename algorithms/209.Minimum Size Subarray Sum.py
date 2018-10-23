
class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        total = left = 0
        res = len(nums) + 1
        for right,num in enumerate(nums):
            total += num
            while total >= s:
                res = min(res,right - left + 1)
                total -= nums[left]
                left += 1
        return res if res <= len(nums) else 0
