#sliding windows
class Solution:
    
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        res = []
        dic1 = collections.Counter(p)
        dic2 = collections.Counter(s[:len(p)-1])
        
        for i in range(len(p)-1,len(s)):
            dic2[s[i]] += 1
            
            if dic2 == dic1:
                res.append(i - len(p) + 1)
            dic2[s[i - len(p)+1]] -= 1
            if dic2[s[i - len(p)+1]] == 0:
                del dic2[s[i - len(p)+1]]
        return res
