#use deque to pop first and second , then append into tail,until only 1


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from collections import deque

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
       if len(lists) == 0:
            return None
        q = deque(lists)
        while len(q) != 1:
            first = q.popleft()
            second = q.popleft()
            head = tail = ListNode(0) 
            while first != None and second != None:
                if first.val < second.val:
                    tail.next, tail = first, first
                    first, tail.next = first.next, None
                else:
                    tail.next, tail = second, second
                    second, tail.next = second.next, None
            if first != None:
                tail.next = first
            if second != None:
                tail.next = second
            q.append(head.next)
        return q.popleft()
