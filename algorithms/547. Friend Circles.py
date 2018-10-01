#dfs

class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
#         if not M:
#             return 0
#         res = 0
#         row = len(M)
#         col = len(M[0])
#         for i in range(row):
#             for j in range(col):
#                 if M[i][j] == 1:
#                     self.dfs(M,i,j)
#                     res += 1
#         return res
        
#     def dfs(self,M,i,j):

#         for k in range(len(M[0])):
#             if M[i][k] == 1:
#                 M[i][k] = 0
#                 self.dfs(M,i,k)
#         for m in range(len(M)):
            
#             if M[m][j] == 1:
#                 M[m][j] = 0
#                 self.dfs(M,m,j)
               
    
        
        if not M:
            return 0
        count = 0
        visit = [0] * len(M)
        for i in range(len(M)):
            if visit[i] == 0:
                self.dfs(M,i,visit)
                count += 1
        return count

    def dfs(self,M,i,visit):
        for j in range(len(M)):
            if M[i][j] == 1 and visit[j] == 0:
                visit[j] = 1
                self.dfs(M,j,visit)
        
        
            
            
            
            
            
