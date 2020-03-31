# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        def dfs(head,root):
            if not head:
                return True
            if not root:
                return False
            if root.val == head.val:
                return dfs(head.next,root.left) or dfs(head.next,root.right)
            return False
        
        if not head:
            return True
        if not root:
            return False
        return dfs(head,root) or self.isSubPath(head,root.left) or self.isSubPath(head,root.right)
