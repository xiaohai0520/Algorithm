class Solution:
    def maximum69Number (self, num: int) -> int:
        ls = list(str(num))
        for i,n in enumerate(ls):
            if n == '6':
                ls[i] = '9'
                break
        return int(''.join(ls))
