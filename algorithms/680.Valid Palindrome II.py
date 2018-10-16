#O(n) time 

class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
#         return self.helper(s,0)
    
#     def helper(self,s,la):
#         l,r = 0,len(s) - 1
#         while l < r:
#             if s[l] == s[r]:
#                 l += 1
#                 r -= 1
#             else:
#                 if la == 0:
#                     return self.helper(s[l:r],la+1) or self.helper(s[l+1:r+1],la+1)
#                 else:
#                     return False
#         return True
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                remove_j, remove_i = s[l:r], s[l + 1:r + 1]
                return remove_j == remove_j[::-1] or remove_i == remove_i[::-1]
            l, r = l + 1, r - 1
        return True   
