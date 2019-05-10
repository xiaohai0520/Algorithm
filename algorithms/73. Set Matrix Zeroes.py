class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = matrix
        r, c = len(m), len(m[0])
        fc = fr = False
        for i in range(r):
            for j in range(c):
                if m[i][j] == 0:
                    if i == 0: fr = True
                    if j == 0: fc = True
                    m[i][0] = m[0][j] = 0
        for i in range(1, r):
            for j in range(1, c):
                if m[i][0] == 0 or m[0][j] == 0:
                    m[i][j] = 0
        if fc:
            for i in range(r):
                m[i][0] = 0
        if fr:
            m[0] = [0] * c
