#like linklist cycle find the meet point
#slow is head and go step
#the meet point is start

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        fast = slow = 0
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast == slow:
                break
        slow = 0
        while fast != slow:
            fast = nums[fast]
            slow = nums[slow]
        return slow
