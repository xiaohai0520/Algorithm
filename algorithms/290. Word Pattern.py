class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        ls = list(str.split(' '))
        print(ls)
        if len(ls) != len(pattern):
            return False
        return len(set(zip(pattern,ls))) == len(set(list(pattern))) == len(set(ls))
