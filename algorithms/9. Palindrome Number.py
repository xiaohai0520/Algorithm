# tostring or use // and % from last digit to first one
# 这道题基本思想是考数字的变换，如果数字小于0， 那一定不是palindrome。
# 然后将数字进行 翻转， 每次除以10， 用余数去构造翻转后的数， divmod  方法可以同时获得两个部分。
# 最后将结果进行比较就可以， 如果相等 则说明是palindrome。


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
