class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals:
            return True
        intervals.sort(key=lambda x:x[0])
        l = len(intervals)
        for i in range(l-1):
            if intervals[i][1] > intervals[i+1][0]:
                return False
        return True
