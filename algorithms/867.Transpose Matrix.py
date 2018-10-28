class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
#         row = len(A)
#         col = len(A[0])
        
#         B = [[0 for i in range(row)] for j in range(col)]
#         for i in range(row):
#             for j in range(col):
#                 B[j][i] = A[i][j]
#         return B
        return list(zip(*A))
