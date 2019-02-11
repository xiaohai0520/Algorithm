# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDiffInBST(self, root: 'TreeNode') -> 'int':
#         self.diff = float('inf')
#         self.helper(root)
#         return self.diff
#     def helper(self,root):
#         if not root:
#             return

#         if root.left:
#             l = root.left
#             while l.right:
#                 l = l.right
#             self.diff = min(self.diff,root.val-l.val)
#         if root.right:
#             r = root.right
#             while r.left:
#                 r = r.left
#             self.diff = min(self.diff,r.val - root.val)
        
#         self.helper(root.left)
#         self.helper(root.right)

        stack = []
        res = float('inf')
        pre = None

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            diff = root.val - pre.val if pre else float('inf')
            res = min(res,diff)
            pre,root = root,root.right
        return res
