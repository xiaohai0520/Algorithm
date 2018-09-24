# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

        stack = []
        cur = root
        index = 0
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left 
            cur = stack.pop()
            index += 1
            if index == k:
                return cur.val
            cur = cur.right

        
            
