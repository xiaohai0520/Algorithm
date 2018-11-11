# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if not root:
            return False

        return self._findTarget(root, set(), k)
    
    def _findTarget(self, node, nodes, k):
        if not node:
            return False

        complement = k - node.val
        if complement in nodes:
            return True

        nodes.add(node.val)

        return self._findTarget(node.left, nodes, k) or self._findTarget(node.right, nodes, k)
            
