class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if not wordList:
                return []
        
        wordList = set(wordList)
        res = []
        layer = {}
        layer[beginWord] = [[beginWord]]
        while layer:
            newlayer = collections.defaultdict(list)
            for word in layer:
                if word == endWord:
                    for ls in layer[word]:
                        res.append(ls)
                    return res
                else:
                    for i in range(len(word)):
                        for ch in 'abcdefghijklmnopqrstuvwxyz':
                            new = word[:i] + ch +word[i+1:]
                            if new in wordList:
                                newlayer[new] += [pre + [new] for pre in layer[word]]
                                
            wordList -= set(newlayer.keys())
            layer = newlayer
        return res
                
