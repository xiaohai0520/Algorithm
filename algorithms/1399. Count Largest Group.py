class Solution:
    def countLargestGroup(self, n: int) -> int:
        dic = collections.defaultdict(int)
        for i in range(1,n+1):
            
            key = sum([int(n) for n in str(i)])
            dic[key] += 1
        max_value = max(list(dic.values()))
        res = 0
        for each in dic:
            if dic[each] == max_value:
                res += 1
        return res
