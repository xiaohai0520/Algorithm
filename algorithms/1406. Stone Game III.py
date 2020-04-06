class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        a = stoneValue
        n = len(a)
        f = [float('-inf')]*n
        for _ in range(3):
            a.append(0)
            f.append(0)
        for i in range(n-1, -1, -1):
            s = 0
            for j in range(3):

                s += a[i+j]
                f[i] = max(f[i], s - f[i+j+1])
        if f[0] > 0: return 'Alice'
        if f[0] < 0: return 'Bob'
        return 'Tie'
