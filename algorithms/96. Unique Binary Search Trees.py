#recursive to dp


class Solution(object):
#     def numTrees(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         return self.getNums(1,n)
            
            
#     def getNums(self,start,end):
#         if start > end:
#             return 1
#         res = 0
#         for i in range(start,end+1):
#             res += self.getNums(start,i-1) * self.getNums(i+1,end)
#         return res

    def DPnumTrees(self,n):
        res = [0] * (n+1)
        res[0] = 1
        for i in range(1, n+1):
            for j in range(i):
                res[i] += res[j] * res[i-1-j]
        return res[n]
