#try to find the first number decrease 
#swap with the first number larger than this one
#then swap the back numbers

class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return 
     
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
 
        if i == -1:
            self.swap(nums,0,len(nums)-1)
            return
        
        j = len(nums) - 1
        
        while j >= 0 and nums[j] <= nums[i]:
            j -= 1
        nums[i],nums[j] = nums[j],nums[i]
        self.swap(nums,i+1,len(nums)-1)
        
            
            
    def swap(self,nums,left,right):
        while left < right:
            nums[left], nums[right] = nums[right],nums[left]
            left += 1
            right -= 1
        
