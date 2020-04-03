class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        l = len(arr)
        counter = collections.Counter(arr)
        cur = 0
        res = 0
        for n in sorted(list(counter.keys()),key=lambda x:-counter[x]):
            cur += counter[n]
            res += 1
            if cur >= l//2:
                return res
        return res
