class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        res = ''
        la = list(a)
        lb = list(b)
        carry = 0
        
        while la or lb:
            cura = curb = 0
            if la:
                cura = int(la.pop())
                
            if lb:
                curb = int(lb.pop())
            
            cur = (cura + curb + carry)%2
            carry = (cura + curb + carry)//2
            
            res = str(cur) + res
        if carry:
            res = '1' + res
        return res
            
