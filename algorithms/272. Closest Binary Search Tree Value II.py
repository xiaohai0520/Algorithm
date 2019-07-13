# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from heapq import heappush,heappop
class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        
        


        dists = [ (-float('inf'),None) ] * k

        def traverse(root):
            if not root: 
                return

            negDist =  - abs(root.val - target)

            if negDist > dists[0][0]:
                heappop(dists)
                heappush(dists,(negDist,root.val))
            traverse(root.left);traverse(root.right)


        traverse(root)
        return [t[1] for t in dists]
