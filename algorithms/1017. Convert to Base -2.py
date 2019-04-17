This is a bit operate problem.

Two thing need to remember, first  N & 1 will get the last digit of the bit number, second thing is N >> 1 means //2

So we need to get last digit every time and right slide.

For base is -2, we only need to get the -(N>>1) each time.

code:
class Solution:
    def baseNeg2(self, N: int) -> str:
        if N == 0:
            return '0'
        res = []
        while N:
            res.append(N&1)
            N = -(N>>1)
        return ''.join(list(map(str,res[::-1])))
            
