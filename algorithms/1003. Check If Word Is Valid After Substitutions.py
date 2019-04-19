This problem use the stack to save.

we append char into stack, when meet c need to pop out two previous char,if not a b ,return False.

At last, the stack should be empty.

Code:


class Solution:
    def isValid(self, S: str) -> bool:
        stack = []
        for s in S:
            if s != 'c':
                stack.append(s)
            else:
                for i in range(2):
                    if i == 0:
                        if not stack:
                            return False
                        else:
                            if stack.pop() != 'b':
                                return False
                    else:
                        if not stack:
                            return False
                        else:
                            if stack.pop() != 'a':
                                return False
        return not stack
