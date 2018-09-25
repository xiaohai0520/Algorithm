#loop cross search 
#another method, cal the length  get equal length and start together



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        cura = headA
        curb = headB
        
        while cura is not curb:
            cura = headB if not cura else cura.next
            curb = headA if not curb else curb.next
        return cura
