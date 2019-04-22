This is a tree problem.

We use the from the down to the top.

base condition is if not root: return 0

other return the number we need 

each step the res need to add the needed number.



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        def dfs(root):
            if not root:
                return 0
            l,r = dfs(root.left),dfs(root.right)
            self.res += abs(l) + abs(r) 
            return root.val + l + r - 1
        
        dfs(root)
        return self.res
