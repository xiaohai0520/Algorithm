class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums or len(nums) < 3:
            return []
        nums.sort()
        res = []
        for i in range(len(nums)-2):
            l,r = i+1,len(nums)-1
            if i != 0 and nums[i] == nums[i-1]:
                continue
            while l < r:
                cur = nums[i] + nums[l] + nums[r]
                if  cur == 0:
                    res.append([nums[i],nums[l],nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                elif cur < 0:
                    l +=1
                else:
                    r -= 1
        return res
                
