Greedy problem.

our startegy is minus small and add large.

if our power is enough, we add the small power to add 1 point.

if we power is not enough, we can add the large power nad minus 1 point.

each time try to get the max point.

code:


class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        tokens.sort()
        queue = collections.deque(tokens)
        cur = 0
        res = 0
        while queue and (queue[0] <= P or cur > 0):
            if queue[0] <= P:
                P -= queue.popleft()
                cur += 1
            else:
                P += queue.pop()
                cur -= 1
            res = max(res,cur)
        return res
