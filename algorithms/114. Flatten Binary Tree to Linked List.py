#preorder


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        root1 = root
        stack = [root1]
        while stack:
            cur = stack.pop()
            if cur is not root:
                root1.right = cur
                root1.left = None
                root1 = root1.right
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
