#可以本地交换
#遍历偶数位， 如果是奇数，在奇数位上找一个偶数 进行交换


class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        res = [0] * len(A)
        i = 0
        j = 1
        while A:
            cur = A.pop()
            if cur % 2 == 0:
                res[i] = cur
                i += 2
            else:
                res[j] = cur
                j += 2
        return res
