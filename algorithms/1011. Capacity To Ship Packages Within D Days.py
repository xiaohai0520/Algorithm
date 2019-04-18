This is a binary search problem.

weight is the target, we use the binary search to try the different weight.

For each weight, we just calculate the days.

For binary search, the l is the lower boundry.


code:
class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        if not weights:
            return 0
        l,r = max(weights),sum(weights)
        while l < r:
            # print(l,r)
            mid = (l + r)//2
            # print(mid)
            days = 1
            cur = 0
            for w in weights:
                if cur + w <= mid:
                    cur += w
                else:
                    cur = w
                    days += 1
            
             
            if days > D:
                l = mid + 1
            else:
                r = mid
              
        return l
