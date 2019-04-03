class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        if not A:
            return []
        left, right = [a for a in A if a < 0],[a for a in A if a >= 0]
        left = left[::-1]
        res = []
        while left and right:
            if abs(left[-1]) > abs(right[-1]):
                res.append(left.pop())
            else:
                res.append(right.pop())
        if left:
            res.extend(left[::-1])
        if right:
            res.extend(right[::-1])
        
        return list(map(lambda x:x*x,res))[::-1]
