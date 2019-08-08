class Solution(object):
    def reverseWords(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        def reverse(l,r):
            while l < r:
                s[l],s[r] = s[r],s[l]
                l += 1
                r -= 1
        
        reverse(0,len(s)-1)
        l = r = 0
        while r < len(s):
            if s[r] == ' ':
                reverse(l,r-1)
                l = r + 1
            elif r == len(s) - 1:
                reverse(l,r)
            r += 1
        
