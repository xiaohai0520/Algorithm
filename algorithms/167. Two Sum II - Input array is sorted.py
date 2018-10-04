#two pointers
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        left = 0
        right = len(numbers) - 1
        
        while left < right:
            res = numbers[left] + numbers[right]
            if res == target:
                return [left+1,right+1]
            elif res < target:
                left += 1
            else:
                right -= 1
        
