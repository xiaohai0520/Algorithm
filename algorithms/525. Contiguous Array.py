class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        res = 0
        dic = {0:-1}
        count = 0
        for i , num in enumerate(nums):
            if num == 0:
                count -= 1
            else:
                count += 1
            
            if count in dic:
                res = max(res,i-dic[count])
            else:
                dic[count] = i
        return res
