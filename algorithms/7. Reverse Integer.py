# 反正数字，先判断数字的正负号，然后取绝对值。
# 设置res = 0, 使用divmod方程，逐渐的获得最后一位。
# 返回时注意integer的范围。

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
