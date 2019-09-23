class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = collections.defaultdict(list)
        for s,e in connections:
            graph[s].append(e)
            graph[e].append(s)
        
        ids = [-1] * n
        low = [-1] * n
        
        self.id = 0
        
        def dfs(node,parent,bridges):
            ids[node] = low[node] = self.id
            self.id += 1
            
            for to in graph[node]:
                if to == parent:
                    continue
                if ids[to] == -1:
                    dfs(to,node,bridges)
                    low[node] = min(low[node],low[to])
                    if ids[node] <low[to]:
                        bridges.append([node,to])
                # else:
                low[node] = min(low[node],ids[to])
        bridges = []            
        dfs(0,-1,bridges)
        return bridges
