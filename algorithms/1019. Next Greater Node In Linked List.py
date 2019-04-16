This problem can be solve by stack in O(n).

When we meet the linked list or array,we can always think of stack.

Stack can save the previous numbers.

We just need to save these number into stack, and compare them with the next node val

if  no number later larger than number in stack, it means 0.

Code:


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        if not head:
            return []
        if not head.next:
            return [0]
        
        
        res,stack = [],[]
        
        while head:
            
            while stack and stack[-1][1] < head.val:
                res[stack.pop()[0]] = head.val
            stack.append((len(res),head.val))
            res.append(0)
            head = head.next
        return res
        
        
        
        
        
        
        
        
        
        
        
        
        
        # if not head:
        #     return []
        # if not head.next:
        #     return [0]
        # cur = []
        # while head:
        #     cur.append(head.val)
        #     head= head.next
        # res = []
        # for i in range(len(cur)-1):
        #     for j in range(i+1,len(cur)):
        #         if cur[j] > cur[i]:
        #             res.append(cur[j])
        #             break
        #     if len(res) < i + 1:
        #         res.append(0)
        # return res + [0]
            
