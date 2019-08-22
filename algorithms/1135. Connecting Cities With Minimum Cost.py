class Solution:
    def minimumCost(self, N: int, connections: List[List[int]]) -> int:
        uf = {i:i for i in range(1,N+1)}
        
        def find(x):
            if uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]
        def union(x,y):
            if find(x) == find(y):
                return False
            uf[find(x)] = find(y)
            return True
        
        con = connections
        con.sort(key=lambda x:x[2])
        res = 0
        for i,j,v in con:
            if union(i,j):
                res += v
        return res if len(set(find(i) for i in range(1,N+1)))==1 else -1 
