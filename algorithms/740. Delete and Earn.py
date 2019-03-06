class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = max(nums)
        points = [0] * (n+1)
        for num in nums:
            points[num] += num
        cur = pre = 0
        for i in range(1,n+1):
            cur,pre = max(pre+points[i],cur),cur
        return cur
