class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        upper_i, upper_j, lower_i, lower_j,  = 0, n - 1, n - 1, 0 
        num = 1
        
        # create n*n matrix
        matrix = [[0 for _ in range( n )] for _ in range( n )]
        
        while num <= n*n:
            for j in range( lower_j, upper_j + 1, 1 ):
                # assign num across current most-top row
                matrix[lower_j][j] = num
                num += 1
            # increment to avoid overwriting current most-top row
            upper_i += 1

            for i in range( upper_i, lower_i + 1, 1 ):
                # assign num across current most-right column
                matrix[i][upper_j] = num
                num += 1
            # decrement to avoid overwriting current most-right row
            upper_j -= 1
            
            for j in range( upper_j, lower_j - 1, -1 ):
                # assign num across current most-bottom row
                matrix[lower_i][j] = num
                num += 1
            # decrement to avoid overwriting current most-bottom row
            lower_i -= 1
            
            for i in range( lower_i, upper_i - 1, -1 ):
                # assign num across current most-left column
                matrix[i][lower_j] = num
                num += 1
            # increment to avoid overwriting current most-left column
            lower_j += 1 
            
        return matrix
