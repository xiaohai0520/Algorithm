class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        res = 0
        dic = collections.defaultdict(int)
        l = 0
        for r in range(len(s)):
            dic[s[r]] += 1
            if len(dic) <= k:
                res = max(res,r-l+1)
            else:
                while len(dic) > k:
                    dic[s[l]] -= 1
                    
                    if dic[s[l]] == 0:
                        del dic[s[l]]
                    l += 1
        return res
