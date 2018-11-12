# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def helper(node):
            if not node:
                return None
            right = helper(node.right)
            self.total += node.val
            newNode = TreeNode(self.total)
            newNode.right = right
            newNode.left = helper(node.left)
            return newNode
            
        
        self.total = 0
        return helper(root)
