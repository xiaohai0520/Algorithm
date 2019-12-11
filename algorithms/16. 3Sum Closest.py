跟 3sum 思路差不多，也是一个N2 的时间复杂度，
用一个指针遍历所有的数，另外两个指针从两边忘中间去比较各种情况
当等于目标值的时候，直接返回，
如果比target小，则左边+1
否则 右边-1

然后每次比较一下绝对值，更新要找的结果值


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if not nums:
            return float('inf')
        
        res = float('inf')
        
        i = 0
        nums.sort()
        while i < len(nums)-2:
            if i > 0 and nums[i] == nums[i-1]:
                i += 1
                continue
                
            l = i+1
            r = len(nums)-1
            while l < r:
                cur = nums[i] + nums[l] + nums[r]

                if cur == target:
                    return cur

                elif cur < target:
                    l += 1
                else:
                    r -= 1
                if abs(cur-target) < abs(res-target):
                    res = cur
            i += 1
        return res
        
        
        
        
        
        
        
        
        
