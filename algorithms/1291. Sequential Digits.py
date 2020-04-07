class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = []
        
        for i in range(1,10):
            cur = 0
            for j in range(i,10):
                cur = cur * 10 + j
                
                if low <= cur <= high:
                    res.append(cur)
        return sorted(res)
