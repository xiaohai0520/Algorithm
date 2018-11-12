class Solution:
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        def preorder(root):
            if root is None:
                return ""
            s=str(root.val)
            l=preorder(root.left)
            r=preorder(root.right)
            if r=="" and l=="":
                return s 
            elif l=="":
                s+="()"+"("+r+")"
            elif r=="":                
                s+="("+l+")"
            else :   
                s+="("+l+")"+"("+r+")"
            return s
        return preorder(t)
