class Solution:
    def totalNQueens(self, n: int) -> int:
        if n == 0:
            return 0
        self.res = 0
        col = set()
        dia = set()
        b_dia = set()
        self.helper(n,0,col,dia,b_dia)
        return self.res
    
    def helper(self,n,i,col,dia,b_dia):
        if i == n:
            self.res += 1
        for j in range(n):
            if j not in col and (j-i) not in dia and (j+i) not in b_dia:
                col.add(j)
                dia.add(j-i)
                b_dia.add(j+i)
                self.helper(n,i+1,col,dia,b_dia)
                col.remove(j)
                dia.remove(j-i)
                b_dia.remove(j+i)
