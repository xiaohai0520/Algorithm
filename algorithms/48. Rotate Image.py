#xiezhe yici shuzheyici


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(i,len(matrix[0])):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
                
        for i in range(len(matrix)):
            for j in range(len(matrix)//2):
                matrix[i][j],matrix[i][len(matrix[0])-j-1] = matrix[i][len(matrix[0])-1-j],matrix[i][j]
                
        
        
