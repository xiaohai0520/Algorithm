#logn if %2 x*pow(x,n-1)    else  pow(x*x,n/2)

class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if n < 0:
            return self.myPow(x,-n)
        if n%2:
            return x * self.myPow(x, n-1)
        else:
            return self.myPow(x*x,n/2)
        
