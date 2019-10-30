# 两个链表，取一个dummy node 作为结果的head， 然后去逐渐处理两个链表的每一位
# 如果和超过10，则使用flag 记为1并且加入下一位， 如果两个链表都用完了，flag还是1， 注意再填一位



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        flag = 0
        dummy = cur = ListNode(0)
        while l1 or l2 or flag:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            flag,val = divmod(v1+v2+flag,10)
            cur.next = ListNode(val)
            cur = cur.next
        return dummy.next
