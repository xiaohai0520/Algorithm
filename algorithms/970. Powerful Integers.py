We can also solve this problem with while loop.

each time we add the x value,

we try every possible of y value.


We can also solve it with recursive.

code:

class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        res = set()
        def dfs(i,j):
            
            cur = x ** i + y ** j
            # print(cur)
            if cur > bound:
                return 
            res.add(cur)
            if x != 1:
                dfs(i+1,j)
            if y != 1:
                dfs(i,j+1)
        dfs(0,0)
        return list(res)
