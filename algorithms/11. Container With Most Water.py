这里需要定义i和j两个指针分别指向数组的左右两端，
然后两个指针向中间搜索，每移动一次算一个值和结果比较取较大的，
容器装水量的算法是找出左右两个边缘中较小的那个乘以两边缘的距离，


class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left,right = 0,len(height) - 1
        area = 0
        
        while left < right:
            area = max(area,(right - left) * min(height[right],height[left]))
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return area
