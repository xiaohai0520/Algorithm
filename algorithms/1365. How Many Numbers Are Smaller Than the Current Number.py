class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        d = {}
        for i, n in enumerate(sorted(nums)):
            if n not in d:
                d[n] = i
                
        return [d[n] for n in nums]
        
        
        
        
        
        
        
        
#         Count = collections.Counter(nums)
#         ls = sorted(list(set(nums)))
#         dic = {}
#         for i,each in enumerate(ls):
#             if i == 0:
#                 dic[each] = 0
#             else:
#                 dic[each] = dic[ls[i-1]] + Count[ls[i-1]]
        
#         for i,num in enumerate(nums):
#             nums[i] = dic[num]
#         return nums
                
            
