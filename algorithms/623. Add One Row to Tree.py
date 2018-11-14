class Solution:
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        def helper(node, depth):
            if depth == 1:
                left_side, right_side = node.left, node.right
                node.left, node.right = TreeNode(v), TreeNode(v)
                node.left.left, node.right.right = left_side, right_side
            else:
                if node.left:
                    node.left = helper(node.left,  depth - 1)
                if node.right:
                    node.right = helper(node.right, depth - 1)
            return node
        
        if root:
            if d == 1:
                output = TreeNode(v)
                output.left = root
                root = output
            else:
                helper(root, d - 1)
        return root
