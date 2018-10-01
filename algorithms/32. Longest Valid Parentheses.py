#use stack

class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        res = 0
        start = -1
        stack = []
        for i,c in enumerate(s):
            if c == '(':
                stack.append(i)
            else:
                if not stack:
                    start = i
                else:
                    stack.pop()
                    if not stack:
                        res = max(res,i-start)
                    else:
                        res = max(res,i-stack[-1])
        return res
                    
