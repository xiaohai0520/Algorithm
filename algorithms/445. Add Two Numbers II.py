# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#use stack from back to front


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        stack1 = []
        stack2 = []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        dummy = ListNode(0)
        carry = 0
        while stack1 or stack2:
            s1 = 0
            s2 = 0
            if stack1:
                s1 = stack1.pop() 
            if stack2:   
                s2 = stack2.pop() 
            
            s3 = (s1 + s2 + carry)%10
            carry = (s1 + s2 + carry)//10
            dummy.val = s3
            pre = ListNode(carry)
            pre.next = dummy
            dummy = pre
   
        return dummy if carry else dummy.next
            
            
            
            
        
        
