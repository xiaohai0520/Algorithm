This is a string problem.

Just need to change each number in to binary and check if it is in the S

The internel function in python translate number to binary is bin()

code:

class Solution:
    def queryString(self, S: str, N: int) -> bool:
        for i in range(1,N + 1):
            target = bin(i)
            if str(target)[2:] not in S:
                return False
        return True

    

                
