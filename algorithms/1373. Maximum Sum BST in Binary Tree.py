# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxSumBST(self, root: TreeNode) -> int:
        self.res = 0
        def dfs(node):
            
            if not node:
                return float('inf'),float('-inf'),0,True
            
            ll,lh,ls,lv = dfs(node.left)
            rl,rh,rs,rv = dfs(node.right)
            v = lv and rv and lh < node.val < rl
            s = ls + rs + node.val if v else -1
            self.res = max(self.res,s)
            return (min(ll,node.val),max(rh,node.val),s,v)
            
        dfs(root)
        return self.res
