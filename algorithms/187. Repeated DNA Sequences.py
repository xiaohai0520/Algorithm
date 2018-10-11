#two sets
class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        save = set()
        res = set()
        for i in range(len(s) - 9):
            if s[i:i+10] in save:
                res.add(s[i:i+10])
                continue
            save.add(s[i:i+10])
        return list(res)
        
