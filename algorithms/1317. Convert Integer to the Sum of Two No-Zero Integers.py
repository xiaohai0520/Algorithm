class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        i = 1
        while 1:
            cur = n - i
            s1 = set(list(str(i)))
            s2 = set(list(str(cur)))
            if '0' not in s1 and '0' not in s2:
                return [i,cur]
            i += 1
