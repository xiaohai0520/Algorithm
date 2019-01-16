class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        # dp = [0] * (len(s) + 1)
        # res = 0
        # stack = []
        # for i in range(len(s)):
        #     if s[i] == '(':
        #         stack.append(i)
        #     else:
        #         if stack:
        #             p = stack.pop()
        #             dp[i+1] = dp[p] + i - p + 1
        # return max(dp)
        
        
        stack = [0]
        res = 0
        for i,c in enumerate(s):
            if c == '(':
                stack.append(0)
            else:
                if len(stack) > 1:
                    p = stack.pop()
                    stack[-1] += p + 2
                    res = max(res,stack[-1])
                else:
                    stack = [0]
        return res
