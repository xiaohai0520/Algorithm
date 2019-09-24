class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
#         import heapq
#         cap = capacity
#         heap = []
#         trips.sort(key=lambda x:x[1])
        
#         for trip in trips:

#             while heap and heap[0][0] <= trip[1]:
#                 cur = heapq.heappop(heap)
#                 cap += cur[1]
#             heapq.heappush(heap,(trip[2],trip[0]))

#             cap -= trip[0]
#             if cap < 0:
#                 return False
#         return True    
        lst = []
        for n, start, end in trips:
            lst.append((start, n))
            lst.append((end, -n))
        lst.sort()
        pas = 0
        for loc in lst:
            pas += loc[1]
            if pas > capacity:
                return False
        return True
