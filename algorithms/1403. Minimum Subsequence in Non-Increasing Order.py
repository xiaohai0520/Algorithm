class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort()
        total = sum(nums)
        res = []
        cur = 0
        while nums:
            n = nums.pop()
            cur += n
            res.append(n)
            total -= n
            if total < cur:
                return res
        return res
