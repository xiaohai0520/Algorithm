class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        M, N = len(matrix), len(matrix[0])
        count = 0
        for k in range(M):
			# sum from row k to the last row
            sumall = [0]*N
            for i in range(k, M):
                vals = collections.defaultdict(int)
                vals[0] = 1
                val = 0
                for j in range(N):
                    sumall[j] += matrix[i][j]
                    val += sumall[j]
                    count += vals[val-target]
                    vals[val] += 1
        return count
