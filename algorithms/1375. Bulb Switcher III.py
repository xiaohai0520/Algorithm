class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        res = 0
        curmax = 0
        for i, num in enumerate(light):
            curmax = max(curmax,num)
            if i + 1 == curmax:
                res += 1
        return res
