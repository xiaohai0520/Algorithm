#get the first of the last
#the length of the subset


class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        c= collections.Counter(nums)
        degree = max(c.values())
        first,last = {},{}
        for i,num in enumerate(nums):
            first.setdefault(num,i)
            last[num] = i
        return min([last[v] - first[v] + 1 for v in c if c[v] == degree])
        
        
        
#         if not nums:
#             return 0
#         d = self.caldegree(nums)
#         for length in range(1,len(nums)+1):
#             for j in range(len(nums) - length + 1):
#                 if self.caldegree(nums[j:j+length]) == d:
#                     return length
#         return 0
        
          
#     def caldegree(self,nums):
#         dic = {}
#         for num in nums:
#             dic[num] = dic.get(num,0) + 1
#         b = list(dic.values())
#         b.sort()
#         return b[-1]
