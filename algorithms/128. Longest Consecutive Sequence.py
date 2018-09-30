#iterate each num in the array and use dic to save the length
#length = left + right + 1
#after update the position then updata left and right


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        dic = {}
        for num in nums:
            if num not in dic:
                left = dic.get(num-1,0)
                right = dic.get(num+1,0)
                
                cur = left + right + 1
                dic[num] = cur
                
                res = max(res,cur)
                
                dic[num-left] = cur
                dic[num + right] = cur
                
        return res
