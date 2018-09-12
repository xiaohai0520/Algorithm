class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """

        if m == n:
            return head
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        for i in range(m-1):
            pre = pre.next
        reverse = None
        cur = pre.next
        
        for i in range(n-m+1):
            cur.next,reverse,cur = reverse,cur,cur.next
            
        pre.next.next = cur
        pre.next = reverse
        return dummy.next
