一般对称的问题，可以使用stack来解决问题。
初始化一个start index, 作为左边界
依次遍历字符串，如果为左括号，讲index放入stack,
如果是右括号，分析情况，如果此时stack是空，说明从这位以及之前的都不能是对称的，更新start,

如果不为空，可以和stack中的左括号组成一对，那么我们要讲stack中的左括号pop出一个，
这个时候如果stack空，更新长度，以start为左边界，如果不为空，以stack中最后一个左括号的index为左边界

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
                    
