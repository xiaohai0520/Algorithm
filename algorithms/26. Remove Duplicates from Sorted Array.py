
#two pointers, a little like quicksort

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        fast = 1 
        slow = 0
        n = len(nums)
        while fast < n:
            if nums[fast] != nums[slow]:
                slow += 1
                nums[fast],nums[slow] = nums[slow],nums[fast]
            fast = fast + 1
           
        return slow + 1         
