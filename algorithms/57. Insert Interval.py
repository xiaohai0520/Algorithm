比较每个pair和要插入的pair的关系即可

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        intervals.sort(key=lambda x:x[0])
        res = []
        for i,inter in enumerate(intervals):
            if inter[1] < newInterval[0]:
                res.append(inter)
            elif inter[0] > newInterval[1]:
                res.append(newInterval)
                return res+intervals[i:]
            else:
                newInterval[0] = min(inter[0],newInterval[0])
                newInterval[1] = max(inter[1],newInterval[1])
            # print(newInterval)
        return res + [newInterval]
        
