This is an array problem.

We sort the array first, we know the first one we do not need to change.

From the second one, use update the need(n)  we want to step by step to update the n but it also depend on the next n.



class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        if not A:
            return 0
        A.sort()
        n = A[0]
        res = 0
        for i in range(1,len(A)):
            n = max(n+1,A[i])
            res += n - A[i]
        return res
