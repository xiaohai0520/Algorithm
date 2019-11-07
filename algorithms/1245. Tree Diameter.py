class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        graph = collections.defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)
        bfs = {(u, None) for u, nex in graph.items() if len(nex) == 1}
        move = 0
        while bfs:
            bfs, move = {(v, u) for u, pre in bfs for v in graph[u] if v != pre}, move + 1
        return max(move - 1, 0)
