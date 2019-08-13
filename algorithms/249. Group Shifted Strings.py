class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        dic = collections.defaultdict(list)
        for st in strings:
            ls = list(st)
            ls = [(ord(x) - ord(ls[0]))%26 for x in ls]
            index = tuple(ls)
            dic[index] +=  [st]
        return list(dic.values())
