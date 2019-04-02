class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        res = pre = 0
        for a in A:
            res = max(res,a+pre)
            pre = max(pre,a) - 1
        return res
