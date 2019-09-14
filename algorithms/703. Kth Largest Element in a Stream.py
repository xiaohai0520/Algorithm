import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        
        self.hq = []
        self.k = k
        for num in nums:
            if len(self.hq) < k:
                heapq.heappush(self.hq,num)

            else:
                heapq.heappushpop(self.hq,num)
        
        
        

    def add(self, val: int) -> int:
        if len(self.hq) < self.k:
            heapq.heappush(self.hq,val)
        else:
            heapq.heappushpop(self.hq,val)
        return self.hq[0]
        
        
        
        

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
