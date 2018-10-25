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
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        slow,fast = head,head.next.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        middle = slow.next
        slow.next = None
        # right = middle.next
        # middle.next = None
        root = TreeNode(middle.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(middle.next)
        return root
