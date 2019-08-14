class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
#         dp = [i for i in range(n+1)]
        
#         for i in range(1,int(n**0.5)+1):
#             dp[i*i] = 1
        
#         for i in range(2,n+1):
#             for num in [j**2 for j in range(1,int(n**0.5)+1)]:
#                 if i >= num:
#                     dp[i] = min(dp[i],dp[i-num]+1)
#         return dp[-1]



        if n < 2:
                return n
        lst = []
        i = 1
        while i * i <= n:
            lst.append( i * i )
            i += 1
        cnt = 0
        toCheck = {n}
        while toCheck:
            cnt += 1
            temp = set()
            for x in toCheck:
                for y in lst:
                    if x == y:
                        return cnt
                    if x < y:
                        break
                    temp.add(x-y)
            toCheck = temp

        return cnt
