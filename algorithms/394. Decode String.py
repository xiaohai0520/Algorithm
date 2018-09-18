#use stack, if num record if isalp plus together if [ add cur and num, if ] pop out and get together

class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []; curNum = 0; curString = ''
        for c in s:
            if c == '[':
                stack.append(curString)
                stack.append(curNum)
                curString = ''
                curNum = 0
            elif c == ']':
                num = stack.pop()
                prevString = stack.pop()
                curString = prevString + num*curString
            elif c.isdigit():
                curNum = curNum*10 + int(c)
            else:
                curString += c
        return curString
