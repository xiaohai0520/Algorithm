class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:

        past = set()
        queue = collections.deque([start])
        while queue:
            i = queue.popleft()
            #print(i)
            if arr[i] == 0:
                return True
            past.add(i)
            cur = i - arr[i]
            if cur >= 0 and cur not in past:
                queue.append(cur)
            cur = i + arr[i]
            if cur < len(arr) and cur not in past:
                queue.append(cur)
        return False
