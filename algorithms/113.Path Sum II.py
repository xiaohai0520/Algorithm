# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(root,sum,[],res)
        return res
        
    def dfs(self,root,target,path,res):
        if not root:
            return
        if (sum(path) + + root.val) == target and not root.left and not root.right:
            res.append(path+[root.val])
            return
        self.dfs(root.left,target,path+[root.val],res)
        self.dfs(root.right,target,path+[root.val],res)
        
