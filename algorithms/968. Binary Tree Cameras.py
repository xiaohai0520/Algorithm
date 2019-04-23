This is a tree problem

We start from the bottom to the up.

we mark leaf 0, leaf's pre 1 ; leaf's pre pre 2

we only want to add camera on the 1

so l,r has 2 return 0

if l,r has 0 ,add 1 ,return 1

if l ,r has 1, return 2

code:

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minCameraCover(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        def dfs(root):
            if not root:
                return 2
            l,r = dfs(root.left),dfs(root.right)
            if l == 0 or r == 0:
                self.res += 1
                return 1
            elif l == 1 or r == 1:
                return 2
            else:
                return 0
        
        return (dfs(root) == 0) + self.res
