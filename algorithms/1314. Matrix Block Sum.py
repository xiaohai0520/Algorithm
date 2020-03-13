class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if i > 0:
                    mat[i][j] += mat[i - 1][j]
                if j > 0:
                    mat[i][j] += mat[i][j - 1]
                if i > 0 and j > 0:
                    mat[i][j] -= mat[i - 1][j - 1]
        
        result = [[0] * len(mat[0]) for _ in range(len(mat))]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                lower = max(0, i - K)
                upper = min(len(mat) - 1, i + K)
                left = max(0, j - K)
                right = min(len(mat[0]) - 1, j + K)
                result[i][j] += mat[upper][right]
                if left > 0:
                    result[i][j] -= mat[upper][left - 1]
                if lower > 0:
                    result[i][j] -= mat[lower - 1][right]
                if left > 0 and lower > 0:
                    result[i][j] += mat[lower - 1][left - 1]
        return result
