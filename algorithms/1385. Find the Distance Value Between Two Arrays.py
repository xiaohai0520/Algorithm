class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        res = 0
        for num1 in arr1:
            for num2 in arr2:
                if abs(num1 - num2) <= d:
                    res += 1
                    break 
        return len(arr1) - res
