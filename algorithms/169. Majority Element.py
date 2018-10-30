class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # nums.sort()
        # return nums[len(nums)//2]
    
        time,target = 0,0
        for num in nums:
            if num == target:
                time += 1
            elif time == 0:
                time,target = 1,num
            else:
                time -= 1
        return target
