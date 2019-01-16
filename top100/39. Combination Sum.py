class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates:
            return []
        candidates.sort()
        res = []
        self.dfs(candidates,target,0,[],res)
        return res
        
        
        
    def dfs(self,nums,target,index,path,res):
        if target == 0:
            res.append(path)
        for i in range(index,len(nums)):
            if nums[i] <= target:
                self.dfs(nums,target-nums[i],i,path+[nums[i]],res)
