This is a greedy problem.

We always want to search the minimum number of the videos.

For greedy problem, we need to search the problem in the sequence. So we need to sort this list firstly.

We record the largest place and the previous largest place, it means that we also want to get a better one unless we have no choice to add one into the results list.

if the video start is larger than the actual end, we need to add one to result.

if the video start is smaller than the actual end, we just need to update the further end.

if the further end is larger than T or next video start is larger than the furthest end. need to break

Example explain:

clips = [[0,4],[3,10],[2,8]]    T= 9

sort: clips = [[0,4],[2,8],[3,10]]

pre_end = -1, end = 0 res = 0

1.[0,4] the start is larger than the pre_end, we must add one into the result.
result = [[0,4]]  and the pre_end = end = 0 end = 4
2.[2,8] now we want to go further, so must add something in. 
result = [[0,4],[2,8]] and the pre_end = 4,end = 10
3.[2,10] we see the new video start is also less than the pre_end, we do not need to add new one, only need to update the further end.
result = [[0,4],[3,10]]

Code:

class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        clips.sort()
        pre_end,next_end,res = -1,0,0
        
        for i,j in clips:
            if next_end >= T or i > next_end:
                break
            elif pre_end < i <= next_end:
                pre_end = next_end
                res += 1
            next_end = max(j,next_end)
        return res if next_end >= T else -1

