#dict   array  or zip set


class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
#         dic1,dic2 = {},{}
#         for i,c in enumerate(s):
#             dic1[c] = dic1.get(c,[]) + [i]
#         for i,c in enumerate(t):
#             dic2[c] = dic2.get(c,[]) + [i] 
            
#         return sorted(dic1.values()) == sorted(dic2.values())



        return len(set(zip(s, t))) == len(set(s)) == len(set(t))
            
