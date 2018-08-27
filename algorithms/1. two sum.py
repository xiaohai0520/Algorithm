# use enumerate to save index and difference in the dic

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
#         dic = {}
#         for i in range(len(nums)):
#             if nums[i] in dic:
#                 return [dic[nums[i]], i]
#             else:
#                 dic[target - nums[i]] = i
        dic = {}        
        for i,num in enumerate(nums):
            if num in dic:
                return [dic[num],i]
            else:
                dic[target - num] = i
