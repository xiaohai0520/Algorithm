class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        a,b,c = sorted([a,b,c])
        m1 = m2 = 0
        if b-a == 1 and c-b == 1:
            m1 = 0
        elif b -a > 2 and c -b > 2:
            m1 = 2
        else:
            m1 = 1
        m2 = c - a -2
        return [m1,m2]
