class Solution:
    def minSteps(self, s: str, t: str) -> int:
        dic1 = collections.Counter(s)
        dic2 = collections.Counter(t)
        
        for ch in dic1:
            if dic1[ch] >= dic2[ch]:
                dic1[ch] -= dic2[ch]
            else:
                dic1[ch] = 0
        return sum(list(dic1.values()))
