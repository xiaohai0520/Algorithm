backtracking
利用递归尝试每一个组和，
直到左边值或者右边值没有了 或者左边比右边大，（ 不可以比） 剩的要少，
时间复杂度 2^n

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n <= 0:
            return []
        res = []
        
        def dfs(l,r,path):
            if l == 0 and r == 0:
                res.append(path)
                return
            if l > r or l < 0 or r < 0:
                return 
            dfs(l-1,r,path+'(')
            dfs(l,r-1,path+')')
        dfs(n,n,'')
        return res
