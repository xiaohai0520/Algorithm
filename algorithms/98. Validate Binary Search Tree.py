#recursive or inorder

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        stack = []
        pre = None
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if pre and pre.val >= root.val:
                return False
            pre = root
            root = root.right
        return True
             
        
#         return self.helper(root,float("-inf"), float("inf"))
    
    def helper(self,root,left,right):
        if not root:
            return True
        return left < root.val < right and self.helper(root.left,left,root.val) and self.helper(root.right,root.val,right)
