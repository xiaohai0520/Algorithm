#use the stack ,if + insert  if * or / pop cal and insert again


class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack,sign,num = [],'+',0
        s = s + ' '
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + ord(s[i]) - ord('0')
            elif (not s[i].isdigit() and s[i] != ' ') or i == len(s) - 1:
                if sign == '-':
                    stack.append(-num)
                elif sign == '+':
                    stack.append(num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                else:
                    stack.append(int(stack.pop() / num))
                
                sign = s[i]
                num = 0
        return sum(stack)
