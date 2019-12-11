利用两个指针，快的指针先前进n步，然后跟慢指针一起前进，知道快指针没有下一个
trick的地方是如果n是链表的长度，那么第一个node需要被删除，那么我们需要用dummy来创造一个虚拟的head
当最后返回的时候return  dummy.next

#two pointers


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        fast = slow = dummy
        for _ in range(n):
            fast = fast.next
        while fast and fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next        
