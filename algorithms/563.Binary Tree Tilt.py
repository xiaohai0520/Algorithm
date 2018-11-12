# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def tilt(root):
            # return (sum, tilt) of tree
            if not root: return (0, 0)
            left = tilt(root.left)
            right = tilt(root.right)
            return (left[0] + right[0] + root.val, abs(left[0] - right[0]) + left[1] + right[1])
        return tilt(root)[1]
       
