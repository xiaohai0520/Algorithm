class Solution:
    def hIndex(self, citations: List[int]) -> int:
        N = len(citations)
        low, high = 0, N - 1

        while low < high:
            mid = low + (high - low) // 2
            if citations[mid] < N - mid:
                low = mid + 1
            else:
                high = mid

        return N - low if N > 0 and citations[low] >= N - low else 0
