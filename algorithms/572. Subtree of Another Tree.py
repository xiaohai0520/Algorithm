class Solution:
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not s:
            return False
        return self.isSame(s,t) or self.isSubtree(s.left,t) or self.isSubtree(s.right,t)
        
        
    def isSame(self,t1,t2):
        if not t1 and not t2:
            return True

        if t1 and t2 and t1.val == t2.val:
            return self.isSame(t1.left,t2.left) and self.isSame(t1.right,t2.right)     
        else:
            return False
