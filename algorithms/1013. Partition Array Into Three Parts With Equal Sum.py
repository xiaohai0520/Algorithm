Array problem.

We just need to make sure if can be divided by 3

Then try to iterate the array and find the three part.

Code:
class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        if not A:
            return False
        if sum(A)%3 != 0:
            return False
        res = sum(A)//3
        cur = 0
        j = 0
        for i in range(len(A)):
            cur += A[i]
            if cur == res:
                j += 1
                cur = 0
            if j == 2 and i != len(A)-1:
                return True
        return False
        
