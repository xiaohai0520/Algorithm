class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        ls = list(map(int,list(str(n))))
        r1 = 1
        r2 = 0
        for each in ls:
            r1 *= each
            r2 += each
        return r1 - r2
        
