class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        
        if len(nums)<=2:
            return False
        
        dic={1:nums[0],2:float('inf')}
        for n in nums[1:]:
            if n>dic[2]:
                return True
            elif dic[2]>n>dic[1]:
                dic[2]=n
            elif n<dic[1]:
                dic[1]=n
        return False
    
#         if len(nums) < 3:
#             return False
#         first = float('inf')
#         second = float('inf')
#         for num in nums:
#             if num < first:
                
#                 first = num

#             elif first < num < second:
#                 second = num
#             elif num > second:
#                 return True
                
#         return False
                
                
