class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        stack1 = []
        stack2 = []
        res = []
        for n in num1:
            stack1.append(n)
        for n in num2:
            stack2.append(n)
        carry = 0
        while stack1 or stack2:
            n1 = n2 = 0
            if stack1:
                n1 = int(stack1.pop())
            if stack2:
                n2 = int(stack2.pop())
            
            carry,cur = divmod(n1+n2+carry,10) 
            res.append(cur)
        if carry:
            res.append(1)
        return ''.join(map(str,res[::-1]))
        
