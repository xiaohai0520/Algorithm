
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        ans=[]
        def canAdd(x):
            return len(ans)<2 or ans[-1]!=x or ans[-2] != x
        d=[[a,"a"],[b,"b"], [c, "c"]]
        total=a+b+c
        while total>0:
            d.sort(reverse=True)
            for i, (k, c) in enumerate(d):
                if k==0: continue
                if canAdd(c):
                    ans.append(c)
                    d[i][0]-=1
                    total-=1
                    break
            else:
                break
        return "".join(ans)
        
        
        
        
#         ls = []
#         if a > 0:ls.append(('a',a))
#         if b > 0:ls.append(('b',b))
#         if c > 0:ls.append(('c',c))
            
#         res = ''
#         while ls:
#             ls.sort(key = lambda x:(x[1],x[0]))
#             ch,n = ls.pop()
#             if not ls:
#                 res += 2 * ch if n >= 2 else ch
#                 return res 
#             ch2,n2 = ls.pop()
#             if n - n2 >= 2:
#                 res += 2 * ch
#                 n -= 2
#                 if n <= n2 and n2 >= 2:
#                     res += ch2 * 2
#                     n2 -= 2
#                 else:
#                     res += ch2
#                     n2 -= 1
#             else:
                
#                 res += 2 * ch if n >= 2 else ch
#                 n -= 2 if n >= 2 else 1
#                 res += 2 * ch2 if n2 >= 2 else ch2
#                 n2 -= 2 if n2 >= 2 else 1
            
                
#             if n > 0:ls.append((ch,n))
#             if n2 > 0: ls.append((ch2,n2))
#         return res
            
        
        
