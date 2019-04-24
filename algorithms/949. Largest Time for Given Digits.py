class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        
        ls = []
        
        def dfs(path,B):
            if len(path) == len(A):
                ls.append(path)
                return 
            for i in range(len(B)):
                dfs(path+[B[i]],B[:i]+B[i+1:])
                
                
        dfs([],A)
        print(ls)
        ls = [(str(p[0])+str(p[1]),str(p[2])+str(p[3])) for p in ls]
        ls = [p for p in ls if  '00'<= p[0] <= '23' and '00' <= p[1] <= '59']
        if not ls:
            return ''
        ls.sort(key=lambda x:(x[0],x[1]))
        
        return ls[-1][0] + ':'+ls[-1][1] 
