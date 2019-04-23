This is a stack problem.

When we want to save the previous most min point, another choice is use the stack

We can save the decrease array in the stack

and check from tail to head compare with the stack[-1]

code:

class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        stack = []
        res = 0
        for i, elem in enumerate(A):
            if not stack or A[stack[-1]] > elem:
                stack.append(i)
        for j in range(len(A) - 1, -1, -1):
            while stack and A[stack[-1]] <= A[j]:
                res = max(res, j - stack.pop())
        return res
        # cur = [(a,i) for i,a in enumerate(A)]
        # cur.sort()
        # imin = float('inf')
        # res = 0
        # for a,i in cur:
        #     res = max(res,i-imin)
        #     imin = min(i,imin)
        # return res
