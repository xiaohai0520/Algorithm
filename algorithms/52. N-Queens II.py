class Solution:
    def totalNQueens(self, n: int) -> int:
        if n == 0:
            return []
        row = set()
        pre = set()
        last = set()
        self.res = 0
        self.helper(n,0,[],row,pre,last)
        return self.res
    
    def helper(self,n,i,path,row,pre,last):
        if i == n:
            self.res += 1

        for j in range(n):
            if j not in row and (j - i) not in pre and (j + i) not in last:
                row.add(j)
                pre.add(j-i)
                last.add(j+i)
                path.append('.' * j + 'Q' + '.' * (n-j-1))
                self.helper(n,i+1,path,row,pre,last)
                path.pop()
                last.remove(j+i)
                pre.remove(j-i)
                row.remove(j)
