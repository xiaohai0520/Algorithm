class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        # dic = {}
        # for i,w in enumerate(words):
        #     if w not in dic:
        #         dic[w] = [i]
        #     else:
        #         dic[w].append(i)
        # l1 = dic[word1]
        # l2 = dic[word2]
        # return min([abs(a-b) for a in l1 for b in l2])
    
    
        i1, i2 = -1, -1
        
        res = len(words)
        
        for i, word in enumerate(words):
            if word == word1:
                i1 = i
            elif word == word2:
                i2 = i
            if i1 != -1 and i2 != -1:
                res = min(res, abs(i2 - i1))
        return res
