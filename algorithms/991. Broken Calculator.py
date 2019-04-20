This problem is a greedy problem.

We want to decrease the diff between x and y

if X > Y   only thing can do is -1

else X want to get y//2 quickly

So here we think use Y //2  if Y EVEN

else  Y + 1 // 2  if Y ODD

CODE:
class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        
        if X >= Y:
            return X-Y
        if Y %2 == 0:
            return  1 + self.brokenCalc(X,Y//2)
        else:
            return self.brokenCalc(X,Y+1) + 1
        
        
        
        
#         res = 0
#         while Y > X:
#             if Y % 2 == 0:
#                 Y //= 2
#             else:
#                 Y = (Y + 1)//2
#                 res += 1
            
#             res += 1
#         return res + X - Y
        
        
        
        
        
        # res = 0
        # queue = collections.deque([X])
        # l = len(queue)
        # while queue:
        #     for _ in range(l):
        #         cur = queue.popleft()
        #         if cur == Y:
        #             return res
        #         queue.append(cur*2)
        #         queue.append(cur-1)
        #     l = len(queue)
        #     res += 1
        # return 
