#try each number and minnus and append the corrsepond char
分别建立数字和字母数组，一一对应
然后从大到小去试剩余的值是否能够满足最大的，如果满足，字符串加上相应的字符，余值减去该数字，直到余值为0



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
