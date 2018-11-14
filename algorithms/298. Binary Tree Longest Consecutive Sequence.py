# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.length = 0
        def dfs(node,l):
            self.length = max(self.length,l)
            if node.left:
                if node.left.val == node.val + 1:
                    
                    dfs(node.left,l+1)
                else:
                    dfs(node.left,1)
            if node.right:
                if node.right.val == node.val + 1:
                    dfs(node.right,l+1)
                else:
                    dfs(node.right,1)
        dfs(root,1)
        return self.length
