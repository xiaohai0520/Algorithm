class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        import re
        if not paragraph:
            return ""
        ban = set(banned)
        paragraph = re.split('\W+',paragraph.lower())
        paragraph = [s for s in paragraph if s !='' and s not in ban]
        dic = {}
        for word in paragraph:
            if word in dic:
                dic[word] += 1
            else:
                dic[word] = 1
        words = list(dic.items())
        words.sort(key=lambda x:-x[1])
        return words[0][0]
        
