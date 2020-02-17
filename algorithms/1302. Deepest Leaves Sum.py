# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        if not root:
            return
        res = 0
        queue = collections.deque([root])
        l = 1
        while queue:
            layer = 0
            for _ in range(l):
                cur = queue.popleft()
                layer += cur.val
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            res = layer
            l = len(queue)
        return res
            
