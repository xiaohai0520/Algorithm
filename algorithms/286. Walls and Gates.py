class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        q = collections.deque([(i, j, 0) for i, row in enumerate(rooms) for j, col in enumerate(row) if not col])
        print(q)
        visited = set()
        while q:
            
            x,y,val = q.popleft()
            
            for i,j in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
                if i<0 or j < 0 or i >= len(rooms) or j >= len(rooms[0]) or rooms[i][j] in [0,-1] or (i,j) in visited:
                    continue
                print((i,j))
                rooms[i][j] = min(rooms[i][j],val+1)
                visited.add((i,j))
                q.append((i,j,val+1))
        
        
        
#         for i in range(len(rooms)):
#             for j in range(len(rooms[0])):
#                 if rooms[i][j] == 0:
#                     queue = collections.deque([])
#                     queue.append((i+1,j,1))
#                     queue.append((i-1,j,1))
#                     queue.append((i,j+1,1))
#                     queue.append((i,j-1,1))
#                     visited = set()
                    
#                     while queue:
#                         a,b,val = queue.popleft()
#                         if a < 0 or b < 0 or a >= len(rooms) or b >= len(rooms[0]) or rooms[a][b] in [0,-1] or (a,b) in visited:
#                             continue
#                         rooms[a][b] = min(rooms[a][b],val)
#                         visited.add((a,b))
#                         queue.append((a+1,b,val+1))
#                         queue.append((a-1,b,val+1))
#                         queue.append((a,b+1,val+1))
#                         queue.append((a,b-1,val+1))
                        
                    
