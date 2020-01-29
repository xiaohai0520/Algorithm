class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s:
            return 0
        s = s.strip(' ')
        ls = s.split(' ')
        if not ls:
            return 0
        return len(ls[-1])
