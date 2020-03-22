# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        cur = []
        def dfs(root):
            if not root:
                return 
            dfs(root.left)
            cur.append(root.val)
            dfs(root.right)
        
        dfs(root)
        
        def bbt(ls):
            if not ls:
                return None
            l = len(ls)
            root = TreeNode(ls[l//2])
            root.left = bbt(ls[:l//2])
            root.right = bbt(ls[l//2+1:])
            return root
        return bbt(cur)
