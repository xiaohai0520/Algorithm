class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        medianIndex = int((len(nums)-1)/2)
        ans = [0] * len(nums)
        ans[::2] = nums[medianIndex::-1]
        ans[1::2] = nums[:medianIndex:-1]
        for i in range(len(nums)):
            nums[i] = ans[i]
