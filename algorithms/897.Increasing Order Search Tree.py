## 897. Increasing Order Search Tree


### 题目分析
一颗BST，我们要把它变成一棵连续递增的树，每棵树只有right child。

### 解法
我们只要inorder这棵BST就可以让所有的点递增。

### 代码
```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        
        dummy = self.node = TreeNode(0)
        
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            self.node.right = TreeNode(root.val)
            self.node = self.node.right
            dfs(root.right)
        dfs(root)
        return dummy.right
        
```

另一种dfs的代码
```
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        return self.helper(root,None)
        
    def helper(self,root,tail):
        if not root:
            return tail
        res = self.helper(root.left,root)
        root.left = None
        root.right = self.helper(root.right,tail)
        return res
 ```       
