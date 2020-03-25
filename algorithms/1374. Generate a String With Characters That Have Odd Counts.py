class Solution:
    def generateTheString(self, n: int) -> str:
        if n == 0:
            return ''
        if n == 1:
            return 'a'
        if n%2 == 0:
            return 'a'* (n - 1) + 'b'
        else:
            return self.generateTheString(n-1) + 'c'
