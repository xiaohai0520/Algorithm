#dfs  time complictiy is O(n2) 
#use math method, k// factorial(n-1) get the first number and continue k% factorial(n-1) = remaining part


class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        
        
        res, nums = "", [i+1 for i in range(n)]
        k -= 1
        while n:
            n -= 1
            index, k = divmod(k, math.factorial(n))
            res += str(nums.pop(index))
        return res
#         if n == 1 and k != 1:
#             return ''
#         res = []
#         self.dfs([i+1 for i in range(n)],'',res)
#         return res[k-1]
    
    
#     def dfs(self,array,path,res):
#         if not array:
#             res.append(path)
#             return
#         for i in range(len(array)):
#             newarray = array[:i] + array[i+1:]
#             self.dfs(newarray,path+str(array[i]),res)

