"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        # if not root:
        #     return []
        # res = []
        # def helper(root,res):
        #     res.append(root.val)
        #     for child in root.children:
        #         helper(child,res)
        # helper(root,res)
        # return res
        if not root:
            return []
        res = []
        stack = [root]
        while stack:
            cur = stack.pop()
            res.append(cur.val)
            for child in cur.children[::-1]:
                stack.append(child)
        return res
       
            
            
        
