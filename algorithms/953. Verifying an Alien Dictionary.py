class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dic = {}
        for i,w in enumerate(order):
            dic[w] = i
        
        def compare(w1,w2):
            l1 = len(w1)
            l2 = len(w2)
            l = min(l1,l2)
            i = 0
            while i < l:
                if dic[w1[i]] == dic[w2[i]]:
                    i += 1
                    continue
                elif dic[w1[i]] < dic[w2[i]]:
                    return True
                else:
                    return False
                
            if l1 < l2:
                return True
            else:
                return False
        
        
        
        
        for i in range(len(words)-1):
            if not compare(words[i],words[i+1]):
                return False
        return True
        
        
        

            
