先根据第一位进行排序，
将第一个放入result结果集，依次去对比下一个的0位和res中最后一个的1位，
如果新的大，则加入结果集
否则 判断两个的1位哪个大，大的作为res最后一个的1位

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort(key=lambda x:x[0])
        res = [intervals[0]]
        
        for i in range(1,len(intervals)):
            cur = intervals[i]
            if cur[0] > res[-1][1]:
                res.append(cur)
            else:
                res[-1][1] = max(res[-1][1],cur[1])
        return res
