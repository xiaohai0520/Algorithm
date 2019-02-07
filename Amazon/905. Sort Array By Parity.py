class Solution:
    def sortArrayByParity(self, A: 'List[int]') -> 'List[int]':
        l = 0
        r = len(A)-1
        while l < r:
            while A[l] % 2 == 1 and l < r:
                A[l],A[r] = A[r],A[l]
                r -= 1
            l += 1
        return A
