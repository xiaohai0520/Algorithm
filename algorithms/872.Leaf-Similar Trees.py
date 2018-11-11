# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        res1 = []
        res2 = []
        self.helper(root1,res1)
        self.helper(root2,res2)
        return res1 == res2
        
    
    
    def helper(self,root,res):
        if not root:
            return 
        if not root.left and not root.right:
            res.append(root.val)
            return
        if root.left:
            self.helper(root.left,res)
        if root.right:
            self.helper(root.right,res)
        
        
        
