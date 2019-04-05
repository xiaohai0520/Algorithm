# 先用第一个值和最后一个值判断是否递增
# 然后遍历 整个数组， 一直大或者一直小 继续， 不满足就跳出 return False


class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
#         if not A or len(A) < 3:
#             return True
#         a = True
#         b = True
#         for i in range(1,len(A)):
#             if A[i] < A[i-1]:
#                 a = False
          
#         for i in range(1,len(A)):
#             if A[i] > A[i-1]:
#                 b = False
#         return a or b
        if len(A)<3:
            return True
        prev = A[0]
        increase = A[0]<A[-1]
        for i in A[1:]:
            if increase and i>=prev or (not increase) and i<=prev:
                prev = i
            else:
                return False
        return True 
            
