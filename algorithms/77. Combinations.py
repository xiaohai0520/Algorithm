class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if not n:
            return []
        if k == 1:
            return [[i] for i in range(1,n+1)]
        res = []
        def dfs(start,path):
            
            if len(path) == k:
                res.append(path)
                return
            # if start > n - k:
            #     return
            for i in range(start,n+1):
                dfs(i+1,path+[i])
        dfs(1,[])
        return res
