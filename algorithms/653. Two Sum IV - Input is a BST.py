# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        if not root:
            return False
        cache = set([])
        def dfs(node):
            if not node:
                return False
            cur = k - node.val
            if cur in cache:
                return True
            cache.add(node.val)
            return dfs(node.left) or dfs(node.right)
        return dfs(root)
