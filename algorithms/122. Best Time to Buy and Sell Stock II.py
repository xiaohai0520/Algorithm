#if later > early, profir++ 

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        maxp = 0
        # start = prices[0]
        # for i in range(len(prices)):
        #     if prices[i] > start:
        #         maxp += (prices[i] - start)
        #         start = prices[i]
        #     else:
        #         start = prices[i]
        # return maxp
        
        for i in range(len(prices)-1):
            if prices[i+1] - prices[i] > 0:
                maxp += prices[i+1] - prices[i]
        return maxp
