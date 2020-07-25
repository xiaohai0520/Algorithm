# 拓扑排序

拓扑排序跟BFS非常类似，但有一些自己的限制条件，粗略的考虑成是带有筛选条件的BFS。

有向无环图（DAG）才有拓扑排序，非DAG图没有拓扑排序一说。


## 1.总体概述
**场景：** 工期排序、大小关系排列

## 2.拓扑框架
```
def topo():
  create DAG and calculate degree
  choose start point (indegree = 0)
  res = []
  while queue:
    cur = queue.popleft()
    res.append(cur)
    for each in cur.next:
       update each degree
       if degree == 0:
          queue.append(each)
  return res
  
```

## 3.具体思路

在图论中，拓扑排序（Topological Sorting）是一个有向无环图（DAG, Directed Acyclic Graph）的所有顶点的线性序列。且该序列必须满足下面两个条件：

1.每个顶点出现且只出现一次。

2.若存在一条从顶点 A 到顶点 B 的路径，那么在序列中顶点 A 出现在顶点 B 的前面。



它是一个 DAG 图，那么如何写出它的拓扑排序呢？这里说一种比较常用的方法：

1.从 DAG 图中选择一个 没有前驱（即入度为0）的顶点并输出。

2.从图中删除该顶点和所有以它为起点的有向边。

3.重复 1 和 2 直到当前的 DAG 图为空或当前图中不存在无前驱的顶点为止。后一种情况说明有向图中必然存在环。

