This is a two pointers question.

We use i and j two pointers, j each time go one step

If the number is 0, we check k, if k < 0 i++

if i previous position is 0, means we use k here, so k++

at last ,i - j is the length all 1.

Code

class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        i = 0
        for index in range(len(A)): 
            if (A[index] == 0):
                    K -= 1
                    
            if K >= 0: 
                continue
                    
            else:
                i += 1
                if A[i-1] == 0:
                    K += 1
             
        return index -i + 1
        
        
#         queue = collections.deque([])
#         res = 0
#         remaind = K
#         start = 0
#         for i,a in enumerate(A):
#             # print(queue)
#             if a == 1:
#                 res = max(res,i-start+1)
#             else:
#                 if K == 0:
#                     start = i + 1
#                 else:
#                     if remaind > 0:
                        
# #                         queue.append(i)
#                         remaind -= 1
#                     else:
#                         cur = queue.popleft()
#                         start = cur + 1
#                     queue.append(i)
#                     res = max(res,i-start+1)
#         return res
                        
            
