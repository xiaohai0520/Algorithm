class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        g = [[0 for _ in range(3)] for _ in range(len(prices)) ]
        l = [[0 for _ in range(3)] for _ in range(len(prices)) ]
        
        for i in range(1,len(prices)):
            diff = prices[i] - prices[i-1]
            for j in range(1,3):
                l[i][j] = max(g[i-1][j-1]+max(diff,0),l[i-1][j]+diff)
                g[i][j] = max(l[i][j],g[i-1][j])
        return g[n-1][2]
