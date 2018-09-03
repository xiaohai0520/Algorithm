#sort and try each one after the first one

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []
        intervals = sorted(intervals,key= lambda x: x.start)
        res = [intervals[0]]
        for n in intervals[1:]:
            if n.start <= res[-1].end:
                res[-1].end = max(res[-1].end, n.end)
            else:
                res.append(n)
        return res
