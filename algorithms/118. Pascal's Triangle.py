class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if not numRows:
            return []
        res = [[1]]
        for i in range(1,numRows):
            cur = [1] * (i + 1)
            for j in range(1,i):
                cur[j] = res[i-1][j-1] + res[i-1][j]
            res.append(cur)
        return res
