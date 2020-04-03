class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        s = sum(arr[:k])
        if s/k >= threshold: res+= 1
        for i in range(k,len(arr)):
            s += arr[i]
            s -= arr[i-k]

            if s/k >= threshold:
                res += 1
        return res 
