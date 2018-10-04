#dfs

class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()
        self.dfs(candidates, target, 0,0, [], res)
        return res

    def dfs(self, nums, target, cursum,index, path, res):
        
        if cursum > target:
            return
        if cursum == target:
            res.append(path)
        for i in range(index,len(nums)):
            self.dfs(nums,target,cursum + nums[i] , i, path + [nums[i]],res)
