class Solution:
    def clumsy(self, N: int) -> int:
        if N <= 2:
            return N
        if N == 3:
            return 6
        t,r = divmod(N,4)
        res = 0
        for i in range(t):
            cur = N * (N-1) // (N-2) 
            if i == 0:
                res += cur
            else:
                res -= cur
            res += N - 3
            N -= 4
        if r == 1:
            cur = N
        elif r == 2:
            cur = N * (N-1)
        else:
            cur = N * (N-1)//(N-2)
        return res - cur
