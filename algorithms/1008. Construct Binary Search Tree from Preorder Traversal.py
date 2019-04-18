A tree problem.

We think about the iteriative method.

We save the node in the stack, and if we meet the right value,find the its root through pop.

At last ,return the root.

Code:
    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
#         if not preorder:
#             return None
#         root = TreeNode(preorder[0])
#         l = [i for i in preorder[1:] if i < preorder[0]]
#         r = [i for i in preorder[1:] if i > preorder[0]]
        
#         root.left = self.bstFromPreorder(l)
#         root.right = self.bstFromPreorder(r)
        
#         return root


        root = TreeNode(preorder[0])
        stack = [root]
        for v in preorder[1:]:
            cur = TreeNode(v)
            if v < stack[-1].val:
                stack[-1].left = cur
            else:
                while stack and stack[-1].val < v:
                    p = stack.pop()
                p.right = cur
            stack.append(cur)
        
        return stack[0]
            
            
            
            
            
        
