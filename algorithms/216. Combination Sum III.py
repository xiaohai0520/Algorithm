class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        nums = [x for x in range(1,10)]
        res = []
        self.dfs(k,n,0,[],res,nums)
        return res
        
    def dfs(self,k,target,start,path,res,nums):
        if k == 0 and sum(path) == target:
            res.append(path)
            return
        if k < 0 or sum(path) > target:
            return
        for i in range(start,len(nums)):
            self.dfs(k-1,target,i+1,path+[nums[i]],res,nums)
        
        
    
