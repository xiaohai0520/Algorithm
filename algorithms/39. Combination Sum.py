每个数字可以重复使用，并且没有重复的数字，
我们使用dfs去尝试每种组合，并记录当前的和，
如果和大于目标值，直接返回上一步
如果等于，加入结果集
小于的话，从当前数字继续添加进path

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        candidates.sort()
        res = []
        
        def dfs(cur,path,start):
            if cur > target:
                return
            if cur == target:
                res.append(path)
                return
            for i in range(start,len(candidates)):
                dfs(cur+candidates[i],path+[candidates[i]],i)
        
        dfs(0,[],0)
        return res
