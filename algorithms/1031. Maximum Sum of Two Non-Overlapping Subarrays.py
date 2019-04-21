This is a Dp problem.

Because it is a subarray pronlem. We use the prefix sum firstly.

We give the initial max val of L M and L+M

each time step + 1, we update the L and M compare with the new possible.

Then we can update the L+M    MAX(RES, LMAX + new M or Mmax + new L）

CODE:

class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        for i in xrange(1, len(A)):
            A[i] += A[i - 1]
        res, Lmax, Mmax = A[L + M - 1], A[L - 1], A[M - 1]
        for i in xrange(L + M, len(A)):
            Lmax = max(Lmax, A[i - M] - A[i - L - M])
            Mmax = max(Mmax, A[i - L] - A[i - L - M])
            res = max(res, Lmax + A[i] - A[i - M], Mmax + A[i] - A[i - L])
        return res
        
        
        
        
#         dp = [0] * len(A)
#         dp[0] = A[0]
#         for i in range(1,len(A)):
#             dp[i] = dp[i-1] + A[i]
#         res = 0
        
#         for i in range(len(A)-L+1):
#             if i == 0:
#                 resL = dp[L - 1]
#             else:   
#                 resL = dp[i+L-1] - dp[i-1]
#             print(resL)
#             for j in range(i):
#                 if i - j < M:
#                     break
#                 if j == 0:
                    
#                     res = max(res,resL + (dp[j+M-1]))
#                 else:
#                     res = max(res,resL + (dp[j+M-1]-dp[j-1]))
#             for j in range(i+L,len(A)):
#                 if len(A) - j < M:
#                     break
#                 res = max(res,resL + dp[j + M - 1] - dp[j-1])
#         return res
                
                
            
            
