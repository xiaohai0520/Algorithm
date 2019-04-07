class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        A.sort()
        res = [None]*len(A)    
        for a,b in sorted([(n,i) for i,n in enumerate(B)])[::-1]:
            if a<A[-1]:
                res[b] = A.pop()
            else:
                res[b] = A.pop(0)           
        return res
