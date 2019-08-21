class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k == 0:
            return s
        h = [(-freq, ch) for (ch, freq) in collections.Counter(s).items()]
        heapq.heapify(h)
        res = []
        while len(res) < len(s):
            q = []
            for _ in range(k):
                if len(res) == len(s):
                    return ''.join(res)
                if not h:
                    return ''
                freq, ch = heapq.heappop(h)
                res.append(ch)
                if freq < -1:
                    q.append((freq+1, ch))
            while q:
                heapq.heappush(h, q.pop())
        return ''.join(res)
