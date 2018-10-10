#recursive and iterater

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
#         if not root:
#             return True
#         return self.helper(root.left,root.right)
    
#     def helper(self,left,right):
#         if not left and not right:
#             return True
#         elif not left and right:
#             return False
#         elif not right and left:
#             return False
#         else:
#             return left.val == right.val and self.helper(left.right,right.left) and self.helper(left.left,right.right)
        
        if root is None:
              return True

        stack = [(root.left, root.right)]

        while len(stack) > 0:
            left,right = stack.pop(0)


            if left is None and right is None:
                continue
            if left is None or right is None:
                return False
            if left.val == right.val:
                stack.append((left.left, right.right))

                stack.append((left.right, right.left))
            else:
                return False
        return True




        
