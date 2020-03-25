class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        return set(min(r) for r in matrix) & set(max(c) for c in zip(*matrix))
