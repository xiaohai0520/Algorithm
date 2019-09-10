class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        d = set(words)
        cache = {}
        
        def dfs(word):
            if word in cache:
                return cache[word]
            cache[word] = False
            
            for i in range(1,len(word)):
                pre = word[:i]
                sur = word[i:]
                if pre in d and sur in d:
                    cache[word] = True
                    break
                if pre in d and dfs(sur):
                    cache[word] = True
                    break
                if sur in d and dfs(pre):
                    cache[word] = True
                    break
            return cache[word]
        
        res = []
        for word in words:
            if dfs(word):
                res.append(word)
        return res
        
