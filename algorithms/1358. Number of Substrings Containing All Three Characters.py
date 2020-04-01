class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        
        res = 0
        ls = [-1] * 3
        for i, ch in enumerate(s):
            ls[ord(ch) - ord('a')] = i
            res += min(ls) + 1
        return res
        
        
        
        
        
        
        
        a,b,c = [],[],[]
        for i in range(len(s)):
            if s[i] =='a':a.append(i)
            elif s[i] == 'b':b.append(i)
            else:c.append(i)
        ans,i = 0,0
        while a and b and c:
            char,v = s[i],0
            if char =='a':
                v = max(b[0],c[0])
                a.pop(0)
            elif char =='b':
                v = max(a[0],c[0])
                b.pop(0)
            else:
                v = max(a[0],b[0])
                c.pop(0)
            ans = ans + len(s)-v
            i+=1
        return ans
