class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:(x[0], -x[1]))
        count=0
        
        prev_end=0
        for start, end in intervals:
            if end > prev_end:
                count+=1
                prev_end=end
        return count        
        
        
        
        
        # res = len(intervals)
        # intervals.sort(key=lambda x:(x[0],-x[1]))
        # while intervals:
        #     x1,y1 = intervals.pop()
        #     for each in intervals:
        #         if each[0] <= x1 and each[1] >= y1:
        #             res -= 1
        #             break
        # return res
                       
                      
                    
                    
