This is a dp problem.

We make a dp length equal days[-1]

for each in dp.

we compare the three methods take the minimum one.


CODE:

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        if len(days) == 1:
            return costs[0]
        dp = [0] * (days[-1] + 1)
        check = set(days)
        for i in range(1,days[-1]+1):
            if i not in check:
                dp[i] = dp[i-1]
            else:
                dp[i] = min(dp[max(0,i-1)]+costs[0],dp[max(0,i-7)]+costs[1],dp[max(0,i-30)]+costs[2])

        return dp[-1]
        
