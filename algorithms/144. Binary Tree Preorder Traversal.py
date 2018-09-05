# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderItervate(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        stack,res = [root],[]
        while stack:
            cur = stack.pop()
            res.append(cur.val)
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
        return res
        
        
    def preorderrecursive(self, root):
        res = []
        self.helper(root,res)
        return res
        
    def helper(self,node,res):
        if not node:
            return
        res.append(node.val)
        self.helper(node.left,res)
        self.helper(node.right,res)
