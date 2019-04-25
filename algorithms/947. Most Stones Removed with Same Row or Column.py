UNION FIND PORBLEM

union we need to set the original x y into the container.

find is import, if x !=UF[x]   UF[x] = find(UF[x])  return UF[x]


class Solution:
    
    
    
    def removeStones(self, stones: List[List[int]]) -> int:
        #union find
        UF= {}
        def find(x):
            if x != UF[x]:
                UF[x] = find(UF[x])
            return UF[x]
        
        def union(x,y):
            UF.setdefault(x,x)
            UF.setdefault(y,y)
            UF[find(x)] = find(y)
            
        for i,j in stones:
            union(i,-j-1)
        return len(stones) - len({find(x) for x in UF})
