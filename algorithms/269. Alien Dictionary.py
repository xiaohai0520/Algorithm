class Solution:
    def alienOrder(self, words: List[str]) -> str:
              
        indegree = {ch: 0 for word in words for ch in word}
        graph = {ch:set() for word in words for ch in word}


        for i in range(len(words) - 1):
            for j in range(min(len(words[i]), len(words[i + 1]))):
                first, second = words[i][j], words[i + 1][j]
                if first != second:
                    if second not in graph[first]:
                        graph[first].add(second)
                        indegree[second] += 1
                    break

        #topological sort
        q = collections.deque([])
        for ch in indegree:
            if indegree[ch] == 0:
                q.append(ch)

        res_order = []

        while q:
            node = q.popleft()
            res_order.append(node)

            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)

        if len(graph) != len(res_order):
            return ""

        return ''.join(res_order)
