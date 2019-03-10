"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        res = []
        stack = [root]
        queue = collections.deque([])
        while stack:
            cur = stack.pop()
            queue.appendleft(cur.val)
            
            if cur.children:
                stack.extend(cur.children)
        return list(queue)
