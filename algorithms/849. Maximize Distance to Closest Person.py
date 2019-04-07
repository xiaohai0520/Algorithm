class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        res, i, j = 0, 0, 0
        for j in range(len(seats)):
            if 1 == seats[j]:
                res = max(res, j) if 0 == i else max(res, (j - i + 1) >> 1)
                i = j + 1
        return max(res, len(seats) - i)
