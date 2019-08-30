# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        
        if not root:
            return None
        def dfs(root,cur):
            if not root:
                return
            if not root.left and not root.right:
                if cur + root.val < limit:
                    return None
                else:
                    return root
            left = dfs(root.left,cur+root.val)
            right = dfs(root.right,cur+root.val)
            if not left and not right:
                return 
            else:
                root.left = left
                root.right = right
                return root
        return dfs(root, 0)
