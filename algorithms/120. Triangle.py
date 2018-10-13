#dp from bottom to top

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 0
        # for i in range(1,len(triangle)):
        #     for j in range(len(triangle[i])):
        #         if j == 0:
        #             triangle[i][j] += triangle[i-1][j]
        #         elif j == len(triangle[i]) - 1:
        #             triangle[i][j] += triangle[i-1][j-1]
        #         else:
        #             triangle[i][j] += min(triangle[i-1][j],triangle[i-1][j-1])
        # return min(triangle[-1])
            
        f = [0] * (len(triangle) + 1)
        for row in triangle[::-1]:
            for i in xrange(len(row)):
                f[i] = row[i] + min(f[i], f[i + 1])
        return f[0]
