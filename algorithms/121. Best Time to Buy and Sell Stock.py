#find the minprice all the round

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        minPri, maxPro = prices[0],0
        for price in prices[1:]:
            minPri = min(price, minPri)
            maxPro = max(maxPro, price - minPri)
        return maxPro
