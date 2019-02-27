class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # def backtrack(i):
        #     if i == n:
        #         res.append(list(board))
        #     for j in range(n):
        #         if j not in cols and j-i not in diag and j+i not in off_diag:
        #             cols.add(j)
        #             diag.add(j-i)
        #             off_diag.add(j+i)
        #             board.append("."*(j)+"Q"+"."*(n-j-1))
        #             backtrack(i+1)
        #             board.pop()
        #             off_diag.remove(j+i)
        #             diag.remove(j-i)
        #             cols.remove(j)
        # res = []
        # board = []
        # cols = set()
        # diag = set()
        # off_diag = set()
        # backtrack(0)
        # return res
        
        
        
        
        
        
        if n == 0:
            return []
        row = set()
        pre = set()
        last = set()
        res = []
        self.helper(n,0,res,[],row,pre,last)
        return res
    
    def helper(self,n,i,res,path,row,pre,last):
        if i == n:
            res.append(path[:])

        for j in range(n):
            if j not in row and (j - i) not in pre and (j + i) not in last:
                row.add(j)
                pre.add(j-i)
                last.add(j+i)
                path.append('.' * j + 'Q' + '.' * (n-j-1))
                self.helper(n,i+1,res,path,row,pre,last)
                path.pop()
                last.remove(j+i)
                pre.remove(j-i)
                row.remove(j)
                
