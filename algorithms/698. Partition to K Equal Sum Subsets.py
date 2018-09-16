#dfs


class Solution:
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        def dfs(A,target,step,num,k):
            if step==k-1:         # if previous k-1 subset has the average value, then the sum of the rest must be the average
                return True
            n=len(A)
            for i in range(n):
                B=A[:i]+A[i+1:]
                if num+A[i]==target:
                    if dfs(B,target,step+1,0,k):  # if sum of previous number and current number is the average, the step plus 1, 
                        return True
                elif num+A[i]<target:
                    if dfs(B,target,step,num+A[i],k):
                        return True
                elif A[i] > target: return False  #if any single num is great than the average, return false immediately
            return False

        n,total=len(nums),sum(nums)
        if total%k!=0: return False
        target=total/k
        nums.sort(reverse=True)     # reverse  sort to check bigest number first
        res=dfs(nums,target,0,0,k)
        return res
        
