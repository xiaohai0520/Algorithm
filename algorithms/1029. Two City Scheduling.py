This is a greedy question.

We need to sorted the diff between the two cities.

If we sorted by A-B

We all front half of A then rest are B.

Code:

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        cur = []
        for cost in costs:
            cur.append([cost[0],cost[1],cost[0]-cost[1]])
        cur.sort(key=lambda x:x[2])
        res = 0
        for i in range(len(costs)):
            if i < len(costs)//2:
                res += cur[i][0]
            else:
                res += cur[i][1]
        return res
