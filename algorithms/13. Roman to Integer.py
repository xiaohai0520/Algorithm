建立字典，存储字符和数字的关系
遍历字符串中的每一位，
如果前一位比后一位大，则加该数字
如果前一位比后一位小，则见该数字

class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {'I': 1, 'V':5, 'X':10, 'L':50, 'C': 100, 'D':500,'M': 1000}
        res = 0
        for i in range(len(s)-1):
            if dic[s[i]] < dic[s[i+1]]:
                res -= dic[s[i]]
            else:
                res += dic[s[i]]
        return res + dic[s[-1]]
