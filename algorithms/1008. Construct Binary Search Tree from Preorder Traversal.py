# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        cur = preorder.pop(0)
        
        left = [i for i in preorder if i < cur] if preorder else []
        right = [i for i in preorder if i > cur] if preorder else []
        
        root = TreeNode(cur)
        root.left = self.bstFromPreorder(left)
        root.right = self.bstFromPreorder(right)
        
        return root
        
