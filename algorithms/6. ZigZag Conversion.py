# zigzag 分割字符串，
# 我们考虑每 2* 行数 - 2 个长度为一个循环， 其中前一部分为正序，后一部分为倒叙。
# 建立 长度为 行数的数组，然后遍历整个字符串， 求每个字符 应该在的index,  放入相应的index中。
# 最后将数组中所有的字符串加在一起。


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if not s:
            return ''
        if numRows == 1:
            return s
        res = [''] * numRows
        circle = 2*(numRows-1)
        
        for i,c in enumerate(s):
            r = i % circle
            if r <= numRows - 1:
                res[r] += c
            else:
                res[circle-r] += c
        return ''.join(res)
                
