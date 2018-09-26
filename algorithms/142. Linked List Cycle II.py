#Assume the first pointer runs from head at a speed of 1-by-1 step, as S, and the second pointer runs at a speed of 2-by-2 step, as 2S, then two pointers will meet at MEET-POINT, using the same time. Define outer loop is A, the distance from CIRCLE-START-POINT to MEET-POINT is B, and the distance from MEET-POINT to CIRCLE-START-POINT is C (Apparently, C=loop-B), then (n*loop+a+b)/2S = (a+b)/S, n=1,2,3,4,5,....

#Converting that equation can get A/S=nloop/S-B/S. Since C=loop-B, get A/S = ((n-1)loop+C)/S.

#That means, as second step, assuming a pointer running from head and another pointer running from MEET-POINT both at a speed S will meet at CIRCLE-START-POINT


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast is slow:
                break
        if not fast or not fast.next:
            return None
        while head is not slow:
            head = head.next
            slow = slow.next
        return head
