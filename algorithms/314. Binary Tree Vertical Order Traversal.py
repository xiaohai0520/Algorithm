#not need to think about the row ,bfs always from top to bottom

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections
class Solution:
    
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        node_dict = collections.defaultdict(list)
        Q = collections.deque([(root, 0)])
        
        while Q:
            node, level = Q.popleft()
            if not node:
                continue
            node_dict[level].append(node.val)
            Q.append((node.left, level-1))
            Q.append((node.right, level+1))
        
        return [node_dict[x] for x in sorted(node_dict)]
        
        
#         if not root:
#             return []
#         ls = []
#         stack = [(root,0,0)]
#         while stack:
#             cur,row,col = stack.pop(0)
#             ls.append((cur.val,row,col))
#             if cur.left:
#                 stack.append((cur.left,row+1,col-1))
#             if cur.right:
#                 stack.append((cur.right,row+1,col+1))
                
#         ls.sort(key=lambda x : (x[-1],x[1]))
#         pre = ls[0][-1]
#         res = []
#         cur = []
#         for node in ls:
#             if node[-1] == pre:
#                 cur.append(node[0])
#             else:
#                 res.append(cur)
#                 pre = node[-1]
#                 cur = [node[0]]
#         res.append(cur)
#         return res
            
