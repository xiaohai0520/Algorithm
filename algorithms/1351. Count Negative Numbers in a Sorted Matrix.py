class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        return sum([self.binary_search(arr) for arr in grid])
        
    def binary_search(self, arr):
        start, end = 0, len(arr) - 1
        while start <= end:
            mid = (start + end) // 2
            if arr[mid] < 0:
                end = mid - 1
            else: 
                start = mid + 1
        return len(arr) - start
