# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.first,self.second, self.pre = None,None,None
        
        def helper(node):
            if not node:
                return 
            helper(node.left)
            if not self.first and self.pre and node.val < self.pre.val:
                self.first = self.pre
            if self.first and node.val < self.pre.val:
                self.second = node
            self.pre = node
            helper(node.right)
            
        helper(root)
        self.first.val, self.second.val = self.second.val, self.first.val
