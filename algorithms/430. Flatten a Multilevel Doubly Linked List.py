"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        
        if not head: 
            return head
        self.getFlatten(head)
        return head
    def getFlatten(self, head):
        if head.child:
            childEnd = self.getFlatten(head.child)
            childEnd.next = head.next
            if head.next:
                head.next.prev = childEnd
            head.next = head.child
            head.child.prev = head
            head.child = None
            head = childEnd
        if not head.next:
            return head
        else:
            return self.getFlatten(head.next)
        
