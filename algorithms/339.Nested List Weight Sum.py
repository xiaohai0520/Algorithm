# recursive and iterator with stack



"""
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution(object):
    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        # if not nestedList:
        #     return 0
        # res = 0
        # stack = []
        # for l in nestedList:
        #     stack.append((l,1))
        # while stack:
        #     next, d = stack.pop(0)
        #     if next.isInteger():
        #         res += d * next.getInteger()
        #     else:
        #         for cl in next.getList():
        #             stack.append((cl,d+1))
        # return res
        return self.dfs(nestedList)
        
    def dfs(self, List, depth=1):
        sum = 0
        for i in List:
            if i.isInteger():
                sum += i.getInteger() * depth
            else:
                sum += self.dfs(i.getList(), depth + 1)
        return sum

        
        
        
        
        
        
        
        
        
        
        
