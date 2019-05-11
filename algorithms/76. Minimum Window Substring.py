class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        from collections import defaultdict
        left = 0
        right = 0
        counts = defaultdict(int)
        count_t = defaultdict(int)
        for c in t:
            count_t[c] += 1
        min_length = float('inf')
        res = ''
        while right < len(s):
            counts[s[right]] += 1
            while self.check(counts,count_t):
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    res = s[left:right+1]
                counts[s[left]] -= 1
                if counts[s[left]] == 0:
                    del counts[s[left]]
                left += 1
            right += 1
        
        return res
    
    def check(self,counts,count_t):
        for key in count_t.keys():
            if key not in counts or count_t[key] > counts[key]:
                return False
        return True
