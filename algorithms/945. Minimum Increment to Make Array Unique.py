class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        if not A or len(A) == 1:
            return 0
        
        res = need = 0
        for i in sorted(A):
            res += max(need-i,0)
            need = max(need+1,i+1)
        return res
        
