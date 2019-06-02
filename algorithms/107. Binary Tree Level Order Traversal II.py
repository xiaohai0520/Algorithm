# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        import collections
        res = []
        queue = collections.deque([root])
        count = 1
        while queue:
            ls = []
            for i in range(count):
                cur = queue.popleft()
                ls.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            
            res.append(ls)
            count = len(queue)
        return res[::-1]

    
