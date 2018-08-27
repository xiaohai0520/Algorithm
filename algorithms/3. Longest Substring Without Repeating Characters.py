# literate for head to tail
# use dic to save the duplicate char's index 

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = start = 0
        used = {}
        
        for i in range(len(s)):
            if s[i] in used and start <= used[s[i]]:
                start = used[s[i]] + 1
            else:
                length = max(length, i - start + 1)
            used[s[i]] = i
        return length
               
        
        
        
        
        
        
        
        
        
        
