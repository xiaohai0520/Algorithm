Hash table problem,

Use the map to save the number of char in the first world.

For each char, we go to get the min val in all the words.

Code:

class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        if not A:
            return []
        if len(A) == 1:
            return [i for i in A[0]]
        c = collections.Counter(A[0])
        res = []
        
        for key in c:
            j = c[key]
            for i in range(1,len(A)):
                cur = A[i].count(key)
                j = min(j,cur)
            res += [key]*j
        return res
