#sort as string

class Solution:
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        from functools import cmp_to_key
        def mycmp(x, y):
            return -1 if x + y < y + x else x + y > y + x or 0

        nums = [str(x) for x in nums]
        nums.sort(key=cmp_to_key(mycmp), reverse=True)
        return ''.join(nums).lstrip('0') or '0'
