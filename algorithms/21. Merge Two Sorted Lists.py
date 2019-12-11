合并链表

使用dummy 建立一个虚拟的头

然后对两个链表进行比较，将小的一个链到头的下一个，然后小的这个链表后移，继续比较

直到其中某一个链表到最后一个，最后讲剩余的链表加到尾部

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = tail = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                tail.next,tail = l1,l1
                l1, tail.next = l1.next, None
            else:
                tail.next, tail = l2, l2
                l2, tail.nexta = l2.next, None
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        return head.next
