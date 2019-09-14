class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        nums = [i for i in range(n)]
        
        
        def find(x):
            if nums[x] != x:
                nums[x] = find(nums[x])
            return nums[x]
        def union(x,y):
            res1 = find(x)
            res2 = find(y)
            
            if res1 != res2:
                nums[res1] = res2
                
        for e1,e2 in edges:
            union(e1,e2)
        
        res = [find(x) for x in range(n)]
        return len(set(res))
