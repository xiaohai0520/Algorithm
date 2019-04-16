String problem.

We can split first and move out the outer parathese later.

We can also use count to check whether need to add each char.

if count > 0 means skip a '(', if count > 1, means we can add the not last ')'.

Code:
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        if not S:
            return ''
        count = 0
        res = ''
        for s in S:
            if s == '(':
                if count > 0:
                    res += s
                count += 1
            else:
                if count >1:
                    res += s
                count -= 1
        return res
                    
            
#         l = r = 0
#         res = ''
#         cur = ''
#         for i in range(len(S)):
#             if S[i] == '(':
#                 l += 1
#             else:
#                 r += 1
#             cur += S[i]  
#             # if l != r or (l == 0 and r == 0):
                
            
                
#             if l == r and (l != 0 and r != 0):
#                 res += cur[1:-1]
#                 cur = ''
#                 l = r = 0
#         return res
                
                
            
