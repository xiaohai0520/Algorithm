# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        
        if not root:
            return 0
        self.num = 0
        self.dic = {0:1}
        self.helper(root,0,sum)
        return self.num
        
    def helper(self,root,path,target):
        if not root:
            return 0
        path += root.val
        old = path - target
        self.num += self.dic.get(old,0)
        self.dic[path] = self.dic.get(path,0) + 1
        self.helper(root.left,path,target)
        self.helper(root.right,path,target)
        self.dic[path] -= 1
