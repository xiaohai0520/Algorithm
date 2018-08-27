#use stack
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dic = {
            "[": "]",
            "{": "}",
            "(": ")"
        }
        stack = []
        
        for c in s:
            if c in dic:
                stack.append(dic[c])
            elif len(stack) == 0 or stack.pop() != c:
                return False
            
        return len(stack) == 0
