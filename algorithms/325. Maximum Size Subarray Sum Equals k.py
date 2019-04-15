This is a subarray question.

It always need to save the history path in a dic.

We only need to save the sum value first appear, because we only need to get the largest distance.

Code:

class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:

        if not nums:
            return 0
        dic = {0:-1}
        cur = 0
        res = 0
        for i in range(len(nums)):
            cur += nums[i]
            if cur not in dic:
                dic[cur] = i
            if cur - k in dic:
                res = max(res,i-dic[cur-k])
        return res
