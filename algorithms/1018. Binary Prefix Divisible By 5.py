class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        # if not A:
        #     return []
        # res = [False] * len(A)
        # cur = [0] * len(A)
        # res[0] = True if A[0] == 0 else False
        # cur[0] = A[0]
        # for i in range(1,len(A)):
        #     cur[i] = 2*cur[i-1] + A[i]
        #     if cur[i]%5 == 0:
        #         res[i] = True
        # return res
    
    
    
        for i in range(1, len(A)):
            A[i] += A[i - 1] * 2 % 5
        return [a % 5 == 0 for a in A]
        
