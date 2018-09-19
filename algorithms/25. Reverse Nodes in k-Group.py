#use for to cal the times of reverse node


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        l = 0
        node = head
        while node:
            l += 1
            node = node.next
        if k <= 1 or l < k:
            return head
        pre, cur = None ,head
        
        for i in range(k):
            cur.next,pre,cur = pre,cur,cur.next
            
        head.next = self.reverseKGroup(cur,k)
        return pre
