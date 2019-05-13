class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        heights.append(-1)
        stack = []
        i, area = 0, 0
        while 1:
            if not stack and i == len(heights) - 1:
                return area
            while not stack or heights[stack[-1]] <= heights[i]:
                stack.append(i)
                i += 1
            height = stack.pop()
            if not stack:
                width = i
            else:
                width = (i - stack[-1] - 1)
            area = max(area, heights[height] * width)
