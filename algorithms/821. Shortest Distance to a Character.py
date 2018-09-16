#get the position of c and for abs

class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        pos = []
        for i, v in enumerate(S):
            if v == C:
                pos.append(i)
        res = [0] * len(S)
        for i in range(len(S)):
            res[i] = min([abs(i - p) for p in pos])
        return res
            
           
                
                
        
