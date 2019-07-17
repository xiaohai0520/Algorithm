class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        res = []
        
        def dfs(path, cur, biggest): 
            if path:
                res.append(path + [cur])
            for i in range(biggest,int(math.sqrt(cur)) + 1):
                if cur % i == 0:
                    dfs(path + [i], cur//i, i)
            

        dfs([], n, 2)
        return res
        
        
        
        
        
        
        
        
        
