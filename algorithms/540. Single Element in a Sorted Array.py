class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while(l < r):
            m = (l + r) // 2
            if m % 2 == 0:
                if nums[m] != nums[m + 1]:
                    r = m
                else:
                    l = m + 1
            else:
                if nums[m] != nums[m - 1]:
                    r = m
                else:
                    l = m + 1
                    
        return nums[l]
