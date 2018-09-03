# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # cur, prev = head, None
        # while cur:
        #     cur.next, prev, cur = prev, cur, cur.next
        # return prev
        
        
        
        return self._reverse(head)
        
    def _reverse(self,cur,pre=None):
        if not cur:
            return pre
        n = cur.next
        cur.next = pre
        return self._reverse(n,cur)     
     
       
