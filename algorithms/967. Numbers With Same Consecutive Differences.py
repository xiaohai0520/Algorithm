Dfs problem.

each time we add one digit, we make sure it satifiy the condition.


Code:

class Solution:
    def numsSameConsecDiff(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """
        if N == 1:
            return [i for i in range(10)]
        if K == 0:
            return list(map(int,[str(i)*N for i in range(1,10)]))
        
        res = []
        def dfs(path,l):
            if l == N:
                res.append(path)
                return
            cur = path % 10
            if cur + K < 10:
                dfs(path * 10 + cur + K, l + 1)
            if cur - K >= 0:
                dfs(path * 10 + cur - K, l + 1)
            
        
        
        for i in range(1,10):
            dfs(i,1)
        return res
            
        
