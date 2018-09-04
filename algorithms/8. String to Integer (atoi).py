


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
