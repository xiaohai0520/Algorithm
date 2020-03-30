class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        dic = {0:-1}
        vowels = 'aeiou'
        state = 0
        ans = 0
        for i in range(len(s)):
            j = vowels.find(s[i])
            if j >= 0: state ^= 1 << j
            if state not in dic:
                dic[state] = i
            else:
                ans = max(ans,i - dic[state])
        return ans
            
            
