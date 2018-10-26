class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = 0
        base = 1
        for i, c in enumerate(reversed(s)):
            curr = (ord(c) - ord('A') + 1) * base
            total += curr
            base *= 26
        return total
