class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        ban = set(banned)
        paragraph = [s.strip("!?',;.") for s in paragraph.lower().split(' ')] 

        p = [w for w in paragraph if w not in ban]
        dic = {}
        for w in p:
            if w in dic:
                dic[w] += 1
            else:
                dic[w] = 1
                
        cur = [(v,k) for k,v in dic.items()]
        cur.sort(key=lambda x:-x[0])
        return cur[0][1]
