class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        crows = 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
        
        c1 = collections.Counter(secret)
        c2 = collections.Counter(guess)
        
        for each in c1:
            crows += min(c1[each],c2[each])
        return str(bulls)+ 'A'+ str(crows-bulls) + 'B'
