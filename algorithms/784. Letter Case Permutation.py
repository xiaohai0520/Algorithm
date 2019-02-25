class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        res = [S]
        for i, c in enumerate(S):
            if c.isalpha():
                res.extend([s[:i] + s[i].swapcase() + s[i+1:] for s in res])
        return res
        
        
        
#         res = ['']
#         for ch in S:
#             if ch.isalpha():
#                 res = [r + new for r in res for new in [ch.upper(),ch.lower()]]
#             else:
#                 res = [r + ch for r in res]
#         return res
        
              
        
        
        # if not S:
        #     return ['']
#         res = []
#         self.helper(S,res,0)
#         return res
        
#     def helper(self,S,res,index):
#         if index == len(S):
#             res.append(S)
#             return
#         if S[index].isalpha():
#             self.helper(S[:index] + S[index].lower() + S[index+1:],res,index+1)
#             self.helper(S[:index] + S[index].upper() + S[index+1:],res,index+1)
#         else:
#             self.helper(S,res,index+1)
        
