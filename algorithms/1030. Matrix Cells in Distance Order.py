This a 2d array problem.

Easy to solve, get all the pairs and sort them with the distance.

code:
class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
#         dic = collections.defaultdict(list)
#         check = set()
        
#         queue = collections.deque([(r0,c0,0)])
#         check.add((r0,c0))
#         while queue:
#             r,c,l = queue.popleft()
#             dic[l].append([r,c])
#             for pair in [(0,1),(0,-1),(1,0),(-1,0)]:
#                 newr = r + pair[0]
#                 newc = c + pair[1]
#                 if (newr,newc) not in check and 0 <= newr < R and 0 <= newc < C:
#                     check.add((newr,newc))
#                     queue.append((newr,newc,l+1))
#         res = []
#         for key in sorted(dic.keys()):
#             res += dic[key]
#         return res
    
        return sorted([[r, c] for r in range(R) for c in range(C)], key=lambda x : (abs(x[0] - r0) + abs(x[1] - c0)))
                    
            
           
            
