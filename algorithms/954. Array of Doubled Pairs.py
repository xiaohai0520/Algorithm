Map to solve this problem.

Counter all the number.

check each number 
if n number is larger than 2n number   false
else update 2n number


class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        counter = collections.Counter(A)
        
        for n in sorted(counter, key=abs):
            print(n)
            if counter[n] > counter[n*2]:
                return False
            counter[n*2] -= counter[n]
        
        return True
        
        
        
        
#         dic = collections.Counter(A)
#         A.sort()
#         right = [i for i in A if i >= 0]
#         left = [i for i in A if i < 0][::-1]
        
#         if len(right)%2 != 0:
#             return False
#         for ls in [right,left]:
#             for num in ls:
#                 if num not in dic:
#                     continue
#                 else:
#                     dic[num] -= 1
#                     if dic[num] == 0:
#                         del dic[num]

#                     if 2 * num not in dic:
#                         return False
#                     else:
#                         dic[2 * num] -= 1
#                         if dic[2 * num] == 0:
#                             del dic[2 * num]
#         return True
