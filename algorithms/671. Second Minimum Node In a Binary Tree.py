# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        if root.left is None or root.right is None:  
            return -1
        left_min = root.left.val if root.val != root.left.val else self.findSecondMinimumValue(root.left)
        right_min = root.right.val if root.val != root.right.val else self.findSecondMinimumValue(root.right)
        if left_min == -1:  return right_min
        if right_min == -1: return left_min
        return min(left_min, right_min)
