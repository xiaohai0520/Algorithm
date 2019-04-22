This is a problem we can solve with heap.

ALways heap is a min heap ,pop out the min

now we can transfer it into a max heap with input is -num

only use the memory of K

code:
class Solution:
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        import heapq
        heap = []
        i = 0
        for point in points:
            cur = point[0] **2 + point[1]**2
            if i < K:
                heapq.heappush(heap,( -cur ,point[0],point[1]))
                i += 1
                continue
            if cur < -heap[0][0]:
                heapq.heapreplace(heap,(-cur,point[0],point[1]))
        res = []
        for i in range(len(heap)):
            cur = heapq.heappop(heap)
            res.append([cur[1],cur[2]])
        return res[::-1]
