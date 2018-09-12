from collections import defaultdict, deque
class Solution:
    def killProcess(self, pid, ppid, kill):
        d, q, res = defaultdict(list), deque([kill]), []
        for parent, child in zip(ppid, pid):
            d[parent].append(child)
        while q:
            parent = q.popleft()
            res.append(parent)
            q.extend(d[parent])
        return res
