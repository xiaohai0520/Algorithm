class Solution:
    def largeGroupPositions(self, S: str) -> List[List[int]]:
        res = []

        start = end = 0
        while start < len(S):
            while end < len(S) and S[end] == S[start]:
                end += 1
            if end - start >=3:
                res.append((start,end-1))
            start = end
        return res
