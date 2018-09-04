#try each number and minnus and append the corrsepond char

class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
        numerals = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
        res = ''
        for i in range(len(values)):
            while num >= values[i]:
                num -= values[i]
                res += numerals[i]
        return res
