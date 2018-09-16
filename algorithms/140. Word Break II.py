#dfs + dp
#dfs get every possible and dp to check if can break


class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        res = []
        self.dfs(s,wordDict,'',res)
        return res
        
    def dfs(self,s,wordDict,path,res):
        if self.check(s,wordDict):
            if not s:
                res.append(path[:-1])
                return 
            for i in range(1,len(s)+1):
                if s[:i] in wordDict:
                    self.dfs(s[i:],wordDict,path + s[:i] + ' ',res)
        
        
        
        
    def check(self,s,wordDict):
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(1,len(s)+1):
            for w in wordDict:
                if w == s[i-len(w):i] and dp[i-len(w)] :
                    dp[i] = True
        return dp[-1]
