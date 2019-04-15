This is a dfs problem. When we meet the tree, the question always can be solved by dfs.

In this question, we can have two ways to solve this problem.

The first one is bottom up, the second one is top down,

BOTTOM UP.
we just need to dfs every node, and return the best res, max, min  to update these three values.

TOP DOWN
we transalte the max and min to the leaf, update these two values all the time. 



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        
        
        
#         def dfs(root):
#             # if not root:
#             #     return 0,float('-inf'),float('inf')
#             res,high,low = 0,float('-inf'),float('inf')
#             if root.left:
#                 r,h,l = dfs(root.left)
#                 res = max(r,res)
#                 high = max(high,h)
#                 low = min(low,l)
#             if root.right:
#                 r,h,l = dfs(root.right)
#                 res = max(r,res)
#                 high = max(high,h)
#                 low = min(low,l)
            
#             return max(res,high - root.val, root.val - low),max(root.val,high),min(root.val,low)
        
#         return dfs(root)[0]


        def helper(root,mx,mn):
            if not root:
                return mx - mn
            return max(mx-root.val,root.val-mn,helper(root.left,max(root.val,mx),min(root.val,mn)),helper(root.right,max(root.val,mx),min(root.val,mn)))
        
        return helper(root,0,100000)
