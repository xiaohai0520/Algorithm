class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = 1
        if x < 0:
            flag = 0
        x = abs(x)
        res = 0
        while x > 0:
            q = x // 10
            reminder = x % 10
            res = res * 10 + reminder
            x = q
        
        if res > 2**31 -1 or res < -2**31:
            return 0
        return res if flag else -res
