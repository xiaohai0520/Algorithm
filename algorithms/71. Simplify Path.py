class Solution:
    def simplifyPath(self, path: str) -> str:
        ls = path.split('/')
        ls = [c for c in ls if c != '']
        stack = []
        
        for c in ls:
            if c == '..':
                if stack:
                    stack.pop()
            elif c == '.':
                pass
            else:
                stack.append(c)
        return '/' + '/'.join(stack)
