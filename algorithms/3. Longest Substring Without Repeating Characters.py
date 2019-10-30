# literate for head to tail
# use dic to save the duplicate char's index 
# 初始化起始位置为0， 最长不重复长度为0。
# 遍历字符串，使用字典存储每个字符的index，如果遇见出现过的字符，并且字符出现的index 比此时的起始位置更靠后，应该更新起始位置为index+1。

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        dic = {}
        start = 0
        for i,ch in enumerate(s):
            if ch in dic and dic[ch] >= start:
                start = dic[ch] + 1
            else:
                res = max(res,i-start+1)
            dic[ch] = i
        return res
               
        
        
        
        
        
        
        
        
        
        
