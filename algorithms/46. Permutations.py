dfs 或者 bfs，
dfs每次取数组第n个数字，然后去掉此数字，组成新的数组，继续dfs,
bfs 用每个数字去组合调用自己本身的结果

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        res = []
        
        def dfs(path,nums):
            if not nums:
                res.append(path)
                return
            for i in range(len(nums)):
                dfs(path+[nums[i]],nums[:i] + nums[i+1:])
                
        dfs([],nums)
        return res

            
