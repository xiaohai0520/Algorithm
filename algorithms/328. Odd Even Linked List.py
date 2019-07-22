# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        l1, l2, l3 = head, head.next, head.next
        
        while l1 and l2 and l1.next and l2.next:
            l1.next, l2.next = l1.next.next, l2.next.next
            l1, l2 = l1.next, l2.next
        
        l1.next = l3
        
        return head
        
