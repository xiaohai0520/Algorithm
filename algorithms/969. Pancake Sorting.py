# 找到要安排的数的index   把这个数flip到第一位上，然后再flip到适当的位置

class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        move = []
        for k in range(len(A),1,-1):
            index = A.index(k)+1
            if index == k:
                continue
            if index != 1:
                move.append(index)
                A = A[:index][::-1] + A[index:]
            move.append(k)
            A = A[:k][::-1] + A[k:]
        return move
