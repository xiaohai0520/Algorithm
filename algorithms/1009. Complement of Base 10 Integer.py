This is a bit problem.

We can also solve this problem in math method.

if the % op get 2, means that the last is 0, we add 1 to the result.

else: do nothing

then update the base.

Code:

class Solution:
    def bitwiseComplement(self, N: int) -> int:
        # if N == 0:
        #     return 1
        # cur = bin(N)[2:]
        # res = []
        # for i in cur:
        #     if i == '1':
        #         res.append('0')
        #     else:
        #         res.append('1')
        # return int(''.join(res),2)
        if N == 0:
            return 1
        res = 0
        cur = 1
        while N != 0:
            if N%2 == 0:
                res += cur
            N >>= 1
            # print(N)
            cur <<= 1
            # print(cur)
        return res
