# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
#         if not root:
#             return 
        
#         res = []
#         stack = []
#         while stack or root:
#             while root:
#                 stack.append(root)
#                 root = root.left
#             root = stack.pop()
#             res.append(root.val)
#             root = root.right
#         res = res[::-1]
#         Dummy = cur = TreeNode(0)
#         while res:
#             cur.right = TreeNode(res.pop())
#             cur = cur.right
#         return Dummy.right
        return self.helper(root,None)
        
    def helper(self,root,tail):
        if not root:
            return tail
        res = self.helper(root.left,root)
        root.left = None
        root.right = self.helper(root.right,tail)
        return res
        
