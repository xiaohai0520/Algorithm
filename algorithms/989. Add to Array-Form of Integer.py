class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        if not A:
            return list(map(int,list(str(K))))
        K = list(map(int,list(str(K))))
        queue = collections.deque()
        ten = 0
        while A or K or ten:
            a = k = 0
            if A:
                a = A.pop()
            if K:
                k = K.pop()
            ten, res = divmod(a + k + ten,10)
            queue.appendleft(res)

        
        return list(queue)
            
        
