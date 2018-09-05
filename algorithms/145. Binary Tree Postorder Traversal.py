# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        stack = [root]
        from collections import deque
        res = deque()
        while stack:
            cur = stack.pop()
            res.appendleft(cur.val)
            
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
        return list(res)
