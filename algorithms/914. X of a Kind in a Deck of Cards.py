from math import gcd
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        if not deck or len(deck) < 2:
            return False
        dic = collections.Counter(deck)
        
        v = list(dic.values())
        
        g = v[0]
#         for i in range(2,len(deck)+1):
#             if all([j%i == 0 for j in v]):
#                 return True
#         return False
        for i in range(1,len(v)):
            g = gcd(g,v[i])
        return g >= 2
        
