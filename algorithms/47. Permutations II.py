dfs 每次递归之前 判断一下是否和前置位重复

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums:return
        
        nums.sort()
        res = []
        def dfs(nums,path):
            if not nums:
                res.append(path)
                return
            for i in range(len(nums)):
                if i > 0 and nums[i-1] == nums[i]:
                    continue
                dfs(nums[:i] + nums[i+1:],path+[nums[i]])
        dfs(nums,[])
        return res
