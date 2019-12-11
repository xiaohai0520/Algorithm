使用递归的思想比较方便解题

base condition 是当链表为null  或者只有一个的时候，返回本身即可

每次讲第一个 第二个 第三个进行保存，然后 第二个指向第一个，第一个指向递归回来的第三个，
最终返回第二个

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
