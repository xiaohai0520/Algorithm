##quick select


class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        #quick sort

#         pivot = nums[0]   
#         large = [num for num in nums if num > pivot]
#         equal = [num for num in nums if num == pivot]
#         small = [num for num in nums if num < pivot]
        
#         if k <= len(large):
#             return self.findKthLargest(large,k)
#         elif len(large) < k <= len(equal) + len(large):
#             return pivot
#         else:
#             return self.findKthLargest(small,k-len(equal)-len(large))


        import heapq
        min_heap = nums[:k]
        heapq.heapify(min_heap)
        for i in range(k,len(nums)):
            if nums[i] > min_heap[0]:
                heapq.heapreplace(min_heap,nums[i])
        return min_heap[0]
    
    

    
        
