#merge  divid into two  and sort

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        return self.quicksort(head)

    def quicksort(self, head):
        if not head:
            return

        dummyLeft = curLeft = ListNode(0)
        dummyRight = curRight = ListNode(0)
        dummyMid = curMid = head

        cur = head.next
        while cur:
            if cur.val == head.val:
                curMid.next = cur
                curMid = curMid.next
            elif cur.val < head.val:
                curLeft.next = cur
                curLeft = curLeft.next
            else:
                curRight.next = cur
                curRight = curRight.next
            cur = cur.next

        curMid.next = curLeft.next = curRight.next = None

        dummyLeft.next = self.quicksort(dummyLeft.next)
        dummyRight.next = self.quicksort(dummyRight.next)

        curLeft = dummyLeft
        while curLeft.next:
            curLeft = curLeft.next

        curLeft.next = head
        curMid.next = dummyRight.next
        return dummyLeft.next




class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        # divide list into two parts
        fast, slow = head.next, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        second = slow.next
        # cut down the first part
        slow.next = None
        l = self.sortList(head)
        r = self.sortList(second)
        return self.merge(l, r)

    # merge in-place without dummy node        
    def merge(self, l, r):
        if not l or not r:
            return l or r
        if l.val > r.val:
            l, r = r, l
        # get the return node "head"
        head = pre = l
        l = l.next
        while l and r:
            if l.val < r.val:
                l = l.next
            else:
                pre.next,r,pre.next.next = r,r.next,pre.next
            pre = pre.next
        # l and r at least one is None
        pre.next = l or r
        return head
