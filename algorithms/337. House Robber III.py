# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """   
        if not root:
            return 0
        def dfs(root):
            if not root:
		        return 0,0
            right=dfs(root.right)
            left=dfs(root.left)
            return max(left[0],left[1])+max(right[0],right[1]),root.val+left[0]+right[0]
        use,use_no = dfs(root)
        return max(use,use_no)
