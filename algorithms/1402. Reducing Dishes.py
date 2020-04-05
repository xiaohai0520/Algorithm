class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        A = satisfaction
        res = total = 0
        A.sort()
        while A and A[-1] + total > 0:
            total += A.pop()
            res += total
        return res
        
        # ls = sorted(satisfaction)
        # res = 0
        # for i in range(len(ls)):
        #     cur_ls = ls[i:]
        #     cur = sum([(i+1)*n for i,n in enumerate(cur_ls)])
        #     res = max(cur,res)
        # return res
