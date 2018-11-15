# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ls = []
        def dfs(node,path):
            if not node:
                return 
            if not node.left and not node.right:
                ls.append(path+str(node.val))
                return
            if node.left:
                dfs(node.left,path+str(node.val))
            if node.right:
                dfs(node.right,path+str(node.val))
        dfs(root,'')
        return sum(map(int,ls))
            
