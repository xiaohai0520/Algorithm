#use dic  get tuple of list for key and list of string for values

class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for str in strs:
            key = tuple(sorted(str))
            if key not in dic:
                dic[key] = [str]
            else:
                dic[key] = dic[key] + [str]
        return list(dic.values())
                
