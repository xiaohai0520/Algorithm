class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        N = len(gas)
        
        tmp = []
        
        for g, c in zip(gas, cost):
            tmp.append(g - c)
            
        dp = tmp * 2
        
        pre = 0
        start = 0
        for i in range(2 * N):
            pre += dp[i]
            
            if pre < 0:
                start = i+1
                pre = 0
            elif pre >= 0:
                if i - start == N-1:
                    return start
                
        return -1
