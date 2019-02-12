import heapq
from collections import Counter
class Solution:
    def reorganizeString(self, S: 'str') -> 'str':
        res = ""
        pq = []
        c = Counter(S)
        for key, value in c.items():
            heapq.heappush(pq, (-value, key))
        p_a, p_b = 0, ''
        while pq:
            a, b = heapq.heappop(pq)
            res += b
            if p_a < 0:
                heapq.heappush(pq, (p_a, p_b))
            a += 1
            p_a, p_b = a, b

        if len(res) != len(S): return ""
        return res
