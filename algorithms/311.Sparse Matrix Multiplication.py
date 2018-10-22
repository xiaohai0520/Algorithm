#check if 0 first
class Solution:
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        # if not A or not B:
        #     return
        # if len(A[0]) != len(B):
        #     return
        # res = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
        # for i in range(len(A)):
        #     for j in range(len(B[0])):
        #         cur = 0
        #         for k in range(len(B)):
        #             cur += A[i][k] * B[k][j]
        #         res[i][j] = cur
        # return res
        m, n, nB = len(A), len(A[0]), len(B[0])
        C = [[0 for i in range(nB)] for j in range(m) ]

        for i in range(m):
            for k in range(n):
                if A[i][k]!=0:
                    for j in range(nB):
                        if B[k][j]!=0:
                            C[i][j] += A[i][k] * B[k][j]
        return C
                    
