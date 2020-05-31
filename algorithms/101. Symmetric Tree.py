## 101. Symmetric Tree

### 题目分析
判断两棵树是否是镜像的

### 解法
分别去对比left和right。

时间复杂度 O（n）

空间复杂度 O（1）


### 代码
```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        def helper(p,q):
            if not p and not q:
                return True
            elif not p or not q:
                return False
            else:
                return p.val == q.val and helper(p.left,q.right) and helper(p.right,q.left)
        return helper(root.left,root.right)
```
