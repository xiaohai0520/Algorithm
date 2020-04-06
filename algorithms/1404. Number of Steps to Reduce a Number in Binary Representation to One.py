class Solution:
    def numSteps(self, s: str) -> int:
        def add1(s):
            #flag = 0
            ls = list(s)
            ls[-1] = '0'
            for i in range(len(ls)-2,-1,-1):
                if ls[i] == '0':
                    ls[i] = '1'
                    return ''.join(ls)
            return '1' + '0' * len(ls)
                
            
        def divide2(s):
            return s[:-1]
        
        step = 0
        #print(s)
        while s != '1':
            if s[-1] == '0':
                s = divide2(s)
            else:
                s = add1(s)
            #print(s)
            step += 1
        return step
            
