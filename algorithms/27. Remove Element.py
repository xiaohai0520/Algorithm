class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        l = len(nums)
        i = 0
        index = 0
        while i < l:
            if nums[i] != val:
                nums[index], nums[i] = nums[i],nums[index]
                index += 1
            i += 1
        return index
                
