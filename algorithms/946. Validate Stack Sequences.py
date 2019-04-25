Use a stack to simulate the push and pop.

if stack[-1] not equal the pop[i]  push into the stack


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        i = 0
        j = 0
        while j < len(popped):
            while (not stack or stack[-1] != popped[j]) and i < len(pushed):
                stack.append(pushed[i])
                i += 1
            if stack[-1] != popped[j]:
                return False
            stack.pop()
            j += 1
            
        return True          
