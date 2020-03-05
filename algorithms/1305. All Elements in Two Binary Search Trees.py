# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        res = []
        l1 = []
        l2 = []
        while root1:
            l1.append(root1)
            root1 = root1.left
        while root2:
            l2.append(root2)
            root2 = root2.left
        
        while l1 or l2:
            if not l1:
                s = l2
            elif not l2:
                s = l1
            else:
                if l1[-1].val < l2[-1].val:
                    s = l1
                else:
                    s = l2
            
            cur = s.pop()
            res.append(cur.val)
            cur = cur.right
            while cur:
                s.append(cur)
                cur = cur.left
        return res
