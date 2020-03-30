class Solution:
    def sortString(self, s: str) -> str:
        result=[]
        s=list(s)
        
        flag=True
        while len(s):
            if flag:
                temp=sorted(set(s))
            else:
                temp=sorted(set(s),reverse=True)
            for ch in temp: s.remove(ch)
            result.extend(temp)
            flag=not flag
        return "".join(result)
        
        
        
        
        
        # dic = collections.Counter(s)
        # res = ''
        # ls = sorted(list(set(s)))
        # print(ls)
        # flag = 1
        # while dic:
        #     if flag:
        #         for each in ls:
        #             if each in dic:
        #                 res += each
        #                 dic[each] -= 1
        #                 if dic[each] == 0:
        #                     del dic[each]
        #         flag = 0
        #     else:
        #         for each in ls[::-1]:
        #             if each in dic:
        #                 res += each
        #                 dic[each] -= 1
        #                 if dic[each] == 0:
        #                     del dic[each]
        #         flag = 1
        # return res
