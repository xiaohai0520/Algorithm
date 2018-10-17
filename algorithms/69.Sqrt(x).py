#log
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        l,r= 0,x
        while l <= r:
            mid = l + (r - l)//2
            if mid **2 <= x < (mid + 1)**2:
                return mid
            elif mid ** 2 > x:
                r = mid
            else:
                l = mid + 1
