class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if k > len(s):
            return False
        dic = collections.Counter(s)
        c = 0
        for key in dic:
            if dic[key] %2 != 0:
                c += 1
        #print(c,k)
        if c > k:
            return False
        return True
        
