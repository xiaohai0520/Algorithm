# from 0 to len(s) 
# try each chance
# 1. 由于是找最长回文, 有两种情况，一种是奇数个，一种是偶数个，我们先写一个helper方程，从中间往两边一次对比，如果发现不一样则不是回文。
# 遍历字符串所有的index，依次尝试每种情况，可以找到最长回文。时间复杂度O(n2).
# 2. 用动态规划。建立二维数组，n*n。 从0 开始查询字符串的每一位，然后在当前情况下往前查询知道index = 0。 这样数组可以记录之前的所有情况，
# 包括最长的回文。判断条件是如果两个最外侧的字符相等，并且dp[j+1][i-1] = True. 那么这种情况就找到一个更长的回文，更新结果。
# 时间复杂度也是O(n2)。

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ''
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
        
        cur = ''
        for i in range(len(s)):
            for j in range(i,-1,-1):
                if s[i] == s[j] and (i-j<2 or dp[j+1][i-1] == 1):
                    dp[j][i] = 1
                    if i-j+1 > len(cur):
                        cur = s[j:i+1]
        return cur
        

      
    def longestPalindrome1(self, s: str) -> str:    
        def helper(i,j):
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            return s[i+1:j]
        
        res = ''
        for i in range(len(s)):
            cur = helper(i,i)
            if len(cur) > len(res):
                res = cur
            cur = helper(i,i+1)
            if len(cur) > len(res):
                res = cur
        return res
    
