# 这个regular expression 从最开始刷lc的时候就一直skip, 总觉得很麻烦，终于下定决心给这个题弄个明白
# 对于两个字符串的比较，首先可以考虑的是dp来做比较方便，由于python中的字典比较随意，我们也可以用字典来代替数组做dp.
# DP:
    当s和p都为空时，结果存为True
    当s不为空时，开始比较s和p, 如果 s[i] = p[j]  or p[j] = '.', 则dp[i,j] = dp[i-1,j-1]
    然后分析p[j] = '*' 的情况，
        如果 s[i] != p[j-1] and p[j-1] != '.',则 让* 取消当下位和前面一位， dp[i, j] = dp[i, j-2]
        其他情况 dp[i, j] = dp[i, j-2] or dp[i, j-1] or dp[i-1, j]  
            dp[i,j-2] 是 p[j-1] = '.'   
            dp[i,j-1] 是 p[j-1]= s[i] 使 * 作为1 使用
            dp[i-1,j] 是 * 作为 大于1 的情况使用
            
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = collections.defaultdict(lambda: False)
        dp[-1, -1] = True
        for i in range(-1, m):
            for j in range(n):
                if i >= 0 and s[i] == p[j] or p[j] == '.':
                    dp[i, j] = dp[i-1, j-1]
                if p[j] == '*':
                    if i == -1 or s[i] != p[j-1] and p[j-1] != '.':
                        dp[i, j] = dp[i, j-2]
                    else:
                        dp[i, j] = dp[i, j-2] or dp[i, j-1] or dp[i-1, j]
        # print(dp)
        return dp[m-1, n-1]
        
