class Solution:
    def shortestWordDistance(self, words: List[str], word1: str, word2: str) -> int:
        cache = collections.defaultdict(list)
        for i,word in enumerate(words):
            cache[word].append(i)
        if word1 != word2:
            return min([abs(i-j) for i in cache[word1] for j in cache[word2]])
        else:
            return min([abs(cache[word1][i] - cache[word1][i+1]) for i in range(len(cache[word1])-1)])
