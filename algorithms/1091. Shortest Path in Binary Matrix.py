class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if not grid:
            return -1
        if grid[0][0] == 1:
            return -1
        visited = set([(0,0)])
        queue = collections.deque([(0,0,1)])
        while queue:
            x,y,step = queue.popleft()
            if x== len(grid)-1 and y == len(grid[0])-1:
                return step
            for dx,dy in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]:
                if 0 <= x+dx < len(grid) and 0 <= y+dy < len(grid[0]) and (x+dx,y+dy) not in visited and grid[x+dx][y+dy]!= 1:
                    if x+dx == n and y+dy == n:
                        return step+1
                    queue.append((x+dx,y+dy,step+1))
                    visited.add((x+dx,y+dy))
        return -1
