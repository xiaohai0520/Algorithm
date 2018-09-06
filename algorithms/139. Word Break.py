#use dp and check previous word is true and cur one is in dic
#the last one in list is answer


class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        d = [False] * len(s)    
        for i in range(len(s)):
            for w in wordDict:
                if w == s[i-len(w)+1:i+1] and (d[i-len(w)] or i-len(w) == -1):
                    d[i] = True
        return d[-1]
