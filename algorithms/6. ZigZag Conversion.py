class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if not s:
            return ''
        if numRows == 1:
            return s
        res = ''
        for i in range(numRows):
            
            j = i
            
            if i != numRows - 1 and i != 0:
                while j < len(s):
                    res += s[j]
                    j = j + 2 + (numRows - i - 2) * 2
                    if j < len(s):
                        res += s[j]
                        j = j + 2 * (i - 1) + 2
                    else:
                        break
                    
            else:
                while j < len(s):
                    res += s[j]
                    j = j + 2 * (numRows - 2) + 2
        return res
                    

                
