class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        result, operator, currentNumber, stack = 0, 1, 0, []
        for character in s:
            if character == ' ':
                continue
            elif character.isdigit():
                
                currentNumber = currentNumber*10 + int(character)
            elif character == '(':
               
                stack.append(result)
                stack.append(operator)
               
                operator, result = 1, 0
            elif character == '+':
                
                result += operator*currentNumber
               
                currentNumber = 0
               
                operator = 1
            elif character == '-':
                result += operator*currentNumber
                currentNumber, operator = 0, -1
            elif character == ')':
                result += currentNumber*operator
        
                result *= stack.pop()
               
                result += stack.pop()
                
                currentNumber = 0

       
        if currentNumber:
            result += currentNumber*operator
        return result
            
