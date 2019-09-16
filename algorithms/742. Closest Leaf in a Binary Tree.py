# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findClosestLeaf(self, root: TreeNode, k: int) -> int:
        
        
        def helper(node,k):
            if not node:
                return float('inf'),False,None
            if not node.left and not node.right:
                return 0,node.val == k,node.val
            
            l_min_dis,l_contains,l_val = helper(node.left,k)
            r_min_dis,r_contains,r_val = helper(node.right,k)
            
            if l_contains:
                r_min_dis += 2
            elif r_contains:
                l_min_dis += 2
            else:
                l_min_dis += 1
                r_min_dis += 1
            
            val = l_val if l_min_dis < r_min_dis else r_val
            
            return min(l_min_dis,r_min_dis), node.val == k or l_contains or r_contains,val
        return helper(root,k)[2]
            
                
