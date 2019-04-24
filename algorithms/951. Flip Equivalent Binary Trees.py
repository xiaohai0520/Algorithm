Tree problem

Try flip and not flip for each node.

either is true is OK.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flipEquiv(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        if root1 is None and root2 is None:
            return True
        if root1 is None or root2 is None:
            return False
        if root1.val != root2.val:
            return False
        return ((self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right))
                or (self.flipEquiv(root1.right, root2.left) and self.flipEquiv(root1.left, root2.right)))
    
    
    
    
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        if not root1 and not root2:
            return True
        elif not root1 or not root2:
            return False
        
        if root1.val != root2.val:
            return False
        
        if root1.left:
            if root2.left and root1.left.val != root2.left.val or not root2.left:
                root2.left,root2.right = root2.right,root2.left
        else:
            if root2.left:
                root2.left,root2.right = root2.right,root2.left
        
        return self.flipEquiv(root1.left,root2.left) and self.flipEquiv(root1.right,root2.right)
