class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        # sort array from large to small
        arr.sort(reverse=True)
        max_val = arr[0]
        
        # Iterate all elements, exit when largest value for sum equal to target found
        while arr and target > arr[-1] * len(arr):
            target -= arr.pop()
        
        # Divide remaining target by remaining length of array
        ans = int(target / len(arr) + 0.49)
        return ans
        
        
        
#         l, h = 0, max(arr)
#         def mySum(val):
#             return sum(min(a, val) for a in arr)
#         while l < h:
#             m = (l + h) // 2
#             if mySum(m) < target:
#                 l = m + 1
#             else:
#                 h = m
#         return min(l - 1, l, l + 1, key=lambda x: abs(mySum(x) - target))
        
