class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dic = {'(':')','[':']','{':'}'}
        stack = []
        for ch in s:
            if ch in dic:
                stack.append(dic[ch])
            else:
                if not stack or ch != stack.pop():
                    return False
        return not stack
