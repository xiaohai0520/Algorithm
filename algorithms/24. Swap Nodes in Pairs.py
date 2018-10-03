# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
#         dummy = p = ListNode(0)
#         dummy.next = head
#         while head and head.next:
#             second = head.next
#             head.next = second.next
#             second.next = head
#             p.next = second
#             head = head.next
#             p = second.next
            
#         return dummy.next
 
        if not head or not head.next:
            return head

        first,second = head, head.next
        third = second.next
        head = second
        second.next = first
        first.next = self.swapPairs(third)

        return head
