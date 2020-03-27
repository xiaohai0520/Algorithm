# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        
        self.res = 0
        
        def dfs(node):
            if not node:
                return 0,0
            ll,lr = dfs(node.left)
            rl,rr = dfs(node.right)
            self.res = max(self.res,lr,rl)
            return lr + 1,rl + 1
        
        dfs(root)
        return self.res
            

             
        
#         res = 0
#         q = deque([(root, 0, 0)])
        
#         while q:
#             node, left, right = q.popleft()
#             res = max(res, left, right)
#             if node.left:
#                 q.append((node.left, 0, left + 1))
#             if node.right:
#                 q.append((node.right, right + 1, 0))
        
#         return res
