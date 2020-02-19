class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr) == 1:
            return [-1]
        
        res = [arr[-1]] * len(arr)
        
        for i in range(len(arr)-2,-1,-1):
            res[i] = max(arr[i+1],res[i+1])
        res[-1] = -1
        return res
        
