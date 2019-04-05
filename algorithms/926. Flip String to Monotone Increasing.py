# 单独数组  多为DP
# 次数最大是将所有的1都翻成0  res = len - c0
# 我们要做的是 选定一个1， 将之前的1都翻成0   之后的0 都翻成1
# 开始查出一共有多少个0   为 后面的0 的总数，  c0 = count(0)   
# c1 = 0  前面的1 初始化为0
# 遍历数组，如果是0   c0 - 1, 如果是1， 翻得次数 应该为 c0 + c1   与res 比较 取小   c1 + 1
# 最后得到res 为最小值





class Solution:
    def minFlipsMonoIncr(self, S: str) -> int:
        if not S:
            return 0
        n = len(S)
        c0 = S.count('0')
        c1 = 0
        res = n-c0
        
        for s in S:
            if s == '0':
                c0 -= 1
            else:
                res = min(res,c0 + c1)
                c1 += 1
        return res
