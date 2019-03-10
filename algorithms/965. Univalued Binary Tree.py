# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def isUnivalTree(self, root: TreeNode) -> bool:
        if not root:
            return True
        value = root.val
        queue = collections.deque([root])
        while queue:
            cur = queue.popleft()
            if cur.val != value:
                return False
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        return True
            
        
        
        
        
        
        
        
        
#         if not root:
#             return True
#         def helper(node,value):
#             if not node:
#                 return True

#             return node.val == value and helper(node.left,value) and helper(node.right,value)
        
#         return helper(root,root.val)
        
