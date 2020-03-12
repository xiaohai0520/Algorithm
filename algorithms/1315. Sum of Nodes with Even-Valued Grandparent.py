# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        
        def helper(root,parent,grand):
            if not root:
                return 0
            res = 0
            if grand%2 == 0:
                res += root.val
            res += helper(root.left,root.val,parent)
            res += helper(root.right,root.val,parent)
            return res
        return helper(root,-1,-1)
