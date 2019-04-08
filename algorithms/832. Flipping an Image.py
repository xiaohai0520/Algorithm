class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        def invert(ls):
            for i in range(len(ls)):
                if ls[i] == 0:
                    ls[i] = 1
                else:
                    ls[i] = 0
            return ls
        for i in range(len(A)):
            # A[i] = A[i][::-1]
            A[i] = invert(A[i][::-1])
        return A
