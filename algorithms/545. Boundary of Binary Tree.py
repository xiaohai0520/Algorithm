# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = [root.val]
        
        
        
        def lefth(root):
            if not root or (not root.left and not root.right):
                return
            res.append(root.val)
            if root.left:
                lefth(root.left)
            else:
                lefth(root.right)
        def leaves(root):
            if not root:
                return
            if not root.left and not root.right:
                res.append(root.val)
                return
            leaves(root.left)
            leaves(root.right)
        
        def righth(root):
            if not root or (not root.left and not root.right):
                return
            
            if root.right:
                righth(root.right)
            else:
                righth(root.left)
            res.append(root.val)
        lefth(root.left)
        leaves(root.left)
        leaves(root.right)
        righth(root.right)
        
        return res
        
