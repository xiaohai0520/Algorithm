# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        # if not root.left and not root.right: 
        #     return chr(root.val + 97)
        # elif not root.left: 
        #     return self.smallestFromLeaf(root.right) + chr(root.val + 97)
        # elif not root.right: 
        #     return self.smallestFromLeaf(root.left) + chr(root.val + 97)
        # l, r = self.smallestFromLeaf(root.left), self.smallestFromLeaf(root.right)
        # return sorted([l,r])[0] + chr(root.val + 97)
        
                
        if not root:
            return ''
        chars = list(string.ascii_lowercase)
        res = []
        def dfs(root,cur):
            if not root:
                return
            if not root.left and not root.right:
                res.append(chars[root.val] + cur)
            dfs(root.left,chars[root.val] + cur)
            dfs(root.right,chars[root.val] + cur)
        dfs(root,'')
        res.sort()
        return res[0]
