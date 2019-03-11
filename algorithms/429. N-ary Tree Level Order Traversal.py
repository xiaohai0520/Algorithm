"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        queue = collections.deque([root])
        count = 1
        res = []
        
        while queue:
            layer = []
            for _ in range(count):
                cur = queue.popleft()
                layer.append(cur.val)
                
                if cur.children:
                    queue.extend(cur.children)
            
            count = len(queue)
            res.append(layer)
        return res
