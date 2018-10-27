# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.count = 0
        self.dfs(root)
        return self.count

    def dfs(self, root):
        if root is None:
            return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)

        left = left + 1 if root.left and root.left.val == root.val else 0
        right = right + 1 if root.right and root.right.val == root.val else 0

        self.count = max(self.count, left + right)
        return max(left, right)
