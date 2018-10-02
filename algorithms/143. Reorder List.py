# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
#     def reorderList(self, head):
#         """
#         :type head: ListNode
#         :rtype: void Do not return anything, modify head in-place instead.
#         """
#         # fast = slow = head
#         # while fast and fast.next:
#         #     fast = fast.next.next
#         #     slow = slow.next
              
            if not head:
                return

            # find the mid point
            slow = fast = head 
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next

            # reverse the second half in-place
            pre, node = None, slow
            while node:
                pre, node.next, node = node, pre, node.next

            # Merge in-place; Note : the last node of "first" and "second" are the same
            first, second = head, pre
            while second.next:
                first.next, first = second, first.next
                second.next, second = first, second.next
