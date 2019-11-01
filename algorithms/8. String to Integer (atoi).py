# 先去掉左右两边的空格，如果此时长度为0 则返回0
# 判断第一位是否是符号，如果是+ 或者 - ， 怎么记录符号，并且删除第一位。
# 判断每一位是否是数字，然后累加数字直到不是数字为止。
# 判断数字是否在整数的范围内，如果超过则返回上下边界，未超过则返回结果。


class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """

        ls = list(str.strip())
        if not ls or len(ls) == 0:
            return 0
        sign = -1 if ls[0] == '-' else 1
        if ls[0] in ['-','+']: del ls[0]
        i,res = 0,0
        while i < len(ls) and ls[i].isdigit():
            res = res * 10 + int(ls[i])
            i += 1
        return max(-2**31,min(res*sign,2**31 - 1))
