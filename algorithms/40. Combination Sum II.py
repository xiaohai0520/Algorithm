class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()
        self.dfs(candidates, target, 0, 0,[], res)
        return res

    def dfs(self, nums, target, cursum,index, path, res):
        if cursum > target:
            return 
        if cursum == target:
            res.append(path)
        for i in range(index,len(nums)):
            if i > index and nums[i] == nums[i-1]:
                continue
            self.dfs(nums,target,cursum+nums[i],i+1,path+[nums[i]],res)
