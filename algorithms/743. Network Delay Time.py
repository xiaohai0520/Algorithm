class Solution:
    def networkDelayTime(self, times: 'List[List[int]]', N: 'int', K: 'int') -> 'int':
        edges = collections.defaultdict(dict)
        for edge in times:
            u, v, c = edge
            edges[u][v] = c

        visited = {K}
        heap = [(0, K)]
        while heap:

            pre_cost, u = heapq.heappop(heap)
            visited.add(u)
            if len(visited) == N:
                return pre_cost

            nexts = edges[u]
            if not nexts:
                continue
            for v in edges[u]:
                if v in visited:
                    continue
                heapq.heappush(heap, (edges[u][v] + pre_cost, v))
        return -1
