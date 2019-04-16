This is a dfs problem.

We can dfs from the bound and change all the path it can reach to 0. then count the number of 1

code:
class Solution:
    def numEnclaves(self, A: List[List[int]]) -> int:
        if not A:
            return 0
        
        def helper(i,j):
            if i < 0 or j < 0 or i >= len(A) or j >= len(A[0]) or A[i][j] == 0:
                return 
            A[i][j] = 0
            helper(i+1,j)
            helper(i-1,j)
            helper(i,j+1)
            helper(i,j-1)
        
        for i in range(len(A)):
            for j in range(len(A[0])):
                if (i == 0 or j == 0 or i == len(A)-1 or j == len(A[0])-1) and A[i][j] == 1:
                    helper(i,j)
                    
        
        res = 0
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 1:
                    res += 1
        return res
        
            
        
