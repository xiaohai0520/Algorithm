#use stack 


class Solution:
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        res = [0 for i in range(len(temperatures))]  
        
        stack = []
        
        for i,t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                cur = stack.pop()
                res[cur] = i - cur
            stack.append(i)
        return res
            
