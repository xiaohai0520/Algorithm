class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if not nums:
            return 0
        p = [1] * len(nums)
        q = [1] * len(nums)
        for i in range(1,len(nums)):

            if nums[i] > nums[i-1]:
                p[i] = q[i-1]+1
                q[i] = q[i-1]
            elif nums[i] < nums[i-1]:
                q[i] = p[i-1] + 1
                p[i] = p[i-1]
            else:
                q[i] = q[i-1]
                p[i] = p[i-1]
        return max(q[-1],p[-1])
        
#         if len(nums) == 0:
#             return 0

#         up = 1
#         down = 1
        
#         for i in range(1, len(nums)):
#             if nums[i] > nums[i-1]:
#                 up = down + 1
#             elif nums[i] < nums[i-1]:
#                 down = up + 1
        
#         return max(down, up)
