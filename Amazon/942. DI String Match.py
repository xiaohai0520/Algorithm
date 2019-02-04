class Solution:
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        left = 0
        right = len(S)
        
        res = [0] * (len(S) + 1)
        
        for i,st in enumerate(S):
            if st == 'I':
                res[i] = left
                left += 1
            else:
                res[i] = right
                right -= 1
        res[-1] = left
        return res
