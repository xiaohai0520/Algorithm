# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        x = 0
        for i in range(n):
            if knows(x, i):
                x = i
        for i in range(n):
            if x != i and (knows(x,i) or !knows(i,x)):
                return -1
        return x
