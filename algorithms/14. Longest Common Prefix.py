# try every char

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        shortest = min(strs,key=len)
        for i, ch in enumerate(shortest):
            for other in strs:
                if other[i] != ch:
                    return shortest[:i]
        return shortest
        
        
        @another merge
#         if not strs:
#             return ''
#         if len(strs) == 1:
#             return strs[0]
#         h1 = self.longestCommonPrefix(strs[:len(strs)//2])
#         h2 = self.longestCommonPrefix(strs[len(strs)//2:])
#         return self.merge(h1,h2)
        
#     def merge(self,h1,h2):
#         i = 0
#         while i < len(h1) and i < len(h2) and h1[i] == h2[i]:
#             i +=1
#         return h1[:i]
        
        
        
        
        
