class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        
        for i in range(1,7):
            if all(a == i or b == i for a,b in zip(A,B)):
                return min(len(A)-A.count(i),len(B)-B.count(i))
        return -1
        
        
        
        
#         a = b = 0
#         i= 0
#         while i < len(A):
#             if A[i] != A[0] and B[i] != A[0]:
#                 break
#             else:
#                 if A[i] != A[0]:
#                     a += 1
#                 if B[i] != A[0]:
#                     b += 1
#                 if i == len(A)-1:
#                     return min(a,b)
#                 i += 1
#         i = 0
#         a = b = 0
#         while i < len(B):
#             if A[i] != B[0] and B[i] != B[0]:
#                 break
#             else:
#                 if A[i] != B[0]:
#                     a += 1
#                 if B[i] != B[0]:
#                     b += 1
#                 if i == len(B)-1:
#                     return min(a,b) 
#                 i += 1
            
#         return -1
            
