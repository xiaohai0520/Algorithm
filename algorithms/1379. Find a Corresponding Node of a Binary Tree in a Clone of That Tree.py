# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        queue = collections.deque([(original,cloned)])
        
        while queue:
            o,c = queue.popleft()
            if o is target:
                return c
            if o.left:
                queue.append((o.left,c.left))
            if o.right:
                queue.append((o.right,c.right))
        
            
