三个数 总和为0
先对数组进行排序，然后从第一个数开始，创建两个指针，找三个数的和是否为0
找到 加入结果集，小于0 左指针+1   大于0 右指针-1
左右指针变化时注意排除重复的数


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """       
    
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i != 0 and nums[i-1] == nums[i]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if s == 0:
                    res.append([nums[i],nums[left],nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif s < 0:
                    left += 1
                else:
                    right -= 1
        return res
