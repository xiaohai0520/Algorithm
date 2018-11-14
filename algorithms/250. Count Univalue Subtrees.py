# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        self.count = 0
        self.checkUni(root)
        return self.count

    def checkUni(self, root):
        if not root:
            return True
        l, r = self.checkUni(root.left), self.checkUni(root.right)
        if l and r and (not root.left or root.left.val == root.val) and \
        (not root.right or root.right.val == root.val):
            self.count += 1
            return True
        return False

        
#         self.res = 0
        
#         def helper(node):
#             if not node:
#                 return True
#             if not node.left and not node.right:
#                 self.res += 1
#                 return True
           
#             l = helper(node.left)
#             r = helper(node.right)

#             if l and r:
#                 if node.left and not node.right and node.left.val == node.val:
#                     self.res += 1
#                     return True
#                 elif node.right and not node.left and node.right.val == node.val:
#                     self.res += 1
#                     return True
#                 elif node.right and node.left and node.right.val ==node.val and node.left.val == node.val:
#                     self.res += 1
#                     return True
                             
#                 return False
#         helper(root)
#         return self.res
