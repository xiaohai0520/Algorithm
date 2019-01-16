class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1,-1]
        l,r = self.search(nums,target),self.search(nums,target)
        while l > 0 and nums[l-1] == target:
            l -= 1
        while r < len(nums) - 1 and nums[r + 1] == target:
            r += 1
        return [l,r]
        
        
#         if not nums:
#             return [-1,-1]
#         low = self.searchl(nums,target)
#         high = self.searchl(nums,target+1)-1
#         if target in nums[low:low+1]:
#             return [low,high]
#         else:
#             return [-1,-1]
        
        
        
#     def searchl(self,nums,target):
#         l = 0
#         r = len(nums) - 1
#         while l <= r:
#             mid = (r - l)//2 + l
#             if nums[mid] < target:
#                 l = mid + 1
#             else:
#                 r = mid - 1
#         return l


    def search(self,nums,target):
        l = 0
        r = len(nums) -1 
        while l <= r:
            mid = (r-l)//2 + l
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return -1
            
    
    
    
