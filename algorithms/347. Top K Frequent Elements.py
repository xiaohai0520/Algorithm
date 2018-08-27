#use dic to save the frequent of each number
#use heap to find the top-k or use sort 

import heapq 

class Solution:
    
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dic = {}
        for num in nums:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1
        # lst = [(v, k) for k, v in dic.items()] 
        # lst.sort(key=lambda x:-x[0])
        # return [v for _, v in lst[:k]]
        
        h = []
        count = 0
        for k1, v in dic.items():
            if count < k:
                heapq.heappush(h,(v,k1))
                count += 1
                continue
            cur = heapq.heappop(h)
            if cur[0] < v:
                heapq.heappush(h,(v,k1))
            else:
                heapq.heappush(h,cur)
        res = []
        for i in range(k):
            res.append(heapq.heappop(h)[1])
        res.reverse()
        return res
        
            
            
