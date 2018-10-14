#dp or 2n -1 center 

class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """

        length = len(s)
        if length == 0:
            return 0
        count = 0
        for center in range(2*length):
            left = center // 2
            right = left + center % 2
            while left >= 0 and right < length and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
        return count
    
    
        # if s == '': return 0
        # dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
        # for i in range(len(s)): dp[i][i] = 1
        # for r in range(len(s)-1, -1, -1):
        #     for c in range(r+1, len(s)):
        #         if c == r+1:
        #             dp[r][c] = 1 if s[r]==s[c] else 0
        #         else:
        #             dp[r][c] = 1 if s[r]==s[c] and dp[r+1][c-1]==1 else 0
        # return sum([sum(row) for row in dp])
