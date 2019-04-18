class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        
        
        
        A.sort()
        left = [a for a in A if a < 0]
        right = [a for a in A if a >= 0]
        
        l = len(left)
        
        if K <= l:
            for i in range(K):
                left[i] = -left[i]
            return sum(left) + sum(right)
        else:
            if (K - l) % 2 == 0:
                return -sum(left) + sum(right)
            else:
                if not left:

                    return sum(right[1:]) - right[0]
                elif not right:
                    return -sum(left[:-1]) - left[-1]
                else:
                    return -sum(left[:-1]) + sum(right) + left[-1] if abs(left[-1]) < right[0] else -sum(left) + sum(right[1:]) - right[0]
        
