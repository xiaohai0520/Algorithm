class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        
        stack = []
        res = []
        for i in range(len(nums)):
            if i >= k:
                if stack[0][1] == i - k:
                    stack.pop(0)
                    
            while stack and nums[i] >= stack[-1][0]:
                stack.pop()
            stack.append((nums[i],i))
            if i >= k - 1:
                res.append(stack[0][0])
        
        return res
