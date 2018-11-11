"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []
        import collections
        queue = collections.deque([root])
        count = 1
        res = []
        while queue:
            ls = []
            for i in range(count):
                cur = queue.popleft()
                ls.append(cur.val)
                if cur.children:
                    queue.extend(cur.children)
            res.append(ls)
            count = len(queue)
        return res
