class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        
        dic = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'} 
        res = []


        self.dfs(dic,res,digits,"",0)
        return res
    
    
    def dfs(self,dic,res,digits,path,i):
        if i == len(digits):
            res.append(path)
            return
        
        for ch in dic[digits[i]]:
            self.dfs(dic,res,digits,path+ch,i+1)
                
