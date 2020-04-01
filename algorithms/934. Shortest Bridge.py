class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        def dfs(i,j,n):
            if i < 0 or i >= n or j < 0 or j >= n or A[i][j] == 0 or (i,j) in land:
                return
            land.add((i,j))
            for x,y in ((1,0),(-1,0),(0,1),(0,-1)):
                dfs(i+x,j+y,n)
        
        
        
        land = set()
        n = len(A[0])
        flag = 0
        for i in range(n):
            for j in range(n):
                if A[i][j] == 1:
                    if flag == 0:
                        dfs(i,j,n)
                        flag = 1

        print(land)       
        queue = collections.deque(list(land))
        step = 0
        while queue:
            print(queue)
            for _ in range(len(queue)):
                i,j = queue.popleft()
                for x,y in ((1,0),(-1,0),(0,1),(0,-1)):
                    if 0 <= i+x < n and 0 <= j + y < n:
                        if A[i+x][j+y] == 1 and (i+x,j+y) not in land:
                            return step
                        if A[i+x][j+y] == 0:
                            A[i+x][j+y] = 1
                            queue.append((i+x,j+y))
                            land.add((i+x,j+y))

            step += 1

                        
            
