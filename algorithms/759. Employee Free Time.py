"""
# Definition for an Interval.
class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
class Solution:
    def employeeFreeTime(self, schedule: 'list<list<Interval>>') -> 'list<Interval>':
        ls = []
        for s in schedule:
            for interval in s:
                ls.append(interval)
        ls.sort(key=lambda x:x.start)
        res = []
        
        curs,cure = ls[0].start,ls[0].end
        for i,interval in enumerate(ls[1:]):
            if interval.start > cure:
                res.append(Interval(cure,interval.start))
                curs,cure = interval.start,interval.end
            elif interval.end < cure:
                curs = interval.end
            else:
                curs,cure = cure,interval.end
        return res
                
