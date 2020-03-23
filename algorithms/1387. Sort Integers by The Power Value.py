class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        dic = {1:0}
        def power(n):
            if n in dic:
                return dic[n]
            if n % 2:
                dic[n] = power(3 * n + 1) + 1
            else:
                dic[n] = power(n // 2) + 1
            return dic[n]    
        res = {}
        for num in range(lo,hi+1):
            res[num] = power(num)
               
        ls = sorted(list(res.items()),key=lambda x:(x[1],x[0]))

        return ls[k-1][0]
    
            
        
