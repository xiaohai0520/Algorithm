# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """   
        res, n = [], newInterval
        for index, i in enumerate(intervals):
            if i.end < n.start:
                res.append(i)
            elif n.end < i.start:
                res.append(n)
                return res+intervals[index:] 
            else:  # overlap case
                n.start = min(n.start, i.start)
                n.end = max(n.end, i.end)
        res.append(n)
        return res
        
