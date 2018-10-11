class Solution:
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        
        
        def tominutes(time):
            return int(time[:2]) * 60 + int(time[3:])
        
        ls = list(map(tominutes,timePoints))
        
        minres = 24*60 
        ls.sort()
        for i in range(len(ls) -1):
            minres = min(ls[i+1] - ls[i],minres)
        minres = min(minres,24*60-ls[-1] + ls[0])
        return minres
                
