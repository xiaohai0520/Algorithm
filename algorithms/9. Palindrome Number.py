# tostring or use // and % from last digit to first one



class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # return str(x) == str(x)[::-1]
        
        if x < 0:
            return False
        
        temp = x
        res = 0
        while temp > 0:
            reminder = temp // 10
            lastdigit = temp % 10
            res = res * 10 + lastdigit
            temp = reminder
        return res == x
