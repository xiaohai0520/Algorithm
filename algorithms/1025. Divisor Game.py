This is a dp problem.

The dp array use to record every number can win or not win.

We from 1 to N, for each number try every step from 1 to i//2, if satify the condition, we change the dp[i] to True.

For these problem, always need the previous state to check. so it is dp.


Code:
class Solution:
    def divisorGame(self, N: int) -> bool:
        dp = [False] *(N+1)
        for i in range(1,N+1):
            for j in range(1,i//2+1):
                if i % j == 0 and not dp[i-j]:
                    dp[i] = True
                    break
        return dp[-1]
