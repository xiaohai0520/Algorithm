class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:
        n = len(A)
        swap = [n] * n
        non_swap = [n] * n
        swap[0] = 1
        non_swap[0] = 0
        for i in range(1,n):
            if A[i] > A[i-1] and B[i] > B[i-1]:
                non_swap[i] = non_swap[i-1]
                swap[i] = swap[i-1] + 1
            if A[i] > B[i-1] and B[i] > A[i-1]:
                non_swap[i] = min(non_swap[i],swap[i-1])
                swap[i] = min(swap[i],non_swap[i-1]+1)
        return min(swap[-1],non_swap[-1])
