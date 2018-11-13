# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        
        res = []
        count = 1
        import collections
        queue = collections.deque([root])
        while queue:
            ls = []
            for i in range(count):
                cur = queue.popleft()
                ls.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            res.append(max(ls))
            count = len(queue)
        return res
            
