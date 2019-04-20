union find algorithm.

Make the union find structure first. 

we do the union when  ==

find each != in the array.


Code：
def find(x):
            if x != uf[x]: uf[x] = find(uf[x])
            return uf[x]
        uf = {a: a for a in string.ascii_lowercase}
        for a, e, _, b in equations:
            if e == "=":
                uf[find(a)] = find(b)
        return not any(e == "!" and find(a) == find(b) for a, e, _, b in equations)
    
    
    
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        
        dic = {i:set([i]) for i in string.ascii_lowercase}
        
        
        def union(v1,v2):
            k1 = find(v1)
            k2 = find(v2)
            # print(k1,k2)
            if k1 != k2:
                dic[k1] = dic[k1].union(dic[k2])
            
            # dic[k1].update(dic[k2])
            # print(dic[k1])
                del dic[k2]

            
        def find(v):
            for key,values in dic.items():
                
                if v in values:
                    return key
        
        for e in equations:
            if e[1] == '=' and e[0] != e[3]:
                union(e[0],e[3])
        for e in equations:
            if e[1] == '!':
                k1 = find(e[0])
                k2 = find(e[3])
                if k1 == k2:
                    return False
        return True
        
