class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        mem = set()
        while n != 1:
            cur = 0
            while n != 0:
                cur += (n%10)**2
                n = n//10
            n = cur
            if cur in mem:
                return False
            else:
                mem.add(cur)
        return True
