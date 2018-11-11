# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if not root:
            return []
        
        
        import collections
        
        queue = collections.deque([root])
        count = 1
        res = []
        while queue:
            sum = 0
            for i in range(count):
                cur = queue.popleft()
                sum += cur.val
                if cur.left:
                    
                    queue.append(cur.left) 
                if cur.right:
                    
                    queue.append(cur.right) 
            
            
            res.append(sum/float(count))
            
            count = len(queue)
            
        return res
