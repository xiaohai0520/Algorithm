一行一行往下backtrack
每次往下一行，都要检查当前列和两个斜对角
当最后一行也通过时，则加入结果集

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 0:
            return []
        
        
        res = []
        row = set()
        pre = set()
        last = set()
        
        def dfs(i,path):
            if i == n:
                res.append(path)
                return
            for j in range(n):
                if j not in row and (j-i) not in pre and (j+i) not in last:
                    row.add(j)
                    pre.add(j-i)
                    last.add(j+i)
                    dfs(i+1,path+['.' * j + 'Q'+'.'*(n-j-1)])
                    row.remove(j)
                    pre.remove(j-i)
                    last.remove(j+i)
        dfs(0,[])
        return res
        
