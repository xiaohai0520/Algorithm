

class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        dic = {}
        for c in s:
            dic[c] = dic.get(c, 0) + 1
        ls = [(k,v) for k,v in dic.items()]
        ls.sort(key=lambda x:-x[1])
        res = ''
        for pair in ls:
            res += pair[1]*pair[0]
        return res
