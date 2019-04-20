This is a tree dfs or bfs problem.

we can solve it in recursive or iterative.

return parent and depth every time.


code:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        
        
        
        
        def dfs(root,depth,pre,target,find):
            if not root:
                return 
            if root.val == target:
                find.append(pre)
                find.append(depth)
            dfs(root.left,depth+1,root,target,find)
            dfs(root.right,depth+1,root,target,find)
        
        ls1 = []
        ls2 = []
        dfs(root,0,None,x,ls1)
        dfs(root,0,None,y,ls2)
        return ls1[0] != ls2[0] and ls1[1] == ls2[1]
