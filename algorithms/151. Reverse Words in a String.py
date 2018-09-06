
#split into each char and reverse
#reverse each word in the list and join together

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        s = list(" ".join(s.split()))[::-1]
        i = 0
        while i < len(s):
            start = i
            while i < len(s) and not s[i].isspace():
                i += 1
            self.reverse(s,start,i-1)
            i += 1
        return ''.join(s) 
        
        
        
    def reverse(self,ls,i,j):
        while i < j:
            ls[i],ls[j] = ls[j],ls[i]
            i += 1
            j -= 1
