# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        con = collections.defaultdict(list)
        def set_map(root,child):
            if root and child:
                con[root.val].append(child.val)
                con[child.val].append(root.val)
            if child.left:
                set_map(child,child.left)
            if child.right:
                set_map(child,child.right)
        set_map(None,root)
        bfs = [target.val]
        seen = set(bfs)
        for i in range(K):
            bfs = [y for x in bfs for y in con[x] if y not in seen]
            seen |= set(bfs)
        return bfs
                
