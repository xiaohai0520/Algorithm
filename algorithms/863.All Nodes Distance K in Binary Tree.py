#set par and use bfs

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        def dfs(node, par = None):
            if node:
                node.par = par
                dfs(node.left, node)
                dfs(node.right, node)

        dfs(root)

        queue = collections.deque([(target, 0)])
        seen = {target}
        while queue:
            if queue[0][1] == K:
                return [node.val for node, d in queue]
            node, d = queue.popleft()
            for nei in (node.left, node.right, node.par):
                if nei and nei not in seen:
                    seen.add(nei)
                    queue.append((nei, d+1))

        return []
        
        
        
#         def findnodes(root,steps):
#             if not root:
#                 return
#             if steps == 0:
#                 res.append(root.val)
#                 return
#             findnodes(root.left,steps-1)
#             findnodes(root.right,steps-1)
        
        
#         if not root:
#             return 
#         res = []
#         if root.left:
#             if root.left.val == target:
#                 findnodes(root.left,k)
#                 findnodes(root,k-1)
#             else:
#                 self.distanceK(root.left,target,K)
#         if root.right:
#             if root.right.val == target:
#                 findnodes(root.right,K)
#                 findnodes(root.left,K-1)
#             else:
#                 self.distanceK(root.right,target,K)
#         return res
                
                
                
                
        
