# presum use dic to save the times
#like two sum

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dic = {0:1}
        pre_sum = 0
        res = 0
        for num in nums:
            pre_sum += num
            res += dic.get(pre_sum - k,0)
            dic[pre_sum] = dic.get(pre_sum,0) +1
        return res
