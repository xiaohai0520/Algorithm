class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        if not num:
            return True
        dic = {'0':'0','1':'1','6':'9','8':'8','9':'6'}
        
        res = ''
        for ch in num[::-1]:
            if ch in dic:
                res += dic[ch]
            else:
                return False
        return num == res
