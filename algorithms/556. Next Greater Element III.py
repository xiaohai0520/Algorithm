#2**31 -1 
class Solution:
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        ls = [x for x in str(n)]
        sign = len(ls) - 1
        for i in range(len(ls)-1,0,-1):
            if ls[i-1] < ls[i]:
                sign = i-1
                break
        if sign == len(ls) - 1 :
            return -1
        mark = 0
        for i in range(len(ls)-1,-1,-1):
            if ls[i] > ls[sign]:
                mark = i
                break
        ls[sign],ls[mark] = ls[mark],ls[sign]
        
        l,r = sign + 1,len(ls)-1
        while l < r:
            ls[l],ls[r] = ls[r],ls[l]
            l += 1
            r -= 1
        return int(''.join(ls)) if int(''.join(ls)) < 2**31 -1 else -1
    
