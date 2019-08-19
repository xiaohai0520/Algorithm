class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        def helper(n, d):
            if n in d:
                return d[n]
            
            if n%2 == 0:
                d[n] = helper(n/2, d) + 1
            else:
                d[n] = 1 + min(helper(n + 1, d), helper(n - 1, d))
            return d[n]
                
        d = {1: 0}
        return helper(n, d)
