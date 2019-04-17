This is a dp problem.

We want to find the maximum pair. 

Record two values, cur_max_res and pre_max_val

every time we need to update the cur_max_res

every time also need to update the previous max value (remember to - 1 for the step)

code:
    
class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        res = pre = 0
        for a in A:
            res = max(res,a+pre)
            pre = max(pre,a) - 1
        return res
