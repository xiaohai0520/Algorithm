左右寻找矮边作为最低线，依次左右往中间汇聚，加上差值。

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        l, r, water, minHeight = 0, n - 1, 0, 0
        while l < r:
            while l < r and height[l] <= minHeight:
                water += minHeight - height[l]
                l += 1
            while r > l and height[r] <= minHeight:
                water += minHeight - height[r]
                r -= 1
            minHeight = min(height[l], height[r])
        return water
    
class Solution:
    def trap(self, height: List[int]) -> int:
        if height == []:
            return(0)
        water = 0
        size = len(height)

        left_max = [-1]* size
        right_max = [-1] * size

        left_max[0] = height[0]

        for i in range(size):
            left_max[i] = max(height[i], left_max[i - 1])

        right_max[size - 1] = height[size - 1]
        for i in range(size - 2, 0, -1):
            right_max[i] = max(height[i], right_max[i + 1])

        for i in range(i, size - 1):
            water += min(left_max[i], right_max[i]) - height[i]

        return water
