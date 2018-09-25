#random.randint(0,count)
import random
class Solution:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        # self.dic = {}
        # for i,num in enumerate(nums):
        #     self.dic[num] = self.dic.get(num,[])+[i]
        self.nums = nums

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        # return random.choice(self.dic[target])
        result = -1
        count = 0
        for i in range(len(self.nums)):  
            if self.nums[i] == target:
                if random.randint(0, count) == 0: 
                    result = i 
                count += 1
        return result 
        
# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
