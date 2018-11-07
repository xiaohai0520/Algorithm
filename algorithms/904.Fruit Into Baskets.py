#sliding window
class Solution:
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        l = res = 0
        dic = {}
        for i in range(len(tree)):
            if tree[i] in dic:
                dic[tree[i]] += 1
            else:
                dic[tree[i]] = 1
            
            while len(dic) > 2:
                dic[tree[l]] -= 1
                if not dic[tree[l]]:
                    del dic[tree[l]]
                l += 1
            res = max(res,i-l+1)
        return res
        
