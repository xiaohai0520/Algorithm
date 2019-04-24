This is a bfs question.

Because the tree is complete, so we check it in the order. from the left to right layer by layer

When we find the first None, it means it is the last node if the tree is complete.

If still have node not None, it is not a complete tree.

code:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        if not root:
            return True
        queue = collections.deque([root])
        while queue:
            cur = queue.popleft()
            # print(cur.val)
            
            if not cur: 
                if self.allNone(list(queue)):
                    return True
                else:
                    return False
            
            
            queue.append(cur.left)
            queue.append(cur.right)
            
    def allNone(self,ls):
        for node in ls:
            if node:
                return False
        return True
