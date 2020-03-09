class Solution:
    def printVertically(self, s: str) -> List[str]:
        res = []
        ls = s.split()
        n = max([len(w) for w in ls])

        i = 0
        while i < n:
            cur = ''
            for w in ls:
                if i < len(w):
                    cur += w[i]
                else:
                    cur += ' '

            res.append(cur.rstrip())
            i += 1
        return res
