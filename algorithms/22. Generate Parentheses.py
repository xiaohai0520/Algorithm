#use backtracking and set the condition not valid
#dfs

class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        res = []
        self.helper(n,n,'',res)
        return res
        
        
    def helper(self,l,r,path,res):
        if l == 0 and r == 0:
            res.append(path)
            return
        if l < 0 or r < 0 or l > r:
            return 
        self.helper(l-1,r,path+'(',res)
        self.helper(l,r-1,path+')',res)
