class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        if not A or not queries:
            return []
        res = []
        
        cur = sum([i for i in A if i%2 == 0])
        
        
        for query in queries:
            val,index = query
            pre = A[index]
            
            if pre %2 == 0:
                if val % 2 == 0:
                    cur += val
                    
                else:
                    cur -= pre
                    
            else:

                if val %2 != 0:
                    cur += pre + val
                    
            res.append(cur)
            A[index] += val
            
        return res
