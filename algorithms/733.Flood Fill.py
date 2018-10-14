#dfs
class Solution:
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        def dfs(x, y, prev_color):
            # make sure we're within bounds
            if x < 0 or x >= len(image) or y < 0 or y >= len(image[0]): 
                return
            if image[x][y] != prev_color or image[x][y] == newColor:
                return

            image[x][y] = newColor
            # .. recursively
            dfs(x - 1, y, prev_color)
            dfs(x, y - 1, prev_color)
            dfs(x, y + 1, prev_color)
            dfs(x + 1, y, prev_color)
            
        dfs(sr, sc, image[sr][sc])
        
        return image
