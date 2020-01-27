每次记录一下最远可到达的index， 如果此刻的index 大于最远的，我们视为不可到达last index,


class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        maxReach = 0
        for i in range(len(nums)):
            if i > maxReach:
                return False
            maxReach = max(maxReach, i+nums[i])
        return True
