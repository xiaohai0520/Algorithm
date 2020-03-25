class Solution:
    def longestPrefix(self, s: str) -> str:
        prefix,suffix=s[:-1],s[1:]
        while prefix and suffix and prefix!=suffix:
            prefix=prefix[:-1]
            suffix =suffix[1:]
        return prefix
