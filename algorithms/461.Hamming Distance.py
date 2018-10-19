use xor and &
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        m = x ^ y
        n = 0
        while(m):
            n += 1
            m &= m -1
        return n
