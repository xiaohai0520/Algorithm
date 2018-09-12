#dfs

class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        nums = set([str(x) for x in range(0, 256)])
        self.helper(s,[],res,0,nums)
        return list(map(lambda x: '.'.join(x), res))

    def helper(self, s, path, res, i, nums):
        if not s and i == 4:
            res.append(path)
            return
        if i == 4 and s:
            return
        for j in range(0, 3):
            if s[:j+1] in nums and len(s) >= j+1:
                self.helper(s[j + 1:], path + [s[:j+1]], res, i + 1, nums)
