# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur1 = l1
        cur2 = l2
        len1 = 0
        len2 = 0
        while cur1:
            len1 += 1
            cur1 = cur1.next
        while cur2:
            len2 += 1
            cur2 = cur2.next
        
        
        def helper(l1,l2,len1,len2):
            
            if len1 == 1 and len2 == 1:
                val = l1.val + l2.val
                flag,val = divmod(val,10)
                return ListNode(val),flag
            
            val = 0
            if len2 > len1:
                l1,l2 = l2,l1
                len1,len2 = len2,len1
            v1 = v2 = 0
            
            if len1 == len2:
                v1 = l1.val
                v2 = l2.val
                cur,flag = helper(l1.next,l2.next,len1-1,len2-1)
            else:
                v1 = l1.val
                v2 = 0
                cur,flag = helper(l1.next,l2,len1-1,len2)
               
            val = v1 +v2 + flag
            flag,val = divmod(val,10)
            new = ListNode(val)
            new.next = cur
            return new,flag
        
        res,flag = helper(l1,l2,len1,len2) 
        if flag:
            cur = ListNode(flag)
            cur.next = res
            return cur
        return res
                
        
        # def helper(l1,l2,len1,len2):
        #     if not l1 and not l2:
        #         return ListNode(0)

        #     val = 0
        #     if len1 == len2:
        #         next = helper(l1.next,l2.next,len1-1,len2-1)
        #         val = l1.val + l2.val + next.val
        #     else:
        #         next = helper(l1.next,l2,len1-1,len2)
        #         val = l1.val + next.val
        #     next.val = val%10
        #     val //= 10
        #     new = ListNode(val)
        #     new.next = next
        #     return new
        # res = helper(l1,l2,len1,len2)
        # return res.next if res.val == 0 else res
            











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
            
            
            
            
        
        
