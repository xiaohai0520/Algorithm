# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        if not root: 
            return root
        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)
        if not root.left and not root.right and root.val == target:
            return None
        return root
        
        
        
        
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:    
        if not root:
            return None
        
        def helper(node):
            if not node:
                return 0
            l = helper(node.left)
            r = helper(node.right)
            if l == 0:
                node.left = None
            if r == 0:
                node.right = None
                
            if l == 0 and r == 0 and node.val == target:
                return 0
               
            else:
                return 1
        
        n = helper(root)
        return root if n != 0 else None
    
                
