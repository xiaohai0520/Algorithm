This is a graph problem.

We need to track every one support number and whether it support other.

Two conditions can help us to solve this question.

Code:

from collections import defaultdict
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        A = [True] * N
        B = [0] * N
        
        for a, b in trust:
            A[a - 1] = False
            B[b - 1] += 1
        
        for i in range(N):
            if A[i] and B[i] == N - 1:
                return i + 1
        
        return -1
#         if not trust:
#             return N
#         dic = defaultdict(list)
#         for i,j in trust:
#             dic[j].append(i)
            
#         for key in dic:
#             if len(dic[key]) == N - 1:
#                 for l in dic.values():
#                     if key in l:
#                         break
                
#                 else:
#                     return key
#         return -1
                
