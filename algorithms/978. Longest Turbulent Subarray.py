class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        dp = [1] * len(A)
        
        for i in range(1,len(A)):
            
            if i >= 2:
                if A[i-2] < A[i-1] > A[i] or A[i-2] > A[i-1] < A[i]:
                    dp[i] = dp[i-1] + 1
                    continue
            if A[i] != A[i-1]:
                dp[i] = 2
        return max(dp)
