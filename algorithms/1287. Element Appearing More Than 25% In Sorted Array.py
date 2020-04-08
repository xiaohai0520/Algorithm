class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        w = len(arr) // 4 + 1
        for i in range(len(arr)):
            if arr[i] == arr[i+w-1]:
                return arr[i]
