class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold = float('-inf')
        rest = sold = 0

        for p in prices:
            # pre_sold = sold
            sold ,hold ,rest= hold + p, max(hold,rest - p),max(rest,sold)
            
           
        return max(rest,sold)
