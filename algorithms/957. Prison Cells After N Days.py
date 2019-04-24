We need to find the loop in the change.
Then get the remainder to change the state.

Code:

class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        seen = {}
        while N > 0:
            seen[tuple(cells)] = N 
            N -= 1
            cells = self.nextday(cells)
            if tuple(cells) in seen:
                N %= seen[tuple(cells)] - N
        return cells
    
    
    
    def nextday(self,cells):
        res = [0]
        for i in range(1,len(cells)-1):
            if cells[i-1] == cells[i+1]:
                res.append(1)
            else:
                res.append(0)
        res.append(0)
        return res
