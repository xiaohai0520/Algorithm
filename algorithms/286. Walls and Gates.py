class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        """
        if not rooms:
            return 
        r, c= len(rooms), len(rooms[0])
        for i in range(r):
            for j in range(c):
                if rooms[i][j] == 0:
                    queue = collections.deque([])
                    queue.append((i+1, j, 1)); queue.append((i-1, j, 1))
                    queue.append((i, j+1, 1)); queue.append((i, j-1, 1))
                    visited = set()
                    while queue:
                        x, y, val = queue.popleft()
                        if x < 0 or x >= r or y < 0 or y >= c or rooms[x][y] in [0, -1] or (x, y) in visited:
                            continue
                        visited.add((x, y))
                        rooms[x][y] = min(rooms[x][y], val)
                        queue.append((x+1, y, val+1)); queue.append((x-1, y, val+1))
                        queue.append((x, y+1, val+1)); queue.append((x, y-1, val+1))
