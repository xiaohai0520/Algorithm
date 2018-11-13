# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
#         bfs
        import collections
        queue = collections.deque([root])
        res = None
        count = 1
        while queue:
            for i in range(count):
                cur = queue.popleft()
                if i == 0:
                    res = cur.val
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            count = len(queue)
        return res
