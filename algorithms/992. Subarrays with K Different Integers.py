class Solution:
    def atmost_k(self,s,k):
        
        n = len(s)
        if n <= k:
            return n
                
        i = 0
        j = 0
        ans = 0
        prev = collections.defaultdict(int)
        
        while i < n and j < n:
            prev[s[j]] += 1
                
            while len(prev) > k:
                prev[s[i]] -= 1
                if prev[s[i]] == 0:
                    del prev[s[i]]
                i += 1
                
            ans +=  j-i+1
            j += 1
            
        return ans
    
    def subarraysWithKDistinct(self, s: List[int], k: int) -> int:
        return self.atmost_k(s,k) - self.atmost_k(s,k-1)
    
    
        
