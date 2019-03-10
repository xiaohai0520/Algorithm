"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
        if not root:
            return []
        stack = [root]
        res = []
        while stack:
            cur = stack.pop()
            res.append(cur.val)
            
            if cur.children:
                stack.extend(cur.children[::-1])
        return res
                
        
        
        # if not root:
        #     return []
        # res = []
        # def helper(node):
        #     if not node:
        #         return
        #     res.append(node.val)
        #     for n in node.children:
        #         helper(n)
        # helper(root)
        # return res
            
