class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return []
        res = []
        self.dfs(n,n,res,'')
        return res
    
    
    def dfs(self,l,r,res,cur):
        if l > r or l < 0 or r < 0:
            return
        if l == 0 and r == 0:
            res.append(cur)
            return
        self.dfs(l-1,r,res,cur+'(')
        self.dfs(l,r-1,res,cur+')')
