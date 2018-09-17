
#slidng windows

class Solution:
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        #sliding window

        n = len(s1)
        target = [0] * 26
        window = [0] * 26
        for c in s1:
            target[ord(c) - ord('a')] += 1 
        for i,c in enumerate(s2):
            window[ord(c) - ord('a')] += 1
            
            if i >= n:
                window[ord(s2[i-n]) - ord('a')] -= 1
            if window == target:
                return True
        return False
