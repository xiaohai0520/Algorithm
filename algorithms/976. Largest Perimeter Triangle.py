class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort(reverse=True)
        res = 0
        for i in range(len(A)-2):
            if A[i] < A[i+1] + A[i+2]:
                res = max(res,A[i] + A[i+1] + A[i+2])
        return res
                    
            
