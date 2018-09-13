#bfs
class Solution:
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def isval(s):
            res = 0
            for i in range(len(s)):
                if s[i] == '(':
                    res += 1
                elif s[i] == ')':
                    res -= 1
                if res < 0:
                    return False
            return res == 0
        
        level = {s}
        while 1:
            res = list(filter(isval,level))
            if res:
                return res
            level = {s[:i]+s[i+1:] for s in level for i in range(len(s))}
