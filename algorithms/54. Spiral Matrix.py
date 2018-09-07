#while condition,left <= right  top <= down
circle by circle
or  pop() to update the matrix


class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        left,right,up,down,res = 0,len(matrix[0])-1,0,len(matrix)-1,[]
        while left <= right and up <= down:
            res.extend(matrix[up][left:right+1])
            up += 1
            
            for i in range(up,down+1):
                res.append(matrix[i][right])
            right -= 1
            if up <= down:
                res.extend(matrix[down][left:right+1][::-1])
                down -= 1
            if left <= right:
                for i in range(down,up-1,-1):
                    res.append(matrix[i][left])
                left += 1
        return res
