# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.res = float('-inf')
        
        def dfs(root):
            if not root:
                return 0
            left = max(0,dfs(root.left))
            right = max(0,dfs(root.right))

            self.res = max(self.res, root.val + left + right)
            return max(left,right)+root.val
        dfs(root)
        return self.res
