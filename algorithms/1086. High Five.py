class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        dic = collections.defaultdict(list)
        for item in items:
            dic[item[0]].append(item[1])
        res = []
        for i in sorted(dic.keys()):
            ls = sorted(dic[i],key=lambda x:-x)
            score = sum(ls[:5])//5
            res.append([i,score])
        return res
            
