#dic or arry 

class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic1 = {}
        dic2 = {}
        
        for c in s:
            dic1[c] = dic1.get(c,0) + 1
        for c in t:
            dic2[c] = dic2.get(c,0) + 1
        return dic1 == dic2
