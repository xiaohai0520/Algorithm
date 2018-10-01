#use dic to clone this graph


# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []
from collections import deque

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if node == None:
            return None
        q = deque([node])
        dic = {}
        while len(q) != 0:
            tmp = q.popleft()
            dic[tmp] = UndirectedGraphNode(tmp.label)
            for neighbor in tmp.neighbors:
                if neighbor not in dic:
                    q.append(neighbor)
        for origin, clone in dic.items():
            for neighbor in origin.neighbors:
                clone.neighbors.append(dic[neighbor])
        return dic[node]
