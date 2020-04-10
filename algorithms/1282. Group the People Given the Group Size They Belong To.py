class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        dic = collections.defaultdict(list)
        for i,n in enumerate(groupSizes):
            dic[n].append(i)
        res = []
        for k in dic:
            ls = dic[k]

            for i in range(0,len(ls),k):

                res.append(ls[i:i+k])
        return res
                
