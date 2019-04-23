class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        A.sort()
        l,r = len(A)//2-1,len(A)//2
        if A[l] == A[r] or A[l] == A[l-1]:
            return A[l]

        else:
            return A[r]
