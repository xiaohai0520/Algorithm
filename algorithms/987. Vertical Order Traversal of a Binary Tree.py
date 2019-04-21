This is a dfs and tree problem.

use a double dict and save the dic[x][y] :list

give the x sorted, and y sorted and add the sorted(dic[x][y]) is OK.

Code:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        dic = collections.defaultdict(lambda: collections.defaultdict(list))
        
        def dfs(root,x,y):
            if not root:
                return
            dic[x][y].append(root.val)
            dfs(root.left,x-1,y+1)
            dfs(root.right,x+1,y+1)
        
        
        dfs(root,0,0)
        res = []
        for x in sorted(dic.keys()):
            cur = []
            for y in sorted(dic[x].keys()):
                cur.extend(sorted(dic[x][y]))
            res.append(cur)
        return res
        
   
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
                
#         ls.sort(key=lambda x : (x[-1],x[1],x[0]))
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
            
