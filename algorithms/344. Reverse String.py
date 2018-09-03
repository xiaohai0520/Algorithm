class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        i,j = 0,len(s)-1
        cur = list(s)
        while i < j:
            cur[i],cur[j] = cur[j],cur[i]
            i += 1
            j -= 1
        return ''.join(cur)
