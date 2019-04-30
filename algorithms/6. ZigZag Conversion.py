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
                
