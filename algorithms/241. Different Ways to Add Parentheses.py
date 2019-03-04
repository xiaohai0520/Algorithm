class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return []
        res = []
    
        self.dfs(s,[],res)
        return res
    
    def dfs(self,s,cur,res):
        if not s:
            res.append(cur)
        for i in range(1,len(s)+1):
            if self.isp(s[:i]):
                self.dfs(s[i:],cur+[s[:i]],res)
            
        
    def isp(self,s):
        l,r = 0,len(s)-1
        
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return False
        return True
