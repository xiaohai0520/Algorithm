# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        ld = self.getdepth(root.left)
        rd = self.getdepth(root.right)
        
        if ld == rd:
            return 2 ** ld + self.countNodes(root.right)
        else:
            return 2 ** rd + self.countNodes(root.left)
        
        
    def getdepth(self,root):
        if not root:
            return 0
        return 1 + self.getdepth(root.left)
