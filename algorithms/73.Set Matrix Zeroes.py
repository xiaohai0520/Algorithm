class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        ls = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    ls.append((i,j))
        for i in range(len(ls)):
            i,j = ls[i]
            matrix[i] = [0] * len(matrix[0])
            for row in range(len(matrix)):
                matrix[row][j] = 0
            
            
