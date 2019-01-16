# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return []
        import collections
        
        queue = collections.deque(lists)
        while len(queue) != 1:
            l1 = queue.popleft()
            l2 = queue.popleft()
            l = self.helper(l1,l2)
            queue.append(l)
        return queue.popleft()
    
    
    
    def helper(self,l1,l2):
        dummy = cur = ListNode(0)
        while l1 and l2:
            v1 = l1.val
            v2 = l2.val
            if v1 < v2:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
            
        if l1:
            cur.next = l1
        if l2:
            cur.next = l2
        return dummy.next
            
