# use dp to save each largest one

class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        #O(1) space
        
        curSum = maxSum = nums[0]
        for num in nums[1:]:
            curSum = max(num, curSum + num)
            maxSum = max(maxSum, curSum)
        return maxSum
        
        #O(n) space
        dp = [nums[0] for i in range(len(nums))]
        res = nums[0]
        for i in range(1,len(nums)):
            dp[i] = max(dp[i-1] + nums[i], nums[i])
            res = max(dp[i],res)
        return res
        
        # another O(n) space  remember every max value
        dp = [nums[0] for i in range(len(nums))]
        cursum = nums[0]
        for i in range(1,len(nums)):
            cursum = max(cursum+nums[i],nums[i])
            dp[i] = max(cursum,dp[i-1])
        return dp[-1]
           
        
        #divide and conquer
        return self.helper(nums,0,len(nums)-1)
        
        
    def helper(self,nums,left,right):
        if left == right:
            return nums[left]
        mid = (left + right) // 2
        
        suml = leftsum = nums[mid]
        for i in range(mid -1,left -1,-1):
            suml += nums[i]
            leftsum = max(leftsum,suml)
            
        sumr = rightsum = nums[mid+1]
        for i in range(mid+2,right+1):
            sumr += nums[i]
            rightsum = max(rightsum,sumr)
        
        leftmax = self.helper(nums,left,mid)
        rightmax = self.helper(nums,mid+1,right)
        
        return max(leftmax,rightmax,(leftsum + rightsum))      
            
            
        
