先从所有的字符串里找到最短的
然后用最短的第一位开始，去对比所有字符串的每一位，如果碰见不相同的情况，则可以返回当前获得的长度，
当遍历完最短字符串后，可以将其直接返回

也可以用divide conquer 的方法来解决，分成两段，然后求出每段的最长prefix，然后比较两个

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
        
        
        
        
        
