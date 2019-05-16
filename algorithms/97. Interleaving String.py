class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        l1 = len(s1)
        l2 = len(s2)
        dp = [[0 for _ in range(l2 + 1)] for _ in range(l1 + 1)] 
        dp[0][0] = 1
        for i in range(1,l1+1):
            dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
        for j in range(1,l2+1):
            dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]
        for i in range(1,l1+1):
            for j in range(1,l2+1):
                dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i-1+j]) or (dp[i][j-1] and s2[j-1] == s3[j-1+i])
        
        return dp[-1][-1] == 1
