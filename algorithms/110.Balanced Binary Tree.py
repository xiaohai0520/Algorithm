# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        return abs(self.getHeight(root.left) - self.getHeight(root.right)) < 2 and self.isBalanced(root.left) and self.isBalanced(root.right)

    def getHeight(self, root):
        if not root:
            return 0

        return 1 + max(self.getHeight(root.left), self.getHeight(root.right))
  


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.recurs(root)[1]
    
    def recurs(self, node):
        if not node:
            return 0, True
        lHeight, lBalanced = self.recurs(node.left)
        rHeight, rBalanced = self.recurs(node.right)
        return max(lHeight, rHeight) + 1, lBalanced and rBalanced and abs(lHeight - rHeight) <= 1
