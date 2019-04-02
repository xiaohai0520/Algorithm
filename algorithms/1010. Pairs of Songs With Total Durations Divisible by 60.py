class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        n=len(time)
        if n==1: return 0
        
        # 1 计数每个不同余数所含个数
        counts = [0]*60
        for t in time:
            counts[t%60]+=1
        
        # 2 计数可被整除的时间对
        count_pair = (counts[0]*(counts[0]-1) + counts[30]*(counts[30]-1))//2
        for i in range(1,30):
            count_pair += counts[i]*counts[60-i]
        
        return count_pair
