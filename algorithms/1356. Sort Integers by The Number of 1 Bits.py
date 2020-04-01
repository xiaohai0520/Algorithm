class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def count_one(n):
            res = 0
            while n:
                res += n & 1
                n = n >> 1
            return res
        arr.sort(key = lambda x:(count_one(x),x))
        return arr
