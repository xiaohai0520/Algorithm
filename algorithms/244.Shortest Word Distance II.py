#use dic to save index , o(m+n) to find the minimun dis

class WordDistance(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.dic = {}
        for i,word in enumerate(words):
            self.dic[word] = self.dic.get(word,[]) + [i]

    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        
        l1 = self.dic[word1]
        l2 = self.dic[word2]
        i = j = 0
        # return min([abs(n1 - n2) for n2 in l2 for n1 in l1])
        res = float('inf')
        while i < len(l1) and j < len(l2):
            res = min(res, abs(l1[i]-l2[j]))
            if l1[i] < l2[j]:
                i += 1
            else:
                j += 1
        return res
        
        
        


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)
