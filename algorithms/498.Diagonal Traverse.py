#use dic to save the res in same dig
class Solution:
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = [ ]
        dd = {}
        if not matrix: return result
        # Step 1: Numbers are grouped by the diagonals.
        # Numbers in same diagonal have same value of row+col
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                dd[i+j+1] = dd.get(i+j+1,[])+[matrix[i][j]]
                # dd[i+j+1].append(matrix[i][j]) # starting indices from 1, hence i+j+1.
        # Step 2: Place diagonals in the result list.
        # But remember to reverse numbers in odd diagonals.
        for k, v in dd.items():
            if k%2==1: dd[k].reverse()
            result += dd[k]
        return result
