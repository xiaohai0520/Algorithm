## 114. Flatten Binary Tree to Linked List

### 题目分析
flat一棵二叉树。

要求是不招用额外空间。


### 解法

思路是left flatten之后接在root右侧，然后right接在left flatten后面。

那么我们先处理right,然后处理left,然后接在一起。

因为我们一直要连接到之前的一个node,用一个全局变量来记录之前处理的node。

时间复杂度O(n)

空间复杂度O(1)

### 代码
```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def __init__(self):
        self.prev = None
    
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        self.flatten(root.right)
        self.flatten(root.left)
        

        root.right = self.prev
        root.left = None
        self.prev = root

```
