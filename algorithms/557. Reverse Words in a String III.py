class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        ls = s.split()
        return ' '.join(map(lambda x:x[::-1],ls))
