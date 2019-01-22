class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        res = 0
        s = set(nums)
        
        for num in nums:
            if (num - 1) not in s:
                curlength = 1
                curnum = num
                while (curnum + 1) in s:
                    curlength += 1
                    curnum += 1
                res = max(res,curlength)
        return res
                
        
        
#         res = 0
#         dic = {}
#         for num in nums:
#             if num not in dic:
#                 left = dic.get(num-1,0)
#                 right = dic.get(num+1,0)
                
#                 cur = left + right + 1
#                 dic[num] = cur
                
#                 res = max(res,cur)
                
#                 dic[num-left] = cur
#                 dic[num + right] = cur
                
#         return res
