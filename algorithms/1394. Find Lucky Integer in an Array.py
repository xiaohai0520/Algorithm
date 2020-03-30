import collections
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        dic = collections.Counter(arr)
        res = -1
        for k,v in dic.items():
            if k == v:
                res = max(k,res)
        return res
