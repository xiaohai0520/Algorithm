class Solution:
    def minCostClimbingStairs(self, cost: 'List[int]') -> 'int':
        if not cost:
            return 0
        if len(cost) < 2:
            return min(cost[0],cost[1])
        cost = cost
        dp = [0] * (len(cost)+1)
        for i in range(2,len(dp)):
            dp[i] = min(dp[i-1] + cost[i-1],dp[i-2] + cost[i-2])
        return dp[-1]
