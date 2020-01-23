字典key可以是tuple,将每个单词拆解排序变tuple，存入字典

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = collections.defaultdict(list)
        for each in strs:
            dic[tuple(sorted(each))].append(each)
        return list(dic.values())
