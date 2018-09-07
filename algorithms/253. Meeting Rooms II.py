#see room as source, sort for start time,
#if start < min(end)  create a new room
#if start >= min(end), use the same room, replace

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

import heapq 
class Solution:
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        
        intervals.sort(key=lambda x:x.start)
        heap = []
        for i in intervals:
            if heap and i.start >= heap[0]:
                heapq.heapreplace(heap,i.end)
            else:
                heapq.heappush(heap,i.end)
        return len(heap)
