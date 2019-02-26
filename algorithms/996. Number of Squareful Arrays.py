class Solution:
    def numSquarefulPerms(self, A: List[int]) -> int:
        if not A:
            return 0
        A.sort()
        used = [False]*len(A)
        self.res = 0
        self.helper(A,[],used)
        return self.res
    
    def helper(self,A,path,used):
        if len(path) == len(A):
            self.res += 1
            return
        for i in range(len(A)):
            if used[i] or( i > 0 and not used[i-1] and A[i] == A[i-1]):
                continue
            if not path or math.sqrt(path[-1] + A[i])%1 == 0:
                used[i] = True
                self.helper(A,path+[A[i]],used)
                used[i] = False
                
