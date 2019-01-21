# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.helper(root,float('-inf'),float('inf'))
        
    def helper(self,root,low,high):
        if not root:
            return True
        return low < root.val < high and self.helper(root.left,low,root.val) and self.helper(root.right,root.val,high)
        
