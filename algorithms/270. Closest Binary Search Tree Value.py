# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        if not root:
            return sys.maxint
        if not root.left and not root.right:
            return root.val
        node = root.right if target > root.val else root.left
        if not node:
            return root.val
        tmp = self.closestValue(node, target)
        return min((tmp, root.val), key=lambda x:abs(x-target))
