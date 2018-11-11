"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        # if not root:
        #     return []
        # res = []
        # def helper(root,res):
        #     for child in root.children:
        #         helper(child,res)
        #     res.append(root.val)
        # helper(root,res)
        # return res
        
        res = []
        stack = [root]
        while stack:
            cur = stack.pop()
            if cur:
                
                res.append(cur.val)
                stack.extend(cur.children)
        return res[::-1]
            
            
            
            
            
            
            
            
