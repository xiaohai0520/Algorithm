class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        dic = collections.defaultdict(int)
        for i in range(len(leftChild)):
            dic[leftChild[i]] += 1
            dic[rightChild[i]] += 1
        
        
        
        queue = collections.deque([])
        
        for i in range(n):
            if dic[i] == 0:
                queue.append(i)
        if len(queue) != 1:
            return False
        
        #print(queue)
        
        
        visited = set()
        while queue:
            cur = queue.popleft()
            #print(cur)
            if cur in visited:
                return False
            visited.add(cur)
            #print(visited)
            if leftChild[cur] != -1:
                queue.append(leftChild[cur])
            if rightChild[cur] != -1:
                queue.append(rightChild[cur])
        return len(visited) == n
        
