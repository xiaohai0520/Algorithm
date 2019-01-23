# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        l1 = l2 = 0
        A = headA
        B = headB
        while A:
            A = A.next
            l1 += 1
        while B:
            B = B.next
            l2 += 1
        if l1 > l2:
            headA,headB = headB,headA
            l1,l2 = l2,l1
            
        for i in range(l2-l1):
            headB = headB.next
        while headA and headB:
            if headA is headB:
                return headA
            else:
                headA = headA.next
                headB = headB.next
        return None
            
