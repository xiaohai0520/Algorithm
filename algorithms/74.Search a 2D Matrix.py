logn from half  binary search
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        # i = 0
        # j = len(matrix[0])-1
        # while i < len(matrix) and j >= 0:
        #     if matrix[i][j] == target:
        #         return True
        #     elif matrix[i][j] < target:
        #         i += 1
        #     else:
        #         j -= 1
        # return False


        rows, cols = len(matrix), len(matrix[0])
        low, high = 0, rows * cols - 1
        
        while low <= high:
            mid = (low + high) // 2
            num = matrix[mid // cols][mid % cols]

            if num == target:
                return True
            elif num < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return False
