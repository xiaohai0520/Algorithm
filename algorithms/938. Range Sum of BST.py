# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        self.res = 0
        def helper(root,L,R):
            if not root:
                return
            if L <= root.val <= R:
                self.res += root.val
                helper(root.left,L,root.val)
                helper(root.right,root.val,R)
            elif root.val < L:
                helper(root.right,L,R)
            else:
                helper(root.left,L,R)
        helper(root,L,R)
        return self.res
