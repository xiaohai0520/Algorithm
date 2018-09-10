class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n < 3:
            return 0
        res = [1 for i in range(n)]
        res[0] = res[1] = 0
        for i in range(2,int(n ** 0.5) + 1):
            if res[i]:
                for j in range(i*i,n,i):
                    res[j] = 0
        return sum(res)
