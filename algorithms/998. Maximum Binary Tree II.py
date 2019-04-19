The tree problem.

the number add at the at position, if the number larger than the root, previous tree be the left node

else left no need change , recursive it into the right part.

Code:


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoMaxTree(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        if val > root.val:
            node = TreeNode(val)
            node.left = root
            return node
        else:
            root.right = self.insertIntoMaxTree(root.right,val)
            return root
