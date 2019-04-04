class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        res = 0
        pre = 0
        re = [1] + [0] * (K - 1)
        for a in A:
            pre += a
            r = pre%K
            res += re[r]
            re[r] += 1
        return res
