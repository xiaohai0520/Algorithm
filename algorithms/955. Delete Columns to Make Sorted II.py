Greedy problem.

We need to compare each pair in the order.

From the first pair, if it satisfy all the conditions goto the next pair

when we meet the bad order, delete that char, start from the first pair again until we can arrive the tail.


class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        
        idx=set()
        i=1
        while i<len(A):
            for j in range(len(A[i])):
                if j in idx or A[i-1][j]==A[i][j]:
                    continue
                if A[i-1][j]>A[i][j]:
                    idx.add(j)
                    i=0
                break
            i+=1
        return len(idx)
        
        
#         for i in range(len(A[0])):
#             orders = self.getallorders(i,A)
#             # print(orders)
#             for order in orders:
#                 if self.helper(A,order):
#                     return i
#         return len(A[0])
                       
    
#     def getallorders(self,l,A):
#         res = []
#         arr = [i for i in range(len(A[0]))]
        
#         def dfs(l,path,res,start):
#             if l == 0:
#                 res.append(path)
#                 return
#             for i in range(start,len(arr)):
#                 dfs(l-1,path+[arr[i]],res,i+1)
#         dfs(l,[],res,0)
        
#         return res
                
          
    
#     def helper(self,A,order):
#         res = []
#         for a in A:
#             cur = ''
#             order = set(order)
            
#             for i in range(len(a)):
#                 if i not in order:
#                     cur += a[i]
             
#             res.append(cur)
        
#         for i in range(len(res)-1):
#             if res[i] > res[i+1]:
#                 return False
        return True
            
                
