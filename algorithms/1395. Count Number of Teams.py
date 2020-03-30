class Solution:
    def numTeams(self, rating: List[int]) -> int:
        
        
        self.res = 0
        
        def increase(start,path):
            if len(path) == 3:
                self.res += 1
                return
            for i in range(start,len(rating)):
                if not path or rating[i] > path[-1]:
                    path.append(rating[i])
                    #print(path)
                    increase(i+1,path)
                    path.pop()
                    
        def decrease(start,path):
            if len(path) == 3:
                self.res += 1
                return
            for i in range(start,len(rating)):
                if not path or rating[i] < path[-1]:
                    path.append(rating[i])
                    decrease(i+1,path)
                    path.pop()
                    
        increase(0,[])
        decrease(0,[])
        return self.res
    
    
                    
