class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        max_num = math.floor(n**0.5) + 1
        queue = collections.deque([(0,0)])
        visited = set()
        while queue:
            step,val = queue.popleft()
            step += 1
            
            for i in range(1,max_num):
                k = val + i*i
                if k == n:
                    return step
                if k > n:
                    break
                if k not in visited:
                    visited.add(k)
                    queue.append((step,k))
