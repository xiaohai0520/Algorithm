先查一下总长度，如果总长度小于K， 那么我们不需要进行操作

每次都反转前k个node，然后将原来的head指向 剩余部分的反转，

最后返回尾部的node

时间复杂度O（n）


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
