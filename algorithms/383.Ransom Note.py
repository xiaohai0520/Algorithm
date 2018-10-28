class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        dic = collections.Counter(magazine)
        for c in ransomNote:
            if c in dic:
                dic[c] -= 1
                if dic[c] == 0:
                    del dic[c]
            else:
                return False
        return True
        
