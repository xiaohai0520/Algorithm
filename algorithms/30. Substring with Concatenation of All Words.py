import collections

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not words:
            return []
        count = collections.Counter(words)
        l = len(words[0])
        res = []
        
        for start in range(l):
            temp_counter = count.copy()
            match = 0
            for end in range(start,len(s),l):
                word = s[end:end+l]
                if word in temp_counter:
                    temp_counter[word] -= 1
                    match += 1
                    
                    while temp_counter[word] < 0:
                        pre = s[start:start+l]
                        temp_counter[pre] += 1
                        match -= 1
                        start += l
                        
                    if match == len(words):
                        res.append(start)
                else:
                    for i in range(start,end,l):
                        pre = s[i:i+l]
                        temp_counter[pre] +=1
                        match -= 1
                    start = end + l
                    match = 0
        return res
