class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        if m==0 or m==n:
            return m
        count = 0
        while m != n:
            m >>= 1 
            n >>= 1
            count += 1
        return m << count
        
