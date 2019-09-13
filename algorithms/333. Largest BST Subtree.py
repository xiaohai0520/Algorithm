# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:
        self.res = 0
        
        def dfs(node):
            if not node:
                return 0,float('inf'),float('-inf') #  num, min,max
            l,lmin,lmax = dfs(node.left)
            r,rmin,rmax = dfs(node.right)
            if l == -1 or r == -1 or not lmax < node.val < rmin:
                return -1,0,0
            self.res = max(self.res,l+r+1)
            return l+r+1, min(node.val,lmin),max(node.val,rmax)
        dfs(root)
        return self.res
