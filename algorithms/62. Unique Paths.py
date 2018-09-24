#dp

class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        path = [[1 for _ in range(n)] for _ in range(m)]
        for i in range(m):    
            path[i][0] = 1
        for i in range(1,m):
            for j in range(1,n):
                path[i][j] = path[i-1][j] + path[i][j-1]
        return path[-1][-1]
