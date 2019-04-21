This is a greedy problem.

Each time we want to arrive the A == B

if A larger, add 2A  else add 2B

we also can get the A == B

then think about ab or ba

if A or B == 0

we only need to add all the rest.

Code:

class Solution:
    def strWithout3a3b(self, A: int, B: int) -> str:
        res = ""
        while A != B and A and B:
            if A > B:
                res += 'aab'
                A -= 2
                B -= 1
            else:
                res += 'bba'
                A -= 1
                B -= 2
        
        if A == B:
            if res:
                if res[-1] == 'a':
                    res += 'ba' * A
                else:
                    res += 'ab' * A
            else:
                res += 'ab' * A
        else:
            res += ('a' * A + 'b' * B)
        
        return res
                
            
                
                
