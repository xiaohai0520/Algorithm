# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        return self.dfs(root,sum)
    
    def dfs(self,node,target):
        if not node:
            return False
        if not node.left and not node.right and node.val == target:
            return True
        l = self.dfs(node.left,target-node.val)
        r = self.dfs(node.right,target-node.val)
        return l or r
