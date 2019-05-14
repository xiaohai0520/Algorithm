class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        
        def helper():
            stack = []
            res = 0
            for i,hi in enumerate(h + [0]):
                while stack and h[stack[-1]] > hi:
                    cur = stack.pop()
                    pre = stack[-1] if stack else -1
                    res = max(res,h[cur]*(i-pre-1))
                      
                stack.append(i)
            return res  
        
        
        area = 0
        h = [0] *len(matrix[0]) 
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):               
                h[j] = h[j]+1 if matrix[i][j] == "1" else 0
            print(h)
            cur_area = helper()

            area = max(area,cur_area)
        return area
            
