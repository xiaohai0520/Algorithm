跟39 思想一致，只是需要判断下是否含有重复的情况

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        candidates.sort()
        res = []
        
        def dfs(path,cur,start):
            if cur > target:
                return
            if cur == target:
                res.append(path)
                return
            for i in range(start,len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                dfs(path+[candidates[i]],cur+candidates[i],i+1)
        dfs([],0,0)
        return res
