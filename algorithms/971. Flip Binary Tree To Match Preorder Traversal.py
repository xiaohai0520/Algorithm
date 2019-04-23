This is a tree problem.

preorder array is root,left right 

every time we check next number, it gives the order dfs(left) and dfs(right)

if we find the first left is not equal ,we change to have a try.

but if when we arrive the left and the value is not equal we need to return False.


Code:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        res = []
        self.i = 0
        def dfs(root):
            if not root: 
                return True
            if root.val != voyage[self.i]: 
                return False
            self.i += 1
            if root.left and root.left.val != voyage[self.i]:
                res.append(root.val)
                root.left,root.right = root.right, root.left
            return dfs(root.left) and dfs(root.right)
        return res if dfs(root) else [-1]
