class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {n:[] for n in range(numCourses)} 
        for i,j in prerequisites:
            graph[i].append(j)
            
        for n in range(numCourses):
            stack = graph[n]
            visited = set()
            while stack:
                course = stack.pop()
                visited.add(course)
                if course == n:
                    return False
                for c in graph[course]:
                    if c not in visited:
                        stack.append(c)
        return True
            
