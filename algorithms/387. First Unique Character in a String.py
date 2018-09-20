class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return -1
        res = collections.Counter(s)
        cur = []
        for k,v in res.items():
            if v == 1:
                cur.append(k)
        ind = [s.index(x) for x in cur]
        if not ind:
            return -1
        return min(ind)
    
    
