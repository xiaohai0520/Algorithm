This is a BFS problem.

Each time add four direction node into the queue

Layer by layer. When queue is empty. check the grid has 1 if yes, return -1 else return the layer.


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = collections.deque()
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i,j))
        l = len(queue)
        ls = [(0,1),(0,-1),(1,0),(-1,0)]
        while queue:
            
            for _ in range(l):
                i,j = queue.popleft()
                for d in ls:
                    if 0 <= (i+d[0]) < len(grid) and 0 <= (j+d[1]) <len(grid[0]) and grid[i+d[0]][j+d[1]] == 1:
                        grid[i+d[0]][j+d[1]] = 2
                        print((i+d[0],j+d[1]))
                        queue.append((i+d[0],j+d[1]))
            if queue:
                res += 1
            l = len(queue)
            
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        return res
