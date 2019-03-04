class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        
        self.dp = [0]*len(nums) 
        if nums:
            self.dp[0] = 0
            for i in range(1,len(nums)):
                self.dp[i] = self.dp[i-1]+ nums[i]

    def sumRange(self, i: int, j: int) -> int:
        if not self.nums:
            return 0
        
        return self.dp[j] - self.dp[i] + self.nums[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
