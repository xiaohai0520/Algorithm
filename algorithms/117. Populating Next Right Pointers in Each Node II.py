# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

from collections import deque
class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return 
        queue = deque([root])
        n = len(queue)
        while queue:
            for i in range(n):
                cur = queue.popleft()
                if i == n - 1:
                    cur.next = None
                else:
                    cur.next = queue[0]
                if cur.left:
                    queue.append(cur.left) 
                if cur.right:
                    queue.append(cur.right)
         
            n = len(queue)
                    
                    
                
        
