# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        fbts = [[] for i in range(N + 1)]
        fbts[1] = [TreeNode(0)]
        for i in range(2, N + 1):
            for j in range(i):
                leftnodes = j
                rightnodes = i - 1 - j
                lefttrees = fbts[leftnodes]
                rightrees = fbts[rightnodes]
                if lefttrees != [] and rightrees != []:
                    for ltree in lefttrees:
                        for rtree in rightrees:
                            root = TreeNode(0)
                            root.left = ltree
                            root.right = rtree
                            fbts[i].append(root)
        return fbts[N]
