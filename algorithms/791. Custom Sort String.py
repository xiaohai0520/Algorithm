class Solution:
    def customSortString(self, S: str, T: str) -> str:
        dic = collections.Counter(T)
        res = ''
        for ch in S:
            if ch in dic:
                res += ch*dic[ch]
                

                del dic[ch]
        
        for ch in string.ascii_lowercase:
            if ch in dic:
                res += ch * dic[ch]
        return res
