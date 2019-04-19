This is a dfs and graph and math problem.

We need to sort the array first to delete the duplicate.

Then think it is a dfs problme, try to dfs the next pair which sum is a perfect square.


Code:
    
import math

class Solution:
    def numSquarefulPerms(self, A: List[int]) -> int:
        A.sort()
        self.res = 0
        
        
        
               
        def check(integer):
            root = int(math.sqrt(integer))
            if root ** 2 == integer: 
                return True
            else:
                return False
        
        def dfs(pre,nums):
            if not nums:
                self.res += 1
                return
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                cur = pre + nums[i]
                if check(cur):
                    dfs(nums[i],nums[:i]+nums[i+1:])
         
        

        
        
        for i in range(len(A)):
            if i > 0 and A[i] == A[i-1]:
                continue
            pre = A[i]
            dfs(pre,A[:i]+A[i+1:])
        
        
        return self.res
    
        
