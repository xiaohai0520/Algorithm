
建立一个字典 将括号方向存进去，为的是pop出来之后可以比较，
利用栈的lifo原则 来进行比较即可。


class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        stack = []
        dic = {')':'(', ']':'[','}':'{'}
        stack = []
        
        for ch in s:
            if ch not in dic:
                stack.append(ch)
            else:
                if not stack:
                    return False
                cur = stack.pop()
                if cur != dic[ch]:
                    return False
        return not stack
