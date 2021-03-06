class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m,n = len(s),len(p)
        dp = collections.defaultdict(lambda: False)
        dp[0,0] = True
        
        for i in range(1,n+1):
            if p[i-1] == '*':
                dp[0,i] = dp[0,i-1]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if p[j-1] == '*':
                    dp[i,j] = dp[i-1,j] or dp[i,j-1]
                else:
                    dp[i,j] = (s[i-1] == p[j-1] or p[j-1] == '?') and dp[i-1,j-1]
        return dp[m,n]
