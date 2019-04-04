class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) < 3:
            return False
        i = 0
        j = len(A) - 1
        while i + 1 < len(A) and A[i] < A[i+1]: 
            i += 1
        while j > 0 and A[j] < A[j-1]: 
            j -= 1
            
        return  0 < i == j < len(A)-1
