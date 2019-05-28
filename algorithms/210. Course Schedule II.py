class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        degree = [0] * numCourses
        for i,j in prerequisites:
            degree[i] += 1
            graph[j].append(i)
            
            
        queue = collections.deque([n for n in range(numCourses) if degree[n] == 0])
        path = []
        while queue:
            cur = queue.popleft()
            path.append(cur)
            
            for c in graph[cur]:
                degree[c] -= 1
                if degree[c] == 0:
                    queue.append(c)
        return path if len(path) == numCourses else []

    
    
