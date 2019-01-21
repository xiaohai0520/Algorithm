# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if not n:
            return []
        return self.createTree(1,n)
    
    def createTree(self,start,end):
        result = []
        
        if start > end:
            result.append(None)
            return result
        
        for i in range(start,end+1):
            leftc = self.createTree(start,i-1)
            rightc = self.createTree(i+1,end)
            
            for l in leftc:
                for r in rightc:
                    root = TreeNode(i)
                    root.left = l
                    root.right = r
                    result.append(root)
        return result
