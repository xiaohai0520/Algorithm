# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        dic = {}

        
        def helper(root):
            if not root:
                return 0
            if not root.left and not root.right:
                dic[root.val] = dic.get(root.val,0) + 1
                return root.val
            
            cur_val = root.val + helper(root.left) + helper(root.right)
            dic[cur_val] = dic.get(cur_val,0) + 1
 
            return cur_val
        helper(root)
        res = []
        
        times = max(dic.values())
        for key,value in dic.items():
            if value == times:
                res.append(key)
        return res
        
