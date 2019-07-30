class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        if not words:
            return 0
        res = 0
        ls = [0] * len(words)
        for i in range(len(words)):
            for c in set(words[i]):
                ls[i] |= 1 << (ord(c) - ord('a'))
            for j in range(i):
                if not (ls[j] & ls[i]):
                    res = max(res,len(words[i]) * len(words[j]))
        return res
