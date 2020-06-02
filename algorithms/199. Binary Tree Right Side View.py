## 199. Binary Tree Right Side View


### 题目分析
找到一棵树每层最右边的node。

### 解法

BFS， 一层一层的遍历，然后将每层最后一个加入结果集。

DFS，用先right后left的方法遍历，结果集的长度为层数，如果层数等于结果集长度，说明这个node是该层最后一个。


### 代码
BFS
```


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        res = []
        n = 1
        stack = collections.deque([root])
        while stack:
            for i in range(n):
                cur = stack.popleft()
                if i == n - 1:
                    res.append(cur.val)
                if cur.left:
                    stack.append(cur.left)
                if cur.right:
                    stack.append(cur.right)
            n = len(stack)
        return res
    
```
dfs
```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        
        def dfs(node,i):
            if not node:
                return 
            if i == len(res):
                res.append(node.val)
            dfs(node.right,i+1)
            dfs(node.left,i+1)
        
        dfs(root,0)
        return res
```
    
