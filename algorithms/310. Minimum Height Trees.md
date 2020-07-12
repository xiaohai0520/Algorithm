## 310. Minimum Height Trees

### 题目分析
对于一个没有环的图，我们可以想象成是一棵树，然后找到图中高度最小的树。即找到这个图中最中心的点。

### 解法

其实对于一个图来说，最中心的点分两种情况，一个或者两个。

我们用拓扑排序来逐层的去掉最外圈的叶子，然后当剩下两个或者两个以下的点的时候，就是最中心的点。

时间复杂度 O(n)

空间复杂度 O(n)

### 代码
```
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        graph = [[] for _ in range(n)]
        degree = [0] * n
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            degree[a] += 1
            degree[b] += 1
        cur = [i for i in range(n) if degree[i] == 1]
        while cur:
            nxt = []
            for node in cur:
                degree[node] -= 1
                for _node in graph[node]:
                    degree[_node] -= 1
                    if degree[_node] == 1:
                        nxt.append(_node)
            if not nxt: # if nxt is empty, it means cur is the result.
                return cur
            cur = nxt

```

