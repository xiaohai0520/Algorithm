#find the half of the list
#reverse latter half to match 



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # cur = head
        # pre = None
        # while cur:
        #     cur.next,pre,cur = pre,cur,cur.next
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        if fast:
            slow = slow.next
        pre = None
        
        while slow:
            slow.next,pre,slow = pre,slow,slow.next
        while head and pre:
            if head.val != pre.val:
                return False
            head = head.next
            pre = pre.next
        return True
        
        
        
        
