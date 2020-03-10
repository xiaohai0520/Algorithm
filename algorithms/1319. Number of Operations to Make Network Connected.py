class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        def find(x):
            while a[x]>=0:
                x = a[x]
            return x
        def union(x,y):
            xp,yp = find(x), find(y)
            if xp!=yp:
                a[yp] = xp
                a[xp]-=1
        
        
        if len(connections)<(n-1):
            return -1
        a = [-1 for _ in range(0,n)]
        disconnected = 0
        for i,j in connections:
            union(i,j)
        for i in a:
            if i<=-1:
                disconnected+=1
        return disconnected-1
        
        
        
        
        
        
        
        # self.visited = [False for i in range(n)]
        # self.graph = collections.defaultdict(list)
        # for i in connections:
        #     self.graph[i[0]].append(i[1])
        #     self.graph[i[1]].append(i[0])
        # def dfs(i):
        #     self.visited[i] = True
        #     for j in self.graph[i]:
        #         if not self.visited[j]:
        #             dfs(j)
        # count = 0
        # for i in range(n):
        #     if not self.visited[i]:
        #         dfs(i)
        #         count += 1
        # if len(connections) < (n-1):
        #     return -1
        # else:
        #     return count-1
